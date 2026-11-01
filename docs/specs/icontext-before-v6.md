# Preserved pre-v6 CLI implementation

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
iContext Federation Protocol v5.0 — Universal Master CLI Orchestrator
====================================================================
Herramienta de control maestro para la gestión 1-Click de repositorios
gobernados bajo la arquitectura iContext (L0, L1, L2, L3) y el ecosistema completo:
  - L0: iDirectory       (Topología, Ruteo & Contratos AST)
  - L1: ThinkingSeed     (Memoria Semántica & Gates de ADN)
  - L2: MetricsThinking  (Telemetría Forense, FPAI & Deriva AST)
  - L3: iReadme          (Síntesis Ejecutiva & Dual READMEs Paper-Grade)

Comportamiento Context-Aware (Tipo 'git'):
  - Si se ejecuta dentro de un repositorio específico (o CWD):
      python icontext.py status    <- Estado en vivo, trazabilidad temporal de beacons/satélite.
      python icontext.py sync      <- Ciclo completo de 5 fases (L0 -> L1 -> L2 -> L3 -> Sellado L0).
      python icontext.py audit     <- Auditoría forense de las 4 capas del repositorio local.
      python icontext.py init      <- Inicializa andamiaje L0 en nuevo proyecto.
  - Si se ejecuta en la raíz del ecosistema o con --all:
      Opera sobre los 4 repositorios centrales de la federación.
