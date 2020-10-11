import pytest

from flix import create_app
from flix.adapters import memory_repository
from flix.adapters.memory_repository import MemoryRepository

TEST_DATA_PATH = "tests/data/movies.csv"

@pytest.fixture
def in_memory_repo():
    repo = MemoryRepository()
    repo.populate(TEST_DATA_PATH)
    return repo

@pytest.fixture
def client():
    my_app = create_app({
        'TESTING': True,
        'TEST_DATA_PATH': TEST_DATA_PATH,
        'WTF_CSRF_ENABLED': False
    })

    return my_app.test_client()

class AuthenticationManager:
    def __init__(self, client):
        self._client = client

    def login(self, username = 'thorke', password = 'wPO9A75e*z!t'):
        return self._client.post(
            'authentication/login',
            data = {'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/authentication/logout')

@pytest.fixture
def auth(client):
    client.post(
        '/authentication/register',
        data = {'username': 'thorke', 'password': 'wPO9A75e*z!t'}
    )
    return AuthenticationManager(client)