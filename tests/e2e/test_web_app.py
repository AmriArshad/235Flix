import pytest

from flask import session

def test_register(client):
    response_code = client.get('/authentication/register').status_code
    assert response_code == 200

    response = client.post(
        '/authentication/register',
        data = {'username': 'gmichael', 'password': 'CarelessWhisper1984'}
    )
    assert response.headers['Location'] == 'http://localhost/authentication/login'

@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('', '', b'Username is required'),
    ('cj', '', b'Username must have 3 or more characters'),
    ('test', '', b'Password is required'),
    ('test', 'test', b'Your password must at least 8 characters, and contain an upper case letter, a lower case letter and a digit'),
    # ('thorke', 'Test#6^0', b'Username is already taken'),
))
def test_register_with_invalid_input(client, username, password, message):
    response = client.post(
        '/authentication/register',
        data = {'username': username, 'password': password}
    )
    assert message in response.data
    # print(response.data)
    # print("\n")

def test_login(client, auth):
    status_code = client.get('/authentication/login').status_code
    assert status_code == 200

    response = auth.login()
    assert response.headers['Location'] == 'http://localhost/'

    with client:
        client.get('/')
        assert session['username'] == 'thorke'

def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert 'user_id' not in session

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

def test_login_required_to_review(client):
    response = client.post('/review')
    assert response.headers['Location'] == 'http://localhost/authentication/login'

def test_review(client, auth):
    auth.login()

    response = client.get('/review?movie=Suicide+Squad')

    response = client.post(
        '/review',
        data = {'review': 'Wow amazing!', 'rating': 7, 'movie_title': 'Suicide Squad'}
    )
    assert response.headers['Location'] == 'http://localhost/display?movie=Suicide+Squad'
    
    response = client.get('/review?movie=Suicide+Squad')
    assert b'Wow amazing!' in response.data

@pytest.mark.parametrize(('review', 'rating', 'messages'), (
    ('Absolute shit movie', '1' ,b'Your review must not contain profanity'),
    ('No', '2', b'Your review is too short'),
))
def test_review_with_invalid_input(client, auth, review, rating, messages):
    auth.login()

    reponse = client.post(
        '/review',
        data = {'review': review, 'rating': rating, 'movie_title': 'Suicide Squad'}
    )

    for message in messages:
        assert message in reponse.data

def test_movies_by_title(client):
    response = client.get('/display?movie=Suicide+Squad')
    assert response.status_code == 200

    assert b'Suicide Squad' in response.data