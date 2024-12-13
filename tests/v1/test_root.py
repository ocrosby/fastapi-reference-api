def test_read_root_v1(client):
    """
    Test the root endpoint for version 1.
    """
    response = client.get("/v1/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
