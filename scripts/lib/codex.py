"""Codex CLI resolution helpers."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys


def resolve_codex_executable() -> str:
    if sys.platform == "win32":
        for candidate in ("codex.cmd", "codex.exe", "codex"):
            resolved = shutil.which(candidate)
            if resolved:
                return os.path.abspath(resolved)

    resolved = shutil.which("codex")
    if resolved:
        return os.path.abspath(resolved)

    raise RuntimeError("Command 'codex' not found. Install the Codex CLI and add it to PATH.")


def ensure_codex_available() -> str:
    return resolve_codex_executable()


def codex_version(codex_executable: str | None = None) -> str:
    executable = codex_executable or resolve_codex_executable()
    try:
        result = subprocess.run(
            [executable, "--version"],
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError:
        return "unknown"
    output = (result.stdout or result.stderr or "").strip()
    return output.splitlines()[0].strip() if output else "unknown"
