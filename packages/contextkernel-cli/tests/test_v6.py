"""Integration acceptance tests against isolated projects and user profiles."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

import pytest

REPO = Path(__file__).resolve().parents[1]
if REPO.name == "contextkernel-cli":
    REPO = REPO.parents[1]
RUNTIME = REPO / "tools/icontext_runtime"
sys.path.insert(0, str(RUNTIME))
import context_runtime as runtime
import icontext_cli as cli
import skill_installer


def snapshot(root):
    return {p.relative_to(root).as_posix(): (p.read_bytes(), p.stat().st_mtime_ns)
            for p in root.rglob("*") if p.is_file()}


def project(root):
    (root / "src").mkdir(parents=True)
    (root / "src/main.py").write_text("def greet(name: str) -> str:\n    return name\n", encoding="utf-8")
    return root


def seed(root):
    (root / "01_seed").mkdir(exist_ok=True)
    (root / "01_seed/seed-demo-master.md").write_text(
        '<SEED_ARCHITECTURAL_VECTOR version="6.0" contains_source_code="false">\n'
        '### 0.1 Instrucciones para el modelo receptor\n' +
        '\n'.join(f'## {i}. Architecture\n' for i in range(11)) +
        '\ngreet(name: str) -> str\n## CONTEXT HANDOFF\n</SEED_ARCHITECTURAL_VECTOR>\n', encoding="utf-8")


def readmes(root):
    for name in ("README.md", "README_ES.md"):
        (root / name).write_text('[English](README.md) | [Español](README_ES.md)\n' +
                                 '\n'.join(f'## {i}. Section\nAuthored project-specific content.' for i in range(1, 9)), encoding="utf-8")


def test_inventory_tracks_dirty_add_delete_rename_and_full_verification(tmp_path):
    root = project(tmp_path)
    first, _ = runtime.contracts_index(root, persist=True)
    same, stats = runtime.contracts_index(root, persist=True)
    assert same == first
    assert stats["files_read"] == stats["ast_parses"] == 0
    file = root / "src/main.py"
    stamp = file.stat()
    file.write_text(file.read_text().replace('greet', 'hello'), encoding="utf-8")
    os.utime(file, ns=(stamp.st_atime_ns, stamp.st_mtime_ns))
    changed, _ = runtime.contracts_index(root, full=True, persist=True)
    assert 'hello' in changed['public_symbols']
    assert first['contracts_ast_hash'] != changed['contracts_ast_hash']
    file.rename(root / "src/renamed.py")
    _, delta = runtime.inventory(root)
    assert delta['renamed'] == [{'from': 'src/main.py', 'to': 'src/renamed.py'}]
    assert 'src/main.py' in delta['removed']
    assert 'src/renamed.py' in delta['added']


def test_inherited_pruning_and_gitignore(tmp_path):
    root = project(tmp_path)
    forbidden = root / "src/pruned/child"
    forbidden.mkdir(parents=True)
    (forbidden.parent / ".context.yaml").write_text('crawl: false\n')
    (forbidden / "secret.py").write_text('raise RuntimeError("must not read")')
    (root / ".gitignore").write_text('ignored/\n')
    (root / "ignored").mkdir()
    (root / "ignored/file.txt").write_text('excluded')
    inv, _ = runtime.inventory(root)
    assert all('pruned' not in k and not k.startswith('ignored/') for k in inv['files'])


def test_queries_and_dry_run_do_not_write_even_without_context(tmp_path):
    root = project(tmp_path)
    before = snapshot(root)
    cli.status(root)
    cli.audit(root)
    inv, delta = runtime.inventory(root)
    cli.request(root, 'seed', inv, cli.layer_hash(inv, 'seed', root), delta)
    result, code = cli.sync(root, REPO.parent, dry_run=True)
    assert code == 0 and result['dry_run']
    assert snapshot(root) == before


def test_complete_rejects_stale_inputs(tmp_path):
    root = project(tmp_path)
    inv, _ = runtime.inventory(root)
    expected = cli.layer_hash(inv, 'seed', root)
    seed(root)
    (root / 'src/main.py').write_text('def changed(): return 1\n')
    with pytest.raises(ValueError, match='Inputs changed'):
        cli.complete(root, 'seed', expected)


def test_sync_handoff_and_noop_are_idempotent(tmp_path, monkeypatch):
    root = project(tmp_path)
    result, code = cli.sync(root, REPO.parent)
    assert code == 3 and result['requests'][0]['layer'] == 'seed'
    assert result['layers']['metrics']['state'] == 'blocked_by_seed'
    seed(root)
    inv, _ = runtime.inventory(root)
    cli.complete(root, 'seed', cli.layer_hash(inv, 'seed', root))
    def fake_metrics(root, eco, full=False):
        for path in cli.outputs(root, 'metrics'):
            runtime.atomic_write(path, '{}' if path.suffix == '.json' else 'Measured report')
    monkeypatch.setattr(cli, 'metrics', fake_metrics)
    result, code = cli.sync(root, REPO.parent)
    assert code == 3 and result['requests'][0]['layer'] == 'readme'
    readmes(root)
    inv, _ = runtime.inventory(root)
    cli.complete(root, 'readme', cli.layer_hash(inv, 'readme', root))
    result, code = cli.sync(root, REPO.parent)
    assert code == 0
    before = snapshot(root)
    result, code = cli.sync(root, REPO.parent)
    assert code == 0 and snapshot(root) == before


def test_required_failure_blocks_dependents(tmp_path, monkeypatch):
    root = project(tmp_path)
    seed(root)
    inv, _ = runtime.inventory(root)
    cli.complete(root, 'seed', cli.layer_hash(inv, 'seed', root))
    def fail(*args, **kwargs):
        raise RuntimeError('test failure')
    monkeypatch.setattr(cli, 'metrics', fail)
    result, code = cli.sync(root, REPO.parent)
    assert code == 1
    assert result['layers']['readme']['state'] == 'blocked_by_metrics'


def test_parallel_publish_retains_all_producers(tmp_path):
    processes = []
    for layer in ('l0', 'l1', 'l2', 'l3'):
        code = f"import sys;sys.path.insert(0,{str(RUNTIME)!r});from context_runtime import publish_layer;publish_layer({str(tmp_path)!r},{layer!r},{{'present':True,'state':'validated'}})"
        processes.append(subprocess.Popen([sys.executable, '-B', '-c', code]))
    assert all(p.wait(timeout=30) == 0 for p in processes)
    bus = runtime.read_json(tmp_path / '.context/icontext_bus.json')
    assert all(record['present'] for record in bus['layers'].values())
    before = snapshot(tmp_path)
    runtime.publish_layer(tmp_path, 'l0', {'present': True, 'state': 'validated'})
    assert snapshot(tmp_path) == before


def test_bundles_install_equally_and_repeat_without_writes(tmp_path):
    before = snapshot(tmp_path)
    skill_installer.install(REPO.parent, ['antigravity', 'codex'], tmp_path, dry_run=True)
    assert snapshot(tmp_path) == before
    result = skill_installer.install(REPO.parent, ['antigravity', 'codex'], tmp_path)
    assert result['state'] == 'installed'
    assert not skill_installer.inspect_installation(REPO.parent, tmp_path)['errors']
    for name in skill_installer.SKILLS:
        assert (tmp_path / '.agents/skills' / name / 'SKILL.md').read_bytes() == (tmp_path / '.gemini/config/skills' / name / 'SKILL.md').read_bytes()
    before = snapshot(tmp_path)
    assert skill_installer.install(REPO.parent, ['antigravity', 'codex'], tmp_path)['writes'] == 0
    assert snapshot(tmp_path) == before


def test_runtime_can_run_without_sibling_repositories(tmp_path):
    isolated = tmp_path / 'independent'
    shutil.copytree(RUNTIME, isolated)
    root = project(tmp_path / 'project')
    result = subprocess.run([sys.executable, '-B', str(isolated / 'icontext_cli.py'), 'status', '--target', str(root), '--json'], capture_output=True, text=True)
    assert result.returncode == 0 and json.loads(result.stdout)['project'] == 'project'
    result = subprocess.run([sys.executable, '-B', str(isolated / 'icontext_cli.py'), 'pack', str(root), '--json'], capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr


def test_no_command_only_shows_help(tmp_path):
    before = snapshot(tmp_path)
    result = subprocess.run([sys.executable, '-B', str(REPO / 'icontext.py')], cwd=tmp_path, capture_output=True, text=True)
    assert result.returncode == 0 and 'usage:' in result.stdout
    assert snapshot(tmp_path) == before


def test_missing_metrics_does_not_become_a_perfect_score(tmp_path):
    import fwengine
    report = tmp_path / 'artifacts/plans/metricsthinking/MetricsThinking.json'
    report.parent.mkdir(parents=True)
    report.write_text(json.dumps({'consolidated_score': 42, 'fpai': {'power_factor_spectral': .7, 's_spectral': 200}, 'security': {'pii_matches_count': 1}}))
    layer = fwengine.sync_icontext_bus(tmp_path, write_to_disk=False)['layers']['l2_metricsthinking']
    assert layer['fpai_pf_spectral'] == .7 and layer['fpai_s_spectral'] == 200 and layer['security_gate'] == 0
    report.write_text('{}')
    assert 'l2_metricsthinking' not in fwengine.sync_icontext_bus(tmp_path, write_to_disk=False)['layers']


def test_sessions_are_isolated_and_can_resume_from_another_host(tmp_path):
    import fwengine
    assert fwengine.manage_checkpoint(tmp_path) == {}
    assert not (tmp_path / '.context').exists()
    first = fwengine.manage_checkpoint(tmp_path, action='set', session_id='antigravity-task',
                objective='Implement a bounded context pack', constraints=['Preserve the public CLI'],
                next_action='Run the acceptance fixture', evidence_hash='a' * 64)
    fwengine.manage_checkpoint(tmp_path, action='set', session_id='codex-other', objective='Other task')
    resumed = fwengine.manage_checkpoint(tmp_path, session_id='antigravity-task')
    assert resumed == first
    assert resumed['constraints'] == ['Preserve the public CLI']


def test_context_payload_is_bounded_and_expansion_is_explicit(tmp_path):
    root = project(tmp_path)
    (root / 'pyproject.toml').write_text('[project]\nname = "demo"\n')
    (root / '.context').mkdir()
    runtime.write_json(root / '.context/tree.json', {'nodes': {}, 'topology_hash': 'a' * 64})
    payload = cli.pack(root, task='Inspect only the public interface')
    assert runtime.estimated_tokens(payload) <= 220
    assert payload['files']


def test_v6_schema_accepts_unknown_measurements(tmp_path):
    import jsonschema
    runtime.publish_layer(tmp_path, 'l2', {'present': True, 'state': 'unknown', 'security_gate': None})
    schema = runtime.read_json(REPO.parent / 'iDirectory/schemas/icontext_bus.schema.json')
    jsonschema.validate(runtime.read_json(tmp_path / '.context/icontext_bus.json'), schema)


def test_compiled_orientation_stays_read_only_and_honors_new_pruning(tmp_path, monkeypatch):
    import fwengine
    root = project(tmp_path)
    inv, _ = runtime.inventory(root, persist=True)
    fwengine._compile_context_packs(root, inv)
    before = snapshot(root)
    def no_rebuild(*args, **kwargs):
        raise AssertionError('Warm query rebuilt orientation')
    monkeypatch.setattr(fwengine, '_build_context_pack_live', no_rebuild)
    value = fwengine.build_context_pack(root, 'src')
    assert value['state'] == 'recorded' and value['files']
    assert snapshot(root) == before
    code = f"import sys;sys.path.insert(0,{str(RUNTIME)!r});sys.modules['fwengine']=None;from icontext_cli import pack;from pathlib import Path;assert pack(Path({str(root)!r}),'src')['state']=='recorded'"
    child = subprocess.run([sys.executable, '-B', '-c', code], capture_output=True)
    assert child.returncode == 0, child.stderr
    child = subprocess.run([sys.executable, '-B', str(REPO / 'FWengine.py'), 'context', '--pack', 'src', '--tier', '1a'], cwd=root, capture_output=True)
    assert child.returncode == 0, child.stderr
    assert json.loads(child.stdout.decode('utf-8'))['state'] == 'recorded'
    (root / 'src/.context.yaml').write_text('crawl: false\n')
    value = fwengine.build_context_pack(root, 'src')
    assert value['crawl'] is False and value['files'] == []


def test_windows_json_contract_is_utf8(tmp_path):
    root = project(tmp_path)
    (root / 'src/.context.yaml').write_text('instructions: "Operación quirúrgica"\n', encoding='utf-8')
    result = subprocess.run([sys.executable, '-B', str(REPO / 'icontext.py'), 'pack', '--target', str(root / 'src'), '--json'], capture_output=True)
    assert result.returncode == 0, result.stderr
    assert 'Operación' in json.loads(result.stdout.decode('utf-8'))['instructions']


def test_hybrid_snapshot_does_not_require_a_master(tmp_path):
    root = project(tmp_path)
    seed(root)
    (root / '01_seed/seed-demo-master.md').rename(root / '01_seed/seed-demo.md')
    inv, _ = runtime.inventory(root)
    result = cli.complete(root, 'hybrid', cli.layer_hash(inv, 'hybrid', root))
    assert result['state'] == 'validated'
    assert not cli.outputs(root, 'seed')
    assert runtime.read_json(root / '.context/layers/l1_thinkingseed.json')['artifact_kind'] == 'hybrid'


def test_standalone_metrics_preserves_report_telemetry(tmp_path):
    root = project(tmp_path)
    summary = cli.metrics(root, REPO.parent, profile='agent-skill')
    report = runtime.read_json(root / 'artifacts/plans/metricsthinking/MetricsThinking.json')
    layer = runtime.read_json(root / '.context/layers/l2_metricsthinking.json')
    assert summary['profile'] == 'agent-skill'
    assert layer['fpai_s_spectral'] == report['fpai']['s_spectral']
    assert layer['security_gate'] is not None
    assert layer['inputs_hash'] == runtime.read_json(root / '.context/inventory.json')['inputs_hash']
    assert all(p.is_file() for p in cli.outputs(root, 'metrics'))


def test_installation_diagnosis_detects_damaged_resources(tmp_path):
    skill_installer.install(REPO.parent, ['antigravity', 'codex'], tmp_path)
    script = tmp_path / '.agents/skills/seed/scripts/run.py'
    script.write_text('# damaged resource\n')
    result = skill_installer.inspect_installation(REPO.parent, tmp_path)
    assert not result['installed']['codex']['seed']['matches']
    assert result['installed']['antigravity']['seed']['matches']
    skill_installer.install(REPO.parent, ['codex'], tmp_path)
    assert not skill_installer.inspect_installation(REPO.parent, tmp_path)['errors']


def test_full_sync_propagates_verification_to_metrics(tmp_path, monkeypatch):
    root = project(tmp_path)
    seed(root)
    inv, _ = runtime.inventory(root)
    cli.complete(root, 'seed', cli.layer_hash(inv, 'seed', root))
    observed = []
    monkeypatch.setattr(cli, 'metrics', lambda root, eco, full=False: observed.append(full))
    result, code = cli.sync(root, REPO.parent, full=True)
    assert observed == [True]
    assert code == 3 and result['requests'][0]['layer'] == 'readme'


def test_context_pack_respects_project_budget(tmp_path):
    root = project(tmp_path)
    (root / 'config').mkdir()
    runtime.write_json(root / 'config/context_policy.json',
                       {'profiles': {'tier_1a': {'target_token_budget': 170}}})
    value = cli.pack(root, 'src', task='Review a scoped change')
    assert runtime.estimated_tokens(value) <= 170
    assert value['files']


def test_pack_does_not_mistake_an_internal_kernel_for_the_project_root(tmp_path):
    root = project(tmp_path)
    (root / '.context').mkdir()
    (root / 'src/FWengine.py').write_text('# internal module\n')
    result = subprocess.run([sys.executable, '-B', str(REPO / 'icontext.py'),
                             'pack', 'src', '--target', str(root), '--json'], capture_output=True)
    assert result.returncode == 0, result.stderr
    assert json.loads(result.stdout.decode('utf-8'))['focus'] == 'src'


def test_document_validation_allows_web_urls_and_rejects_local_paths(tmp_path):
    readmes(tmp_path)
    seed(tmp_path)
    master = tmp_path / '01_seed/seed-demo-master.md'
    for path in (tmp_path / 'README.md', tmp_path / 'README_ES.md', master):
        with path.open('a', encoding='utf-8') as stream:
            stream.write('\n[Reference](https://example.com/docs)\n')
    assert not runtime.validate_readmes(tmp_path)
    assert not runtime.validate_seed(master)
    for path in (tmp_path / 'README.md', master):
        with path.open('a', encoding='utf-8') as stream:
            stream.write('\nLocal path: D:/private/project\n')
    assert runtime.validate_readmes(tmp_path)
    assert runtime.validate_seed(master)


def test_readme_validation_allows_absolute_paths_in_terminal_examples(tmp_path):
    readmes(tmp_path)
    for name in ('README.md', 'README_ES.md'):
        path = tmp_path / name
        path.write_text(path.read_text(encoding='utf-8') +
                        '\n```powershell\npython "D:\\Projects\\ContextControl\\icontext.py" status\n```\n',
                        encoding='utf-8')
    assert not runtime.validate_readmes(tmp_path)


def test_audit_runtime_upgrade_invalidates_consumer_metrics(tmp_path, monkeypatch):
    root = project(tmp_path / 'consumer')
    inv, _ = runtime.inventory(root)
    distribution = tmp_path / 'distribution'
    distribution.mkdir()
    monkeypatch.setattr(cli, '__file__', str(distribution / 'icontext_cli.py'))
    runtime.write_json(distribution / 'release_manifest.json', {'files': {'metricsthinking/evaluator.py': 'old'}})
    previous = cli.layer_hash(inv, 'metrics', root)
    seed_hash = cli.layer_hash(inv, 'seed', root)
    runtime.write_json(distribution / 'release_manifest.json', {'files': {'metricsthinking/evaluator.py': 'new'}})
    assert cli.layer_hash(inv, 'metrics', root) != previous
    assert cli.layer_hash(inv, 'seed', root) == seed_hash
