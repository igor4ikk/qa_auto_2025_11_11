import pytest
import requests

@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(r.text)


@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/mojombo')
    body = r.json()
    headers = r.headers

    print(body)
    assert body['blog'] == 'http://tom.preston-werner.com'
    assert r.status_code == 200
    assert headers['Server'] == 'github.com'

@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/sergii_butenko')
    assert r.status_code == 404    