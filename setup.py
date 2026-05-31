from pathlib import Path

from setuptools import find_packages, setup


ROOT = Path(__file__).parent

WEB_REQUIRES = [
    "fastapi>=0.100.0",
    "uvicorn>=0.23.0",
    "pydantic>=2.0.0",
    "websockets>=11.0",
    "httpx>=0.24.0",
]

DEV_REQUIRES = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
    "setuptools>=58.0.0",
]

BUILD_REQUIRES = [
    "pyinstaller>=6.0.0",
]


setup(
    name="codex-session-patcher",
    version="1.4.2",
    description=(
        "AI coding session cleaner with CTF/pentest prompt injection; "
        "supports Codex, Claude Code, OpenCode"
    ),
    long_description=(ROOT / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
    license="MIT",
    author="Your Name",
    author_email="your@email.com",
    keywords=["codex", "cli", "session", "patcher"],
    py_modules=["codex_patcher"],
    packages=find_packages(
        include=[
            "codex_session_patcher",
            "codex_session_patcher.*",
            "web",
            "web.*",
        ]
    ),
    package_data={"codex_session_patcher": ["ctf_config/prompts/*.md"]},
    install_requires=[],
    extras_require={
        "web": WEB_REQUIRES,
        "dev": DEV_REQUIRES,
        "build": BUILD_REQUIRES,
    },
    entry_points={
        "console_scripts": [
            "codex-patcher=codex_session_patcher.cli:main",
            "codex-patcher-web=web.backend.main:run_server",
        ]
    },
)
