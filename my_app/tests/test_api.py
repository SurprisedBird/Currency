from django.test import client
from rest_framework.test import APIClient


def test_get_rates():
    client = APIClient()
    url = '/api/v1/rates/'
    response = client.get(url)
    assert response.status_code == 200
    assert response.json()


def test_post_rates():
    client = APIClient()
    url = '/api/v1/rates/'
    response = client.post(url)
    assert response.status_code == 200
    assert response.json()
