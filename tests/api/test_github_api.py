import pytest
from modules.api.clients.github import GitHub

@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('defunktihorr')
    assert r['message'] == 'Not Found'

# знайти к-сть репозиторіїв 'become-qa-auto' які є в наявності 
@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 57
    assert 'become-qa-auto' in r['items'][0]['name']

# знайти репозиторій якого не існує
@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergbutenko_repo_non-foun')
    assert r['total_count'] == 0   

# пошук по назві репозиторію з одною літерою
@pytest.mark.api
def test_repo_with_singl_char(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0 