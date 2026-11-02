from pathlib import Path

from metricsthinking.engine import run_audit
from metricsthinking.collector import ProjectCollector
from metricsthinking.incremental import observed_context
import pytest


def snapshot(root):
    return {p.relative_to(root).as_posix(): (p.read_bytes(), p.stat().st_mtime_ns)
            for p in root.rglob('*') if p.is_file()}


def test_incremental_audit_reuses_outputs_without_changing_timestamps(tmp_path):
    (tmp_path / 'main.py').write_text('def first(): return 1\n')
    first, artifacts = run_audit(str(tmp_path), quiet=True, reconcile_plans=False)
    before = snapshot(tmp_path)
    again, same = run_audit(str(tmp_path), quiet=True, reconcile_plans=False)
    assert first == again and artifacts == same
    assert snapshot(tmp_path) == before
    (tmp_path / 'main.py').write_text('def other(): return 2\n')
    changed, _ = run_audit(str(tmp_path), quiet=True, reconcile_plans=False)
    assert snapshot(tmp_path) != before


def test_collector_is_read_only_and_honors_ancestor_beacons(tmp_path):
    hidden = tmp_path / 'internal/child'
    hidden.mkdir(parents=True)
    (hidden.parent / '.context.yaml').write_text('crawl: false\n')
    (hidden / 'secret.py').write_text('secret = 1\n')
    (tmp_path / 'main.py').write_text('def alive(): return 1\n')
    before = snapshot(tmp_path)
    evidence = ProjectCollector(str(tmp_path)).collect()
    assert 'main.py' in evidence.rel_files
    assert all('secret.py' not in f for f in evidence.rel_files)
    assert snapshot(tmp_path) == before


def test_duplicate_estimate_uses_actual_duplicate_content(tmp_path):
    (tmp_path / 'a.py').write_text('def one(): return 1\n')
    (tmp_path / 'b.py').write_text('def two(): return 2\n')
    unique = observed_context(ProjectCollector(str(tmp_path)).collect())
    assert unique['duplicate'] == 0
    (tmp_path / 'b.py').write_bytes((tmp_path / 'a.py').read_bytes())
    duplicate = observed_context(ProjectCollector(str(tmp_path)).collect())
    assert duplicate['duplicate'] > 0
    assert duplicate['distortion_state'] == 'not_measured'


def test_invalid_audit_target_is_not_created(tmp_path):
    missing = tmp_path / 'missing'
    with pytest.raises(FileNotFoundError):
        run_audit(str(missing), quiet=True)
    assert not missing.exists()
