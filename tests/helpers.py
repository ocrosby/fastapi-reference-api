from pathlib import Path

def find_root_with_pyproject():
    """
    Find the root directory of the project by looking for a pyproject.toml file.
    """
    current_path = Path(__file__).resolve()
    for parent in current_path.parents:
        if (parent / "pyproject.toml").exists():
            return parent
    return None

def find_root_with_dockerfile():
    """
    Find the root directory of the project by looking for a Dockerfile.
    """
    current_path = Path(__file__).resolve()
    for parent in current_path.parents:
        if (parent / "Dockerfile").exists():
            return parent
    return None
