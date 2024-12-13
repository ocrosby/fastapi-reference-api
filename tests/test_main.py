
def test_read_root(client):
    """
    Test the root endpoint.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_health_check(client):
    """
    Test the health check endpoint.
    """
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_readiness_check(client):
    """
    Test the readiness check endpoint.
    """
    response = client.get("/readiness")
    assert response.status_code == 200
    assert response.json() == {"status": "ready"}
