def test_sanity():
    assert 200 == 200


def test_index(client):
    response = client.get('/index/')
    assert response.status_code == 200
