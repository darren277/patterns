""""""

def test_data_service_with_caching(client):
    # First request (cache miss)
    response = client.get('/data?query=test_query')
    assert response.status_code == 200
    assert b'{"data":"Result for test_query"}' in response.data

    # Second request with the same query (cache hit)
    response = client.get('/data?query=test_query')
    assert response.status_code == 200
    assert b'{"data":"Result for test_query"}' in response.data

    # Test another query (new cache miss)
    response = client.get('/data?query=another_query')
    assert response.status_code == 200
    assert b'{"data":"Result for another_query"}' in response.data