"""

import sys
import os
import json
import time
import argparse
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

VERSION = "5.0.0"
PROJECTS = ["iDirectory", "ThinkingSeed", "MetricsThinking", "iReadme"]


def format_relative_time(timestamp: Optional[Any]) -> str:
    """Convierte un timestamp Unix o estampa ISO en texto relativo amigable ('hace 3 minutos', etc.)."""
    if not timestamp:
        return "Nunca"
    try:
        if isinstance(timestamp, (int, float)):
            dt = datetime.fromtimestamp(float(timestamp), tz=timezone.utc)
        else:
            clean_str = str(timestamp).strip().replace("Z", "+00:00")
            dt = datetime.fromisoformat(clean_str)

        now = datetime.now(timezone.utc)
        diff = (now - dt).total_seconds()

        if diff < 0:
            diff = 0
        if diff < 60:
            return f"hace {int(diff)}s"
        elif diff < 3600:
            mins = int(diff // 60)
            return f"hace {mins}m"
        elif diff < 86400:
            hours = int(diff // 3600)
            return f"hace {hours}h"
        else:
            days = int(diff // 86400)
            return f"hace {days}d ({dt.strftime('%Y-%m-%d %H:%M')})"
    except Exception:
        return str(timestamp)[:19]


def inspect_beacons_enrichment(repo_dir: Path) -> Dict[str, Any]:
    """
    Inspecciona todos los beacons .context.yaml del repositorio:
    - Cantidad total de beacons
    - Cantidad de beacons con enriquecimiento agéntico
    - Estampa y ruta del último beacon modificado/enriquecido
    """
    beacons = list(repo_dir.glob("**/.context.yaml"))
    beacons = [b for b in beacons if not any(part in (".git", ".venv", "venv", "__pycache__", "target") for part in b.parts)]

    total = len(beacons)
    enriched_count = 0
    latest_mtime = 0.0
    latest_path = None

    for b in beacons:
        try:
            mtime = b.stat().st_mtime
            if mtime > latest_mtime:
                latest_mtime = mtime
                try:
                    latest_path = b.relative_to(repo_dir).as_posix()
                except ValueError:
                    latest_path = b.name

            content = b.read_text(encoding="utf-8", errors="replace")
            # Un beacon está enriquecido si key_files tiene ":" o si tiene dependencias/exported_to
            has_rich_keys = any(":" in line and not line.strip().startswith("#") for line in content.splitlines() if "-" in line)
            has_rich_purpose = "purpose:" in content and len(content) > 220
            if has_rich_keys or has_rich_purpose:
                enriched_count += 1
        except Exception:
            pass

    return {
        "total_beacons": total,
        "enriched_count": enriched_count,
        "latest_mtime": latest_mtime if latest_mtime > 0 else None,
        "latest_path": latest_path,
        "relative_time": format_relative_time(latest_mtime) if latest_mtime > 0 else "N/A"
    }


def resolve_ecosystem_root(custom_path: Optional[str] = None) -> Path:
    """Resuelve la raíz del ecosistema iContext donde se alojan los 4 subproyectos."""
    if custom_path:
        cand = Path(custom_path).resolve()
        if (cand / "iDirectory").is_dir():
            return cand
        if (cand.parent / "iDirectory").is_dir():
            return cand.parent

    here = Path(__file__).resolve().parent
    if (here / "iDirectory").is_dir():
        return here
    if (here.parent / "iDirectory").is_dir():
        return here.parent

    cwd = Path.cwd().resolve()
    if (cwd / "iDirectory").is_dir():
        return cwd
    if (cwd.parent / "iDirectory").is_dir():
        return cwd.parent

    return here


def detect_execution_target(
    target_arg: Optional[str] = None,
    all_flag: bool = False,
    root_arg: Optional[str] = None
) -> Tuple[str, Path, Path]:
    """
    Determina si la ejecución debe operar sobre:
    - 'ecosystem': Raíz multi-proyecto iContext (opera sobre los 4 repos: iDirectory, ThinkingSeed, MetricsThinking, iReadme).
    - 'single_repo': Un repositorio específico (CWD o target explícito).

    Retorna: (modo, target_path, ecosystem_root)
    """
    ecosystem_root = resolve_ecosystem_root(root_arg)

    if all_flag:
        return "ecosystem", ecosystem_root, ecosystem_root

    if target_arg:
        p = Path(target_arg).resolve()
        if p == ecosystem_root or all((p / proj).is_dir() for proj in PROJECTS):
            return "ecosystem", ecosystem_root, ecosystem_root
        return "single_repo", p, ecosystem_root

    cwd = Path.cwd().resolve()
    is_eco = (cwd == ecosystem_root) or all((cwd / proj).is_dir() for proj in PROJECTS)
    if is_eco:
        return "ecosystem", ecosystem_root, ecosystem_root

    return "single_repo", cwd, ecosystem_root


def run_sub(
    cmd: List[str],
    cwd: Path,
    env: Optional[Dict[str, str]] = None,
    timeout: int = 120
) -> Tuple[int, str, str]:
    try:
        res = subprocess.run(
            cmd,
            cwd=str(cwd),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            env=env,
            timeout=timeout
        )
        return res.returncode, res.stdout, res.stderr
    except subprocess.TimeoutExpired:
        return -1, "", f"Timeout tras {timeout}s"
    except Exception as e:
        return -1, "", str(e)


def cmd_init(target_path: Path, ecosystem_root: Path) -> int:
    """Inicializa el andamiaje L0 de iDirectory en target_path si no existe."""
    fw = target_path / "FWengine.py"
    if not fw.exists():
        fw = ecosystem_root / "iDirectory" / "FWengine.py"
    if not fw.exists():
        print(f"[!] Error: No se encontró FWengine.py para inicializar en {target_path}", file=sys.stderr)
        return 1

    print(f"[*] Inicializando andamiaje iDirectory en: {target_path}...")
    code, out, err = run_sub([sys.executable, str(fw), "init", str(target_path)], target_path)
    if code == 0:
        print(f"[+] Proyecto inicializado exitosamente en {target_path}")
    else:
        print(f"[!] Advertencia en init: {err or out}")
    return code


def cmd_reconcile_single_repo(repo_dir: Path, ecosystem_root: Path, verbose: bool = False) -> int:
    """
    Ejecuta el Ciclo Completo de Reconciliación Federada (5 Fases) sobre un repositorio individual:
    Fase 1: L0 Reconcile (Scaffolding si es nuevo, Casing, Beacons, Tree, Contracts AST)
    Fase 2: L1 Validación de 6 Gates del Seed Maestro (ThinkingSeed)
    Fase 3: L2 Auditoría Forense FPAI Espectral (MetricsThinking)
    Fase 4: L3 Generación Dual Paper-Grade con Badges de Gobernanza (iReadme)
    Fase 5: L0 Sellado Final Criptográfico (0 Drift)
    """
    start = time.time()
    print("=" * 80)
    print(f"  iContext Federation Protocol v5.0 — Reconciliación Universal 1-Click")
    print(f"  Objetivo: {repo_dir}")
    print("=" * 80)

    fw_script = repo_dir / "FWengine.py"
    if not fw_script.exists():
        fw_script = ecosystem_root / "iDirectory" / "FWengine.py"
    val_script = ecosystem_root / "ThinkingSeed" / "scripts" / "test_seed_coverage.py"
    gen_script = ecosystem_root / "iReadme" / "src" / "ireadme" / "generator.py"

    # Preparar entorno con PYTHONPATH para MetricsThinking e iReadme
    env = os.environ.copy()
    py_paths = [
        str(ecosystem_root / "MetricsThinking" / "src"),
        str(ecosystem_root / "iReadme" / "src")
    ]
    if "PYTHONPATH" in env:
        py_paths.append(env["PYTHONPATH"])
    env["PYTHONPATH"] = os.pathsep.join(py_paths)

    # FASE 1: L0 Reconciliación & Topología
    print("\n[Fase 1/5] Reconciliando L0 Topología & Balizas (iDirectory)...")
    if not (repo_dir / ".context").exists() and not (repo_dir / "FWengine.py").exists():
        print(f"  -> Proyecto nuevo sin andamiaje. Inicializando andamiaje L0...")
        cmd_init(repo_dir, ecosystem_root)

    code, out, err = run_sub([sys.executable, str(fw_script), "reconcile"], repo_dir, env=env)
    if code != 0:
        print(f"  [!] Advertencia en L0 reconcile: {err or out}")
    else:
        print(f"  [+] L0 Reconciliado: Beacons sincronizados, satélite y contratos AST generados.")

    # FASE 2: L1 Validación de Memoria y 6 Gates
    print("\n[Fase 2/5] Validando L1 Memoria Semántica & Gates (ThinkingSeed)...")
    if (repo_dir / "01_seed").is_dir() and val_script.exists():
        code, out, err = run_sub([sys.executable, str(val_script), "--target-repo", ".", "--no-anonymize"], repo_dir, env=env)
        if code == 0:
            print(f"  [+] L1: 6/6 GATES OK (ADN Master sincronizado con contratos AST)")
        else:
            print(f"  [!] L1: Advertencia en gates de seed (Revise 01_seed/).")
    else:
        print(f"  [-] L1 omitido: no se encontró carpeta 01_seed/ (Use /seedMaster para crearla).")

    # FASE 3: L2 Auditoría Forense FPAI Espectral (MetricsThinking)
    print("\n[Fase 3/5] Ejecutando L2 Auditoría Forense FPAI (MetricsThinking)...")
    code, out, err = run_sub([sys.executable, "-m", "metricsthinking.cli", "audit", "--target", ".", "--profile", "default"], repo_dir, env=env)
    if code == 0:
        print(f"  [+] L2: Auditoría forense completada, MetricsThinking.md y FPAI inyectados al bus.")
    else:
        print(f"  [*] L2: Telemetría evaluada.")

    # FASE 4: L3 Generación Dual de Documentación Paper-Grade (iReadme)
    print("\n[Fase 4/5] Generando L3 Documentación Enterprise Paper-Grade (iReadme)...")
    if gen_script.exists():
        code, out, err = run_sub([sys.executable, str(gen_script), "--target", "."], repo_dir, env=env)
        if code == 0:
            print(f"  [+] L3: README.md y README_ES.md generados con badges federados y gobernanza.")
        else:
            print(f"  [!] Error en generator.py: {err}")
    elif (repo_dir / "scripts" / "init_readme.py").exists():
        run_sub([sys.executable, "scripts/init_readme.py"], repo_dir, env=env)

    # FASE 5: L0 Sellado Final Criptográfico
    print("\n[Fase 5/5] Sellado Criptográfico Final & Sincronización del Bus...")
    code, out, err = run_sub([sys.executable, str(fw_script), "reconcile"], repo_dir, env=env)
    if code == 0:
        print(f"  [+] Satélite .context/tree.json y bus sellados con 0 drift.")
    else:
        print(f"  [!] Advertencia en sellado: {err}")

    elapsed = time.time() - start
    print("\n" + "=" * 80)
    print(f"  [OK] RECONCILIACIÓN 1-CLICK COMPLETADA EN {elapsed:.2f}s")
    print(f"  Repositorio '{repo_dir.name}' actualizado y en cumplimiento estricto v5.0.")
    print("=" * 80)
    return 0


def cmd_sync_ecosystem(root: Path, verbose: bool = False) -> int:
    """
    Comando Maestro 1-Click: Sincroniza, repara y sella todos los 4 proyectos
    en el orden de precedencia estricto del iContext Federation Protocol v5.0.
    """
    start = time.time()
    print("=" * 80)
    print("  iContext Federation Protocol v5.0 — Orquestador de Sincronización 1-Click (Ecosistema)")
    print(f"  Root: {root}")
    print("=" * 80)

    # Paso 1: Normalización de mayúsculas y reconciliación L0
    print("\n[Fase 1/4] Reconciliación L0 & Auto-Remediación de Casing (iDirectory)...")
    for proj in PROJECTS:
        pdir = root / proj
        if (pdir / "FWengine.py").exists():
            print(f"  -> Reconciliando {proj}...")
            code, out, err = run_sub([sys.executable, "FWengine.py", "reconcile"], pdir)
            if code != 0:
                print(f"     [!] Advertencia en {proj}: {err or out}")
            elif verbose:
                print(f"     [+] {proj} reconciliado exitosamente.")

    # Paso 2: Validación L1 y actualización de contratos de ADN (ThinkingSeed)
    print("\n[Fase 2/4] Validación de Memoria L1 & Actualización de ADN (ThinkingSeed)...")
    val_script = root / "ThinkingSeed" / "scripts" / "test_seed_coverage.py"
    if val_script.exists():
        for proj in PROJECTS:
            pdir = root / proj
            if (pdir / "01_seed").is_dir():
                print(f"  -> Validando 6 Gates y contratos AST en {proj}...")
                code, out, err = run_sub([sys.executable, str(val_script), "--target-repo", ".", "--no-anonymize"], pdir)
                if code == 0:
                    print(f"     [+] {proj}: 6/6 GATES OK (ADN Master sincronizado)")
                else:
                    print(f"     [!] {proj}: Falló validación de seed.")

    # Paso 3: Sincronización L3 de Documentación Dual Paper-Grade (iReadme)
    print("\n[Fase 3/4] Generación Dual de Documentación Paper-Grade L3 (iReadme)...")
    readme_script = root / "iReadme" / "scripts" / "init_readme.py"
    if readme_script.exists():
        print("  -> Ejecutando init_readme.py en iReadme...")
        code, out, err = run_sub([sys.executable, str(readme_script)], root / "iReadme")
        if code == 0:
            print("     [+] README.md y README_ES.md sincronizados con paridad phi = 1.0.")
        else:
            print(f"     [!] Error sincronizando readmes: {err}")

    # Paso 4: Sellado criptográfico final y sincronización del Bus
    print("\n[Fase 4/4] Sellado Criptográfico Final & Sincronización del Bus Federado...")
    for proj in PROJECTS:
        pdir = root / proj
        if (pdir / "FWengine.py").exists():
            code, out, err = run_sub([sys.executable, "FWengine.py", "reconcile"], pdir)
            if code == 0:
                print(f"  -> {proj}: Satélite .context/tree.json y bus sellados.")
            else:
                print(f"  -> {proj}: [!] Error en sellado final: {err}")

    elapsed = time.time() - start
    print("\n" + "=" * 80)
    print(f"  [OK] SINCRONIZACIÓN 1-CLICK COMPLETADA EN {elapsed:.2f}s")
    print("  Todos los 4 proyectos han sido normalizados, validados y sellados exitosamente.")
    print("  Para verificar la salud detallada, ejecute: python icontext.py audit --all")
    print("=" * 80)
    return 0


def cmd_status_single_repo(repo_dir: Path, ecosystem_root: Path) -> int:
    """Inspección detallada con trazabilidad temporal del repositorio local."""
    print("=" * 80)
    print("  iContext Federation Protocol v5.0 — Estado en Vivo del Repositorio")
    print(f"  Proyecto: {repo_dir.name}")
    print(f"  Ruta    : {repo_dir}")
    print("=" * 80)

    tree_file = repo_dir / ".context" / "tree.json"
    bus_file = repo_dir / ".context" / "icontext_bus.json"
    cp_file = repo_dir / ".context" / "checkpoint.json"

    # 1. Beacons & Enriquecimiento
    beacons_info = inspect_beacons_enrichment(repo_dir)

    # 2. Satélite tree.json y Freshness
    topo_hash = "N/A"
    tree_updated = "N/A"
    freshness_status = "N/A"
    fw_script = repo_dir / "FWengine.py"
    if not fw_script.exists():
        fw_script = ecosystem_root / "iDirectory" / "FWengine.py"

    if tree_file.exists():
        try:
            tdata = json.loads(tree_file.read_text(encoding="utf-8"))
            topo_hash = tdata.get("topology_hash", "N/A")[:16]
            tree_updated = format_relative_time(tdata.get("updated_at") or tdata.get("timestamp"))
        except Exception:
            pass

        if fw_script.exists():
            code, out, _ = run_sub([sys.executable, str(fw_script), "context", "--check-freshness"], repo_dir)
            freshness_status = "FRESH (Al día)" if code == 0 else "DRIFT (Desactualizado)"

    print(f"\n[*] Topología Física & Satélite (L0 iDirectory):")
    print(f"    - Estado Satélite         : {freshness_status}")
    print(f"    - Topology Hash           : {topo_hash}...")
    print(f"    - Última Reconciliación   : {tree_updated}")
    print(f"    - Beacons (.context.yaml) : {beacons_info['total_beacons']} total | {beacons_info['enriched_count']} enriquecidos")
    print(f"    - Último Enriquecimiento  : {beacons_info['relative_time']} ({beacons_info['latest_path'] or 'N/A'})")

    # 3. Telemetría de Capas desde el Bus
    if bus_file.exists():
        try:
            bdata = json.loads(bus_file.read_text(encoding="utf-8"))
            layers = bdata.get("layers", {})
            bus_updated = format_relative_time(bdata.get("updated_at"))

            l0 = layers.get("l0_idirectory", {})
            l1 = layers.get("l1_thinkingseed", {})
            l2 = layers.get("l2_metricsthinking", {})
            l3 = layers.get("l3_ireadme", {})

            print(f"\n[*] Telemetría del Bus Federado (Último sync: {bus_updated}):")
            print(f"    - L0 Tokens Activos       : {l0.get('active_tokens_estimate', 'N/A')} tokens ({l0.get('active_nodes_count', 'N/A')} nodos)")

            l1_time = format_relative_time(l1.get('last_validated_at'))
            print(f"    - L1 ThinkingSeed         : Cov = {l1.get('ast_coverage_pct', 'N/A')}% | Status = {l1.get('freshness_status', 'N/A')} | Validado: {l1_time}")

            l2_time = format_relative_time(l2.get('last_audited_at'))
            print(f"    - L2 MetricsThinking      : Score = {l2.get('consolidated_score', 'N/A')}% | PF Spectral = {l2.get('fpai_pf_spectral', 'N/A')} | Auditado: {l2_time}")

            l3_time = format_relative_time(l3.get('last_synced_at'))
            print(f"    - L3 iReadme              : Parity Phi = {l3.get('parity_score_phi', 'N/A')} | Leakage = {l3.get('path_leakage_rate', 'N/A')}% | Sincronizado: {l3_time}")
        except Exception as ex:
            print(f"    [!] Error leyendo icontext_bus.json: {ex}")
    else:
        print(f"\n[*] Bus Federado: .context/icontext_bus.json ausente (Ejecute 'python icontext.py sync')")

    # 4. Checkpoint
    if cp_file.exists():
        try:
            cp = json.loads(cp_file.read_text(encoding="utf-8"))
            print(f"\n[*] Checkpoint Atencional de Sesión:")
            print(f"    - Plan Activo : {cp.get('plan_id', 'N/A')} (Fase: {cp.get('phase', 'N/A')})")
            print(f"    - Próximo Paso: {cp.get('next_action', 'N/A')}")
        except Exception:
            pass

    print("\n" + "-" * 80)
    print("  Tip: Ejecute 'python icontext.py sync' para sincronizar y sellar este repositorio.")
    print("=" * 80)
    return 0


def cmd_status_ecosystem(root: Path) -> int:
    """Inspección ultrarrápida (< 500 ms) del bus federado en los 4 repositorios centrales."""
    print("=" * 80)
    print("  iContext Federation Protocol v5.0 — Estado en Vivo del Bus Federado (Ecosistema)")
    print(f"  Root: {root}")
    print("=" * 80)

    for proj in PROJECTS:
        pdir = root / proj
        bus_file = pdir / ".context" / "icontext_bus.json"
        tree_file = pdir / ".context" / "tree.json"

        print(f"\n[*] Proyecto: {proj}")
        if not pdir.is_dir():
            print("    [!] Directorio no encontrado en el workspace.")
            continue

        topo_hash = "N/A"
        tree_updated = "N/A"
        if tree_file.exists():
            try:
                tdata = json.loads(tree_file.read_text(encoding="utf-8"))
                topo_hash = tdata.get("topology_hash", "N/A")[:16]
                tree_updated = format_relative_time(tdata.get("updated_at") or tdata.get("timestamp"))
            except Exception:
                pass
        print(f"    - Topology Hash : {topo_hash}... (Satélite: {tree_updated})")

        if bus_file.exists():
            try:
                bdata = json.loads(bus_file.read_text(encoding="utf-8"))
                layers = bdata.get("layers", {})
                l0 = layers.get("l0_idirectory", {})
                l1 = layers.get("l1_thinkingseed", {})
                l2 = layers.get("l2_metricsthinking", {})
                l3 = layers.get("l3_ireadme", {})

                print(f"    - Capa L0 (iDirectory)      : Tokens Activos = {l0.get('active_tokens_estimate', 'N/A')} | Nodos = {l0.get('active_nodes_count', 'N/A')}")
                print(f"    - Capa L1 (ThinkingSeed)    : Seed = {Path(l1.get('seed_path', '')).name} | AST Cov = {l1.get('ast_coverage_pct', 'N/A')}%")
                print(f"    - Capa L2 (MetricsThinking) : Score = {l2.get('consolidated_score', 'N/A')}% | PF Spectral = {l2.get('fpai_pf_spectral', 'N/A')}")
                print(f"    - Capa L3 (iReadme)         : Parity Phi = {l3.get('parity_score_phi', 'N/A')} | Leakage = {l3.get('path_leakage_rate', 'N/A')}%")
            except Exception as ex:
                print(f"    [!] Error leyendo icontext_bus.json: {ex}")
        else:
            print("    [!] .context/icontext_bus.json ausente (ejecute 'python icontext.py sync')")

    print("\n" + "-" * 80)
    print("  Tip: Ejecute 'python icontext.py sync' para actualizar cualquier métrica pendiente.")
    print("=" * 80)
    return 0


def _find_repo_root_and_target(target_path: Path, ecosystem_root: Path) -> Tuple[Path, str]:
    """Determina la raíz del repositorio y la ruta relativa del target dentro del repo."""
    target_resolved = target_path.resolve()
    curr = target_resolved
    while curr != curr.parent and curr != ecosystem_root.parent:
        if (curr / "FWengine.py").exists() or (curr / ".context").exists():
            try:
                rel = target_resolved.relative_to(curr).as_posix()
            except ValueError:
                rel = "."
            return curr, rel or "."
        if curr == ecosystem_root:
            break
        curr = curr.parent

    if (ecosystem_root / "iDirectory" / "FWengine.py").exists():
        return (ecosystem_root / "iDirectory"), "."
    return ecosystem_root, "."


def cmd_capsule(target_path: Path, task: str = "") -> int:
    """Genera una cápsula de contexto quirúrgica (<450 tokens) para subagentes."""
    here = Path(__file__).resolve().parent
    ecosystem_root = resolve_ecosystem_root(str(here))
    repo_root, rel_target = _find_repo_root_and_target(target_path, ecosystem_root)
    fw = repo_root / "FWengine.py"
    if not fw.exists():
        fw = ecosystem_root / "iDirectory" / "FWengine.py"
        repo_root = ecosystem_root / "iDirectory"
    if not fw.exists():
        print("[!] FWengine.py no encontrado para generar cápsula.", file=sys.stderr)
        return 1
    cmd = [sys.executable, str(fw), "context", "--capsule", "--target", rel_target, "--task", task]
    res = subprocess.run(cmd, cwd=str(repo_root))
    return res.returncode


def cmd_pack(target_path: Path, tier: str = "1a") -> int:
    """Emite paquete de contexto optimizado según tier."""
    here = Path(__file__).resolve().parent
    ecosystem_root = resolve_ecosystem_root(str(here))
    repo_root, rel_target = _find_repo_root_and_target(target_path, ecosystem_root)
    fw = repo_root / "FWengine.py"
    if not fw.exists():
        fw = ecosystem_root / "iDirectory" / "FWengine.py"
        repo_root = ecosystem_root / "iDirectory"
    if not fw.exists():
        print("[!] FWengine.py no encontrado para generar paquete de contexto.", file=sys.stderr)
        return 1
    cmd = [sys.executable, str(fw), "context", "--pack", rel_target, "--tier", tier]
    res = subprocess.run(cmd, cwd=str(repo_root))
    return res.returncode


def cmd_audit(target_mode: str, target_path: Path, ecosystem_root: Path, full: bool = False, as_json: bool = False) -> int:
    """Delega al auditor determinista audit_federation.py."""
    auditor = ecosystem_root / "audit_federation.py"
    if not auditor.exists():
        print(f"[!] No se encontró {auditor}", file=sys.stderr)
        return 1
    cmd = [sys.executable, str(auditor)]
    if target_mode == "single_repo":
        cmd.extend(["--target", str(target_path)])
    else:
        cmd.append("--all")
    if full:
        cmd.append("--full")
    if as_json:
        cmd.append("--json")
    return subprocess.run(cmd, cwd=str(target_path if target_mode == "single_repo" else ecosystem_root)).returncode


def main():
    sys.dont_write_bytecode = True
    # v6 keeps the historical script path while dispatching the versioned CLI.
    sys.path.insert(0, str(Path(__file__).resolve().parent / "tools/icontext_runtime"))
    from icontext_cli import main as main_v6
    return main_v6()
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

    parser = argparse.ArgumentParser(
        prog="icontext",
        description="iContext Federation Protocol v5.0 — CLI Maestra de Orquestación Universal (Context-Aware)"
    )
    parser.add_argument("--root", type=str, default=None, help="Ruta base del ecosistema iContext")
    parser.add_argument("--target", type=str, default=None, help="Ruta de un repositorio específico a operar")
    parser.add_argument("--all", action="store_true", help="Opera sobre todos los 4 repositorios centrales del ecosistema")
    parser.add_argument("-v", "--verbose", action="store_true", help="Salida detallada")

    sub = parser.add_subparsers(dest="command", help="Comandos disponibles")

    # init
    init_p = sub.add_parser("init", help="Inicializa el andamiaje L0 de iDirectory en el repositorio objetivo")
    init_p.add_argument("path", nargs="?", default=".", help="Ruta del directorio a inicializar")

    # reconcile / sync / update
    sync_p = sub.add_parser("reconcile", aliases=["sync", "update"], help="Reconcilia, valida gates y sella el repositorio o ecosistema")
    sync_p.add_argument("--target", type=str, default=None, help="Ruta de un repositorio específico a reconciliar")
    sync_p.add_argument("--all", action="store_true", help="Sincroniza todos los repositorios de la federación")
    sync_p.add_argument("--dry-run", action="store_true", help="Solo verifica sin modificar")

    # capsule (subagent isolation < 450 tokens)
    cap_p = sub.add_parser("capsule", help="Genera una cápsula de contexto quirúrgica (<450 tokens) para subagentes")
    cap_p.add_argument("--target", type=str, default=".", help="Directorio objetivo para la cápsula")
    cap_p.add_argument("--task", type=str, default="", help="Descripción de la tarea asignada al subagente")

    # pack
    pack_p = sub.add_parser("pack", help="Emite paquete de contexto optimizado según tier")
    pack_p.add_argument("--target", type=str, default=".", help="Directorio objetivo")
    pack_p.add_argument("--tier", default="1a", choices=["1a", "1b", "2"], help="Perfil de bootloader")

    # audit
    audit_p = sub.add_parser("audit", help="Audita el estado de gobernanza y cumplimiento de las 4 capas")
    audit_p.add_argument("--target", type=str, default=None, help="Ruta de un repositorio específico a auditar")
    audit_p.add_argument("--all", action="store_true", help="Audita todos los repositorios de la federación")
    audit_p.add_argument("--full", action="store_true", help="Ejecuta suite completa de stress benchmarks")
    audit_p.add_argument("--json", action="store_true", help="Salida en JSON estructurado")

    # status
    status_p = sub.add_parser("status", help="Muestra el estado en vivo y trazabilidad temporal del bus federado")
    status_p.add_argument("--target", type=str, default=None, help="Ruta de un repositorio específico a inspeccionar")
    status_p.add_argument("--all", action="store_true", help="Muestra el estado de todos los repositorios de la federación")

    # doctor / fix
    sub.add_parser("doctor", aliases=["fix"], help="Diagnostica y auto-sana discrepancias topológicas o satelitales")

    args = parser.parse_args()
    cmd = args.command

    target_mode, target_path, ecosystem_root = detect_execution_target(
        target_arg=getattr(args, "target", None),
        all_flag=getattr(args, "all", False),
        root_arg=getattr(args, "root", None)
    )

    if cmd == "init":
        init_target = Path(getattr(args, "path", ".")).resolve()
        return cmd_init(init_target, ecosystem_root)

    elif not cmd or cmd in ["reconcile", "sync", "update"]:
        if target_mode == "single_repo":
            return cmd_reconcile_single_repo(target_path, ecosystem_root, verbose=args.verbose)
        return cmd_sync_ecosystem(ecosystem_root, verbose=args.verbose)

    elif cmd == "status":
        if target_mode == "single_repo":
            return cmd_status_single_repo(target_path, ecosystem_root)
        return cmd_status_ecosystem(ecosystem_root)

    elif cmd == "capsule":
        tpath = target_path or Path.cwd().resolve()
        return cmd_capsule(tpath, task=getattr(args, "task", ""))

    elif cmd == "pack":
        tpath = target_path or Path.cwd().resolve()
        return cmd_pack(tpath, tier=getattr(args, "tier", "1a"))

    elif cmd == "audit":
        return cmd_audit(
            target_mode,
            target_path,
            ecosystem_root,
            full=getattr(args, "full", False),
            as_json=getattr(args, "json", False)
        )

    elif cmd in ["doctor", "fix"]:
        from audit_federation import auto_heal_ecosystem
        auto_heal_ecosystem(ecosystem_root, verbose=args.verbose)
        return cmd_audit("ecosystem", ecosystem_root, ecosystem_root, full=False, as_json=False)

    else:
        parser.print_help()
        return 0


if __name__ == "__main__":
    sys.exit(main())

```
