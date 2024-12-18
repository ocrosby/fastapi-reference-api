import pytest
from testcontainers.compose import DockerCompose
from fastapi.testclient import TestClient
from app.main import app
from tests.helpers import find_root_with_dockerfile

@pytest.fixture(scope="session")
def docker_compose():
    """
    Start the Docker Compose stack.
    """
    root_dir = find_root_with_dockerfile()
    with DockerCompose(root_dir) as compose:
        compose.wait_for("api")
        yield compose

@pytest.fixture(scope="module")
def client(docker_compose):
    """
    Create a FastAPI test client.
    """
    return TestClient(app)
