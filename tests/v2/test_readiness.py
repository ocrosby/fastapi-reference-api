def test_readiness_check_v2(client):
    """
    Test the readiness check endpoint for version 2.
    """
    response = client.get("/v2/readiness")
    assert response.status_code == 200
    assert response.json() == {"status": "ready"}
