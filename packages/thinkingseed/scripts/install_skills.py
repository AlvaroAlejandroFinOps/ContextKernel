#!/usr/bin/env python3
"""
ThinkingSeed Universal Skill Installer
=======================================
Instala las skills `/seed` y `/seedMaster` en cualquier entorno de agentes:
- Antigravity / Gemini CLI (Global o Local)
- Claude Code (Global o Local con CLAUDE.md)
- Cursor IDE (.cursorrules)
- Windsurf IDE (.windsurfrules)
- GitHub Copilot (.github/copilot-instructions.md)
- Estándar Agnóstico AGENTS.md

Uso:
    python scripts/install_skills.py                   # Modo interactivo
    python scripts/install_skills.py --global-install  # Instala globalmente para Antigravity y Claude
    python scripts/install_skills.py --target ./ruta   # Inyecta en un proyecto destino
"""

import os
import re
import sys
import shutil
import argparse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SKILLS_SRC_DIR = BASE_DIR / ".agents" / "skills"

TEMPLATE_HYBRID = BASE_DIR / "ThinkingSeed_MasterHybrid.md"
TEMPLATE_MASTER = BASE_DIR / "ThinkingSeed Master.md"


def upsert_segmented_rule_file(src_path: Path, dest_path: Path, tool_key: str = "THINKINGSEED", backup: bool = False) -> bool:
    """
    Inserta o actualiza de forma no destructiva el bloque de reglas de ThinkingSeed v6.0
    en el archivo destino sin sobrescribir reglas preexistentes de iDirectory, MetricsThinking o iReadme.
    """
    content = src_path.read_text(encoding="utf-8", errors="replace").strip()
    start_marker = f"<!-- >>> ICONTEXT-V5:{tool_key}:START >>> -->"
    end_marker = f"<!-- <<< ICONTEXT-V5:{tool_key}:END >>> -->"
    wrapped = f"{start_marker}\n{content}\n{end_marker}"

    if not dest_path.exists():
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        dest_path.write_text(wrapped + "\n", encoding="utf-8")
        return True

    if backup:
        bak_path = dest_path.with_suffix(dest_path.suffix + ".bak")
        shutil.copy2(dest_path, bak_path)

    existing = dest_path.read_text(encoding="utf-8", errors="replace")
    if start_marker in existing and end_marker in existing:
        pattern = re.compile(re.escape(start_marker) + r".*?" + re.escape(end_marker), re.DOTALL)
        updated = pattern.sub(lambda _m: wrapped, existing)
    elif existing.strip() and existing.strip() != content:
        updated = existing.rstrip() + "\n\n" + wrapped + "\n"
    else:
        updated = wrapped + "\n"

    dest_path.write_text(updated, encoding="utf-8")
    return True

def _install_v6(agents, local=None, dry_run=False):
    sys.path.insert(0, str(BASE_DIR / "tools/icontext_runtime"))
    from skill_installer import install
    return install(BASE_DIR.parent, agents, Path.home(), local=local, dry_run=dry_run, only=["seed", "seed-master"])


def get_home_dir() -> Path:
    return Path.home()

def install_antigravity_global() -> bool:
    _install_v6(["antigravity"])
    return True


def install_claude_code_global() -> bool:
    claude_dir = get_home_dir() / ".claude"
    try:
        claude_dir.mkdir(parents=True, exist_ok=True)
        # Copiar CLAUDE.md global o en el home de claude
        claude_md_src = BASE_DIR / "CLAUDE.md"
        if claude_md_src.exists():
            shutil.copy2(claude_md_src, claude_dir / "CLAUDE.md")
            print(f"  [OK] Claude Code Global: Copiado CLAUDE.md en {claude_dir / 'CLAUDE.md'}")
        return True
    except Exception as e:
        print(f"  [ERROR] Al configurar Claude Code Global: {e}")
        return False

def install_codex_global() -> bool:
    _install_v6(["codex"])
    return True


def inject_into_project(target_path: Path, backup: bool = False, check_only: bool = False) -> bool:
    _install_v6(["antigravity", "codex"], local=target_path, dry_run=check_only)
    return True


def main():
    parser = argparse.ArgumentParser(description="Instalador Universal de ThinkingSeed Skills v6.0")
    parser.add_argument("--global-install", action="store_true", help="Instala las skills globalmente en el sistema")
    parser.add_argument("--target", type=str, help="Ruta de un proyecto destino donde inyectar las skills y reglas")
    parser.add_argument("--backup", action="store_true", help="Crea copia de respaldo (.bak) antes de actualizar archivos de reglas")
    parser.add_argument("--check-only", action="store_true", help="Previsualiza los cambios en el repositorio destino sin escribir en disco")

    args = parser.parse_args()

    print("=" * 70)
    print("  Gravity HyperScale Thinking - ThinkingSeed v6.0 Multi-Agent Installer")
    print("=" * 70)

    if args.global_install:
        print("\nInstalando skills en el entorno global del usuario...")
        install_antigravity_global()
        install_codex_global()
        print("\n[OK] Instalacion global completada con exito.")
        return

    if args.target:
        inject_into_project(Path(args.target), backup=args.backup, check_only=args.check_only)
        return

    # Modo interactivo
    print("\nSelecciona una opcion:")
    print("1) Instalacion Global (Antigravity / Gemini CLI + Codex)")
    print("2) Inyectar en un proyecto especifico (Claude, Cursor, Windsurf, Copilot, Gemini, Codex)")
    print("3) Salir")

    try:
        choice = input("\nOpcion [1/2/3]: ").strip()
    except EOFError:
        choice = "1"

    if choice == "1":
        install_antigravity_global()
        install_codex_global()
        print("\n[OK] Instalacion global completada con exito.")
    elif choice == "2":
        path_input = input("Introduce la ruta absoluta o relativa del proyecto: ").strip()
        if path_input:
            inject_into_project(Path(path_input))
        else:
            print("Ruta invalida.")
    else:
        print("Operacion cancelada.")

if __name__ == "__main__":
    main()
