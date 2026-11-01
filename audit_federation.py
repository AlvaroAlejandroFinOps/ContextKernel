#!/usr/bin/env python3
"""Compatibility entrypoint for the versioned iContext v6 runtime."""
import sys
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent / "tools/icontext_runtime"))
from icontext_cli import main

if __name__ == "__main__":
    args = sys.argv[1:]
    if "--fix" in args:
        args.remove("--fix")
        raise SystemExit(main(["doctor", "--fix", *args]))
    raise SystemExit(main(["audit", *args]))
