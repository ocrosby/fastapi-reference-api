from pathlib import Path

def find_root_with_pyproject():
    current_path = Path(__file__).resolve()
    for parent in current_path.parents:
        if (parent / "pyproject.toml").exists():
            return parent
    return None

def find_root_with_dockerfile():
    current_path = Path(__file__).resolve()
    for parent in current_path.parents:
        if (parent / "Dockerfile").exists():
            return parent
    return None
