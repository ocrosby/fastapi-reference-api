def test_health_check_v1(client):
    """
    Test the health check endpoint for version 1.
    """
    response = client.get("/v1/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
