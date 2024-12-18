def test_readiness_check_v1(client):
    """
    Test the readiness check endpoint for version 1.
    """
    response = client.get("/v1/readiness")
    assert response.status_code == 200
    assert response.json() == {"status": "ready"}
