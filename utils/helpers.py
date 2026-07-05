from pathlib import Path


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def normalize_text(value: str) -> str:
    return " ".join(value.strip().split())
