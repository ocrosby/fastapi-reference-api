def test_read_root_v2(client):
    """
    Test the root endpoint for version 2.
    """
    response = client.get("/v2/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
