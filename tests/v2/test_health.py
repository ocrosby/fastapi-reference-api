def test_health_check_v2(client):
    """
    Test the health check endpoint for version 2.
    """
    response = client.get("/v2/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
