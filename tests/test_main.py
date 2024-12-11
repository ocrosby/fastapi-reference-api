
def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_health_check(client):
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_readiness_check(client):
    response = client.get("/readiness")
    assert response.status_code == 200
    assert response.json() == {"status": "ready"}
