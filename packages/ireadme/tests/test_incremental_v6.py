import importlib.util
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from ireadme.generator import generate_universal_readmes


def docs(root):
    for name in ('README.md', 'README_ES.md'):
        (root / name).write_text('[English](README.md) | [Español](README_ES.md)\n' +
                                 '\n'.join(f'## {i}. Section\nUnique project narrative {i}.' for i in range(1, 9)), encoding='utf-8')


def test_preserves_authored_sections_and_never_rewrites_golden_implicitly(tmp_path):
    docs(tmp_path)
    golden = tmp_path / 'tests/golden'
    golden.mkdir(parents=True)
    (golden / 'README_golden.md').write_text('accepted reference')
    result = generate_universal_readmes(tmp_path)
    assert 'Unique project narrative 4.' in result[0]
    assert 'Not measured / No medido' in result[0]
    assert '18.4 MB' not in result[0] and '< 85 ms' not in result[0]
    assert (golden / 'README_golden.md').read_text() == 'accepted reference'
    before = {p: (p.read_bytes(), p.stat().st_mtime_ns) for p in tmp_path.rglob('*') if p.is_file()}
    assert generate_universal_readmes(tmp_path) == result
    assert {p: (p.read_bytes(), p.stat().st_mtime_ns) for p in tmp_path.rglob('*') if p.is_file()} == before


def test_dry_run_does_not_create_files_or_context(tmp_path):
    generate_universal_readmes(tmp_path, write_to_disk=False)
    assert list(tmp_path.iterdir()) == []


def test_explicit_golden_update(tmp_path):
    docs(tmp_path)
    result = generate_universal_readmes(tmp_path, update_golden=True)
    assert (tmp_path / 'tests/golden/README_golden.md').read_text(encoding='utf-8') == result[0]
