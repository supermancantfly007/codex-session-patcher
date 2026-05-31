import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def test_legacy_setup_metadata_exposes_runtime_modules(tmp_path: Path):
    result = subprocess.run(
        [sys.executable, "setup.py", "egg_info", "--egg-base", str(tmp_path)],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr

    egg_info = tmp_path / "codex_session_patcher.egg-info"
    top_level = (egg_info / "top_level.txt").read_text(encoding="utf-8").splitlines()
    entry_points = (egg_info / "entry_points.txt").read_text(encoding="utf-8")

    assert "codex_patcher" in top_level
    assert "codex_session_patcher" in top_level
    assert "web" in top_level
    assert "codex-patcher = codex_session_patcher.cli:main" in entry_points
    assert "codex-patcher-web = web.backend.main:run_server" in entry_points
