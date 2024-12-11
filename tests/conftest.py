import pytest
from testcontainers.compose import DockerCompose
from fastapi.testclient import TestClient
from app.main import app
from tests.helpers import find_root_with_dockerfile


@pytest.fixture(scope="session")
def docker_compose():
    root_dir = find_root_with_dockerfile()
    compose_file = root_dir.joinpath("docker-compose.yml")
    with DockerCompose(compose_file) as compose:
        compose.wait_for("api")
        yield compose

@pytest.fixture(scope="module")
def client(docker_compose):
    return TestClient(app)
