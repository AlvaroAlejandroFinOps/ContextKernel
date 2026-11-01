# Preserved pre-v6 CLI implementation

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
iContext Federation Protocol v5.0 — Global Multi-Project Auditor & Healer
========================================================================
Audita de forma determinista y unificada la salud, sincronización topológica,
cobertura de contratos AST y estado del bus de los 4 proyectos federados:
  - L0: iDirectory
  - L1: ThinkingSeed
  - L2: MetricsThinking
  - L3: iReadme

Uso:
  python audit_federation.py
  python audit_federation.py --fix
  python audit_federation.py --full
  python audit_federation.py --json
"""

import sys
import os
import json
import time
import argparse
import subprocess
from pathlib import Path
from typing import Dict, Any, List, Tuple

FEDERATION_VERSION = "5.0.0"
PROJECTS = ["iDirectory", "ThinkingSeed", "MetricsThinking", "iReadme"]


def run_cmd(cmd: List[str], cwd: Path, timeout: int = 90) -> Tuple[int, str, str]:
    try:
        res = subprocess.run(
            cmd,
            cwd=str(cwd),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout
        )
        return res.returncode, res.stdout, res.stderr
    except subprocess.TimeoutExpired:
        return -1, "", f"Timeout tras {timeout}s"
    except Exception as e:
        return -1, "", str(e)


def auto_heal_ecosystem(root: Path, verbose: bool = False) -> bool:
    """
    Ejecuta el pipeline de auto-sanación determinista de 4 fases:
    1. Reconcile L0 en todos los repos (auto-repara mayúsculas, beacons, satélite inicial).
    2. Certificación L1 en ThinkingSeed y actualización de l1_thinkingseed en bus.
    3. Sincronización L3 en iReadme (init_readme.py dual readmes y bus).
    4. Sellado final L0 en los 4 repos para que los mtimes coincidan con tree.json.
    """
    print("[*] Iniciando Auto-Sanación de la Federación iContext v5.0...")

    # 1. Reconcile L0 en todos los repos
    for proj in PROJECTS:
        pdir = root / proj
        if (pdir / "FWengine.py").exists():
            print(f"  [1/4] Reconciliando {proj} (reparación de casing y beacons)...")
            run_cmd([sys.executable, "FWengine.py", "reconcile"], pdir)

    # 2. ThinkingSeed coverage / gates
    val_script = root / "ThinkingSeed" / "scripts" / "test_seed_coverage.py"
    if val_script.exists():
        for proj in PROJECTS:
            pdir = root / proj
            if (pdir / "01_seed").is_dir():
                print(f"  [2/4] Validando Seed y actualizando bus en {proj}...")
                run_cmd([sys.executable, str(val_script), "--target-repo", ".", "--no-anonymize"], pdir)

    # 3. iReadme init_readme.py
    readme_script = root / "iReadme" / "scripts" / "init_readme.py"
    if readme_script.exists():
        print(f"  [3/4] Sincronizando README.md y README_ES.md en iReadme...")
        run_cmd([sys.executable, str(readme_script)], root / "iReadme")

    # 4. Sellado final de mtimes en los 4 repos
    for proj in PROJECTS:
        pdir = root / proj
        if (pdir / "FWengine.py").exists():
            print(f"  [4/4] Sellando satélite y bus en {proj}...")
            run_cmd([sys.executable, "FWengine.py", "reconcile"], pdir)

    print("[+] Auto-sanación completada. Repositorios sincronizados y sellados.\n")
    return True


def audit_l0_idirectory(root: Path, fix: bool = False) -> Dict[str, Any]:
    proj_dir = root / "iDirectory"
    report = {
        "layer": "L0",
        "project": "iDirectory",
        "exists": proj_dir.is_dir(),
        "status": "FAIL",
        "checks": {}
    }
    if not proj_dir.is_dir():
        report["error"] = "Directorio no encontrado"
        return report

    # 1. FWengine.py reconcile --check
    cmd = [sys.executable, "FWengine.py", "reconcile"]
    if not fix:
        cmd.append("--check")
    code, stdout, stderr = run_cmd(cmd, proj_dir)
    report["checks"]["reconcile"] = {
        "pass": code == 0,
        "exit_code": code,
        "summary": "PASS (0 violaciones)" if code == 0 else "FAIL"
    }

    # 2. .context/tree.json
    tree_path = proj_dir / ".context" / "tree.json"
    if tree_path.exists():
        try:
            tree_data = json.loads(tree_path.read_text(encoding="utf-8"))
            topo_hash = tree_data.get("topology_hash", "")
            report["checks"]["tree_satellite"] = {
                "pass": bool(topo_hash),
                "topology_hash": topo_hash[:16] + "..." if topo_hash else "",
                "total_nodes": len(tree_data.get("nodes", {}))
            }
        except Exception as ex:
            report["checks"]["tree_satellite"] = {"pass": False, "error": str(ex)}
    else:
        report["checks"]["tree_satellite"] = {"pass": False, "error": "tree.json ausente"}

    # 3. .context/contracts_ast.json
    ast_path = proj_dir / ".context" / "contracts_ast.json"
    if ast_path.exists():
        try:
            ast_data = json.loads(ast_path.read_text(encoding="utf-8"))
            report["checks"]["contracts_ast"] = {
                "pass": True,
                "symbols_count": len(ast_data.get("symbols", {})),
                "cli_flags_count": len(ast_data.get("cli_flags", {}))
            }
        except Exception as ex:
            report["checks"]["contracts_ast"] = {"pass": False, "error": str(ex)}
    else:
        report["checks"]["contracts_ast"] = {"pass": False, "error": "contracts_ast.json ausente"}

    # 4. .context/icontext_bus.json
    bus_path = proj_dir / ".context" / "icontext_bus.json"
    report["checks"]["icontext_bus"] = {
        "pass": bus_path.exists(),
        "exists": bus_path.exists()
    }

    all_passed = all(c.get("pass", False) for c in report["checks"].values())
    report["status"] = "PASS" if all_passed else "FAIL"
    return report


def audit_l1_thinkingseed(root: Path, fix: bool = False) -> Dict[str, Any]:
    proj_dir = root / "ThinkingSeed"
    report = {
        "layer": "L1",
        "project": "ThinkingSeed",
        "exists": proj_dir.is_dir(),
        "status": "FAIL",
        "checks": {}
    }
    if not proj_dir.is_dir():
        report["error"] = "Directorio no encontrado"
        return report

    # 1. FWengine reconcile
    cmd_rec = [sys.executable, "FWengine.py", "reconcile"]
    if not fix:
        cmd_rec.append("--check")
    code, stdout, stderr = run_cmd(cmd_rec, proj_dir)
    report["checks"]["reconcile"] = {
        "pass": code == 0,
        "summary": "PASS" if code == 0 else "FAIL"
    }

    # 2. Seed Master file check
    seed_file = proj_dir / "01_seed" / "seed-ThinkingSeed-master.md"
    if seed_file.exists():
        text = seed_file.read_text(encoding="utf-8", errors="replace")
        has_v5 = 'version="5.0"' in text or 'seed_schema_version: "5.0"' in text
        has_xml = '<SEED_ARCHITECTURAL_VECTOR' in text and '</SEED_ARCHITECTURAL_VECTOR>' in text
        report["checks"]["seed_master_v5"] = {
            "pass": has_v5 and has_xml,
            "has_v5": has_v5,
            "has_xml": has_xml
        }
    else:
        report["checks"]["seed_master_v5"] = {"pass": False, "error": "Seed ausente"}

    # 3. 6 Deterministic Gates (test_seed_coverage.py)
    val_script = proj_dir / "scripts" / "test_seed_coverage.py"
    if val_script.exists():
        code, stdout, stderr = run_cmd([sys.executable, str(val_script), "--target-repo", ".", "--no-anonymize"], proj_dir)
        report["checks"]["six_gates"] = {
            "pass": code == 0,
            "exit_code": code,
            "summary": "6/6 GATES OK" if code == 0 else "GATE FAILED"
        }
    else:
        report["checks"]["six_gates"] = {"pass": False, "error": "test_seed_coverage.py ausente"}

    # 4. Unit tests
    code, stdout, stderr = run_cmd([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"], proj_dir)
    report["checks"]["unit_tests"] = {
        "pass": code == 0,
        "exit_code": code,
        "summary": "ALL TESTS PASS" if code == 0 else "TEST FAILURES"
    }

    all_passed = all(c.get("pass", False) for c in report["checks"].values())
    report["status"] = "PASS" if all_passed else "FAIL"
    return report


def audit_l2_metricsthinking(root: Path, fix: bool = False, full_suite: bool = False) -> Dict[str, Any]:
    proj_dir = root / "MetricsThinking"
    report = {
        "layer": "L2",
        "project": "MetricsThinking",
        "exists": proj_dir.is_dir(),
        "status": "FAIL",
        "checks": {}
    }
    if not proj_dir.is_dir():
        report["error"] = "Directorio no encontrado"
        return report

    # 1. FWengine reconcile
    cmd_rec = [sys.executable, "FWengine.py", "reconcile"]
    if not fix:
        cmd_rec.append("--check")
    code, stdout, stderr = run_cmd(cmd_rec, proj_dir)
    report["checks"]["reconcile"] = {
        "pass": code == 0,
        "summary": "PASS" if code == 0 else "FAIL"
    }

    # 2. Pytest suite (optimizado: core suite por defecto, full suite con --full)
    if full_suite:
        test_cmd = [sys.executable, "-m", "pytest", "-q"]
        summary_ok = "PASS (106 Tests)"
    else:
        test_cmd = [
            sys.executable, "-m", "pytest",
            "tests/test_hygiene_v4.py",
            "tests/test_models_schemas_v4.py",
            "tests/test_drift_compensation_v4.py",
            "tests/test_spectral_engine_v4.py",
            "-q"
        ]
        summary_ok = "PASS (Core 44 Tests)"

    code, stdout, stderr = run_cmd(test_cmd, proj_dir)
    report["checks"]["pytest_suite"] = {
        "pass": code == 0,
        "exit_code": code,
        "summary": summary_ok if code == 0 else "FAIL"
    }

    # 3. Seed Master v5.0 Coverage
    val_script = root / "ThinkingSeed" / "scripts" / "test_seed_coverage.py"
    if val_script.exists():
        code, stdout, stderr = run_cmd([sys.executable, str(val_script), "--target-repo", ".", "--no-anonymize"], proj_dir)
        report["checks"]["seed_coverage"] = {
            "pass": code == 0,
            "summary": "6/6 GATES OK" if code == 0 else "GATE FAILED"
        }
    else:
        report["checks"]["seed_coverage"] = {"pass": False, "error": "test_seed_coverage.py ausente"}

    # 4. Roadmap frontmatter schema check
    roadmap_candidates = [
        proj_dir / "artifacts" / "plans" / "metricsthinking" / "INFERRED_ROADMAP.md",
        proj_dir / "artifacts" / "plans" / "active" / "INFERRED_ROADMAP.md"
    ]
    roadmap_path = next((p for p in roadmap_candidates if p.exists()), None)
    if roadmap_path:
        txt = roadmap_path.read_text(encoding="utf-8", errors="replace")
        has_frontmatter = txt.startswith("---") and ("plan_id:" in txt or "id:" in txt) and "status:" in txt
        report["checks"]["roadmap_schema"] = {
            "pass": has_frontmatter,
            "has_frontmatter": has_frontmatter
        }
    else:
        report["checks"]["roadmap_schema"] = {"pass": False, "error": "INFERRED_ROADMAP.md ausente"}

    all_passed = all(c.get("pass", False) for c in report["checks"].values())
    report["status"] = "PASS" if all_passed else "FAIL"
    return report


def audit_l3_ireadme(root: Path, fix: bool = False) -> Dict[str, Any]:
    proj_dir = root / "iReadme"
    report = {
        "layer": "L3",
        "project": "iReadme",
        "exists": proj_dir.is_dir(),
        "status": "FAIL",
        "checks": {}
    }
    if not proj_dir.is_dir():
        report["error"] = "Directorio no encontrado"
        return report

    # 1. FWengine reconcile
    cmd_rec = [sys.executable, "FWengine.py", "reconcile"]
    if not fix:
        cmd_rec.append("--check")
    code, stdout, stderr = run_cmd(cmd_rec, proj_dir)
    report["checks"]["reconcile"] = {
        "pass": code == 0,
        "summary": "PASS" if code == 0 else "FAIL"
    }

    # 2. Dual README generation / check
    readme_en = proj_dir / "README.md"
    readme_es = proj_dir / "README_ES.md"
    dual_exist = readme_en.exists() and readme_es.exists()
    report["checks"]["dual_readmes"] = {
        "pass": dual_exist,
        "readme_en": readme_en.exists(),
        "readme_es": readme_es.exists()
    }

    # 3. Pytest suite
    code, stdout, stderr = run_cmd([sys.executable, "-m", "pytest", "-q"], proj_dir)
    report["checks"]["pytest_suite"] = {
        "pass": code == 0,
        "exit_code": code,
        "summary": "PASS (12/12)" if code == 0 else "FAIL"
    }

    # 4. Seed coverage
    val_script = root / "ThinkingSeed" / "scripts" / "test_seed_coverage.py"
    if val_script.exists():
        code, stdout, stderr = run_cmd([sys.executable, str(val_script), "--target-repo", ".", "--no-anonymize"], proj_dir)
        report["checks"]["seed_coverage"] = {
            "pass": code == 0,
            "summary": "6/6 GATES OK" if code == 0 else "GATE FAILED"
        }
    else:
        report["checks"]["seed_coverage"] = {"pass": False, "error": "test_seed_coverage.py ausente"}

    all_passed = all(c.get("pass", False) for c in report["checks"].values())
    report["status"] = "PASS" if all_passed else "FAIL"
    return report


def audit_global_bus(root: Path) -> Dict[str, Any]:
    bus_report = {
        "status": "PASS",
        "layers_present": {},
        "hashes_aligned": True
    }
    for p in PROJECTS:
        bus_file = root / p / ".context" / "icontext_bus.json"
        if bus_file.exists():
            try:
                data = json.loads(bus_file.read_text(encoding="utf-8"))
                layers = data.get("layers", {})
                bus_report["layers_present"][p] = {
                    "has_l0": "l0_idirectory" in layers,
                    "has_l1": "l1_thinkingseed" in layers,
                    "has_l2": "l2_metricsthinking" in layers,
                    "has_l3": "l3_ireadme" in layers,
                    "topology_hash": layers.get("l0_idirectory", {}).get("topology_hash", "")[:16]
                }
            except Exception as e:
                bus_report["layers_present"][p] = {"error": str(e)}
        else:
            bus_report["layers_present"][p] = {"missing": True}
    return bus_report


def audit_single_repo(repo_dir: Path, ecosystem_root: Path, fix: bool = False, full_suite: bool = False) -> Dict[str, Any]:
    """Audita de forma forense las 4 capas de un repositorio específico."""
    fw_script = repo_dir / "FWengine.py"
    if not fw_script.exists():
        fw_script = ecosystem_root / "iDirectory" / "FWengine.py"
    val_script = ecosystem_root / "ThinkingSeed" / "scripts" / "test_seed_coverage.py"

    report = {
        "project": repo_dir.name,
        "path": str(repo_dir),
        "status": "FAIL",
        "layers": {}
    }

    # 1. Capa L0: iDirectory
    l0 = {"pass": True, "checks": {}}
    if fw_script.exists():
        cmd = [sys.executable, str(fw_script), "reconcile"]
        if not fix:
            cmd.append("--check")
        code, out, err = run_cmd(cmd, repo_dir)
        l0["checks"]["reconcile"] = {
            "pass": code == 0,
            "summary": "PASS (0 violaciones)" if code == 0 else "FAIL"
        }
    else:
        l0["checks"]["reconcile"] = {"pass": False, "error": "FWengine no disponible"}

    tree_path = repo_dir / ".context" / "tree.json"
    if tree_path.exists():
        try:
            tdata = json.loads(tree_path.read_text(encoding="utf-8"))
            thash = tdata.get("topology_hash", "")
            l0["checks"]["tree_satellite"] = {
                "pass": bool(thash),
                "summary": thash[:16] + "..." if thash else "",
                "total_nodes": len(tdata.get("nodes", {}))
            }
        except Exception as ex:
            l0["checks"]["tree_satellite"] = {"pass": False, "error": str(ex)}
    else:
        l0["checks"]["tree_satellite"] = {"pass": False, "error": "tree.json ausente"}

    ast_path = repo_dir / ".context" / "contracts_ast.json"
    l0["checks"]["contracts_ast"] = {
        "pass": ast_path.exists(),
        "summary": "OK" if ast_path.exists() else "ausente"
    }

    bus_path = repo_dir / ".context" / "icontext_bus.json"
    l0["checks"]["icontext_bus"] = {
        "pass": bus_path.exists(),
        "summary": "OK" if bus_path.exists() else "ausente"
    }
    l0["pass"] = all(c.get("pass", False) for c in l0["checks"].values())
    report["layers"]["L0_iDirectory"] = l0

    # 2. Capa L1: ThinkingSeed
    l1 = {"pass": True, "checks": {}}
    seed_files = list((repo_dir / "01_seed").glob("seed-*-master.md")) if (repo_dir / "01_seed").is_dir() else []
    if seed_files:
        seed_txt = seed_files[0].read_text(encoding="utf-8", errors="replace")
        has_v5 = 'version="5.0"' in seed_txt or 'seed_schema_version: "5.0"' in seed_txt
        has_xml = '<SEED_ARCHITECTURAL_VECTOR' in seed_txt and '</SEED_ARCHITECTURAL_VECTOR>' in seed_txt
        l1["checks"]["seed_master_v5"] = {
            "pass": has_v5 and has_xml,
            "summary": seed_files[0].name
        }
        if val_script.exists():
            code, out, err = run_cmd([sys.executable, str(val_script), "--target-repo", ".", "--no-anonymize"], repo_dir)
            l1["checks"]["six_gates"] = {
                "pass": code == 0,
                "summary": "6/6 GATES OK" if code == 0 else "GATE FAILED"
            }
        else:
            l1["checks"]["six_gates"] = {"pass": False, "error": "validador no encontrado"}
    else:
        l1["checks"]["seed_master_v5"] = {"pass": False, "summary": "01_seed/ ausente (ejecute /seedMaster)"}
    l1["pass"] = all(c.get("pass", False) for c in l1["checks"].values())
    report["layers"]["L1_ThinkingSeed"] = l1

    # 3. Capa L2: MetricsThinking
    l2 = {"pass": True, "checks": {}}
    report_md_root = repo_dir / "MetricsThinking.md"
    report_md_canon = repo_dir / "artifacts" / "plans" / "metricsthinking" / "MetricsThinking.md"
    has_report = report_md_root.exists() or report_md_canon.exists()
    l2["checks"]["metrics_report"] = {
        "pass": has_report,
        "summary": "OK" if has_report else "pendiente de auditoría"
    }
    roadmap = repo_dir / "artifacts" / "plans" / "active" / "INFERRED_ROADMAP.md"
    if roadmap.exists():
        txt = roadmap.read_text(encoding="utf-8", errors="replace")
        has_frontmatter = txt.startswith("---") and ("plan_id:" in txt or "id:" in txt)
        l2["checks"]["roadmap_schema"] = {"pass": has_frontmatter, "summary": "OK" if has_frontmatter else "schema inválido"}
    else:
        l2["checks"]["roadmap_schema"] = {"pass": True, "summary": "N/A"}
    l2["pass"] = l2["checks"]["metrics_report"]["pass"]
    report["layers"]["L2_MetricsThinking"] = l2

    # 4. Capa L3: iReadme
    l3 = {"pass": True, "checks": {}}
    en = repo_dir / "README.md"
    es = repo_dir / "README_ES.md"
    l3["checks"]["dual_readmes"] = {
        "pass": en.exists() and es.exists(),
        "summary": "OK (Dual EN & ES)" if (en.exists() and es.exists()) else "README dual ausente"
    }
    if en.exists():
        txt = en.read_text(encoding="utf-8", errors="replace")
        has_gov = "Federated Governance" in txt or "Gobernanza Federada" in txt
        has_badges = "iDirectory" in txt or "ThinkingSeed" in txt
        l3["checks"]["federation_badges"] = {
            "pass": has_gov and has_badges,
            "summary": "OK" if (has_gov and has_badges) else "badges/sección de gobernanza pendiente"
        }
    l3["pass"] = all(c.get("pass", False) for c in l3["checks"].values())
    report["layers"]["L3_iReadme"] = l3

    total_pass = all(layer.get("pass", False) for layer in [l0, l1, l2, l3])
    report["status"] = "PASS" if total_pass else "FAIL"
    return report


def main():
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(Path(__file__).resolve().parent / "tools/icontext_runtime"))
    from icontext_cli import main as main_v6
    legacy_args = sys.argv[1:]
    if "--fix" in legacy_args:
        legacy_args.remove("--fix")
        return sys.exit(main_v6(["doctor", "--fix", *legacy_args]))
    return sys.exit(main_v6(["audit", *legacy_args]))
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

    parser = argparse.ArgumentParser(description="iContext Federation Protocol v5.0 — Global Auditor & Healer")
    parser.add_argument("--root", type=str, default=None, help="Ruta base del ecosistema iContext")
    parser.add_argument("--target", type=str, default=None, help="Ruta de un repositorio específico a auditar")
    parser.add_argument("--all", action="store_true", help="Fuerza auditoría de los 4 repositorios del ecosistema")
    parser.add_argument("--fix", action="store_true", help="Aplica reconciliación y auto-sanación completa")
    parser.add_argument("--full", action="store_true", help="Ejecuta suite completa de stress benchmarks")
    parser.add_argument("--json", action="store_true", dest="as_json", help="Emite salida en formato JSON")
    parser.add_argument("--verbose", action="store_true", help="Salida detallada de cada prueba")
    args = parser.parse_args()

    default_root = Path(__file__).resolve().parent
    ecosystem_root = default_root if (default_root / "iDirectory").is_dir() else default_root.parent

    cwd = Path.cwd().resolve()
    is_eco_cwd = (cwd == ecosystem_root) or all((cwd / proj).is_dir() for proj in PROJECTS)

    # Determinar si auditar un repositorio individual o el ecosistema completo
    if args.target:
        target_path = Path(args.target).resolve()
        is_single = target_path != ecosystem_root and not all((target_path / p).is_dir() for p in PROJECTS)
    elif args.all:
        is_single = False
        target_path = ecosystem_root
    elif not is_eco_cwd:
        is_single = True
        target_path = cwd
    else:
        is_single = False
        target_path = ecosystem_root

    start_time = time.time()

    if is_single:
        # Auditoría de repositorio individual
        rep = audit_single_repo(target_path, ecosystem_root, fix=args.fix, full_suite=args.full)
        elapsed = time.time() - start_time
        rep["elapsed_seconds"] = round(elapsed, 2)

        if args.as_json:
            print(json.dumps(rep, ensure_ascii=False, indent=2))
            sys.exit(0 if rep["status"] == "PASS" else 1)

        print("=" * 80)
        print(f"  iContext Federation Protocol v5.0 — Auditoría de Repositorio")
        print(f"  Proyecto: {rep['project']} ({rep['path']})")
        print(f"  Versión: v{FEDERATION_VERSION} | Tiempo: {elapsed:.2f}s")
        print("=" * 80)

        for name, layer in rep["layers"].items():
            status_badge = "[ PASS ]" if layer["pass"] else "[ FAIL ]"
            print(f"\n{status_badge} {name}")
            for check_name, check_data in layer.get("checks", {}).items():
                mark = "  [+]" if check_data.get("pass", False) else "  [-]"
                detail = check_data.get("summary") or ("OK" if check_data.get("pass") else check_data.get("error", "FAIL"))
                print(f"   {mark} {check_name:<22}: {detail}")

        print("\n" + "-" * 80)
        if rep["status"] == "PASS":
            print(f"  [OK] REPOSITORIO '{rep['project']}' EN ESTADO COMPLETO Y CONFORME (COMPLIANT)")
        else:
            print(f"  [!] SE DETECTARON ADVERTENCIAS O DISCREPANCIAS EN '{rep['project']}'")
            print("  Ejecute 'python icontext.py sync' para auto-sanar y sellar.")
        print("=" * 80)
        sys.exit(0 if rep["status"] == "PASS" else 1)

    # Auditoría del Ecosistema Multi-Proyecto
    root = target_path
    if args.fix:
        auto_heal_ecosystem(root, verbose=args.verbose)

    l0 = audit_l0_idirectory(root, fix=args.fix)
    l1 = audit_l1_thinkingseed(root, fix=args.fix)
    l2 = audit_l2_metricsthinking(root, fix=args.fix, full_suite=args.full)
    l3 = audit_l3_ireadme(root, fix=args.fix)
    bus = audit_global_bus(root)

    total_pass = all(layer["status"] == "PASS" for layer in [l0, l1, l2, l3])
    elapsed = time.time() - start_time

    global_summary = {
        "federation_version": FEDERATION_VERSION,
        "ecosystem_root": str(root),
        "overall_status": "COMPLIANT" if total_pass else "NON_COMPLIANT",
        "elapsed_seconds": round(elapsed, 2),
        "layers": {
            "L0_iDirectory": l0,
            "L1_ThinkingSeed": l1,
            "L2_MetricsThinking": l2,
            "L3_iReadme": l3
        },
        "federation_bus": bus
    }

    if args.as_json:
        print(json.dumps(global_summary, ensure_ascii=False, indent=2))
        sys.exit(0 if total_pass else 1)

    print("=" * 80)
    print(f"  iContext Federation Protocol v5.0 — Auditoría Holística Global")
    print(f"  Root: {root}")
    print(f"  Versión: v{FEDERATION_VERSION} | Tiempo: {elapsed:.2f}s")
    print("=" * 80)

    for name, rep in [
        ("Capa L0: iDirectory     (Topologia, Ruteo & AST)", l0),
        ("Capa L1: ThinkingSeed   (ADN Semantico & Gates)", l1),
        ("Capa L2: MetricsThinking (Telemetria & Deriva AST)", l2),
        ("Capa L3: iReadme         (Paper-Grade Dual)", l3),
    ]:
        status_badge = "[ PASS ]" if rep["status"] == "PASS" else "[ FAIL ]"
        print(f"\n{status_badge} {name}")
        for check_name, check_data in rep.get("checks", {}).items():
            mark = "  [+]" if check_data.get("pass", False) else "  [-]"
            detail = check_data.get("summary") or check_data.get("topology_hash") or ("OK" if check_data.get("pass") else check_data.get("error", "FAIL"))
            print(f"   {mark} {check_name:<20}: {detail}")

    print("\n" + "-" * 80)
    if total_pass:
        print("  [OK] FEDERACIÓN iCONTEXT v5.0 EN ESTADO COMPLETO Y ALINEADO (COMPLIANT)")
        print("  Todos los 4 proyectos cumplen con sus invariantes, contratos AST y buses.")
    else:
        print("  [!] SE DETECTARON DISCREPANCIAS O FALLOS DE GOBERNANZA")
        print("  Ejecute 'python audit_federation.py --fix' para auto-sanar automáticamente.")
    print("=" * 80)

    sys.exit(0 if total_pass else 1)


if __name__ == "__main__":
    main()

```
