from requests.auth import HTTPBasicAuth 
import pytest
import requests

basic_auth = HTTPBasicAuth('1VQDHXQ8EF73QTHESPT7UHU9AJQPLXXL', '')

def test_get_request():
    resp = requests.get('http://164.92.218.36:8080/9-art', auth=basic_auth)
    assert resp.status_code == 200

def test_get_request_again():
    resp = requests.get('http://164.92.218.36:8080/6-accessories', auth=basic_auth)
    assert resp.status_code == 200

def test_get_request_contacts():
    resp = requests.get('http://164.92.218.36:8080/api/contacts', auth=basic_auth)
    assert resp.status_code == 200


def test_authorization():
    url = 'http://164.92.218.36:8080/login?back=my-account'
    data = {'username': 'Sara', 'password': 'Kapibara99'}
    response = requests.post(url, json=data)
    assert response.status_code == 200

