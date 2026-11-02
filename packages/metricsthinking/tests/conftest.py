"""Pytest configuration for MetricsThinking: ensures CWD is repository root during test runs."""
import os
from pathlib import Path
import pytest


@pytest.fixture(autouse=True, scope="session")
def isolate_cwd():
    old_cwd = Path.cwd()
    repo_root = Path(__file__).resolve().parent.parent
    os.chdir(repo_root)
    yield
    os.chdir(old_cwd)
