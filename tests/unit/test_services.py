from datetime import date

import pytest

from flix.authentication.services import AuthenticationException
from flix.movies import services as movies_services
from flix.authentication import services as auth_services
from flix.movies.services import NonExistentMovieException


def test_can_add_user(in_memory_repo):
    new_username = 'asd'
    new_password = 'abcd1A23'

    auth_services.add_user(new_username, new_password, in_memory_repo)

    user_as_dict = auth_services.get_user(new_username, in_memory_repo)
    assert user_as_dict['username'] == new_username

    assert user_as_dict['password'].startswith('pbkdf2:sha256:')

def test_cannot_add_existing_user(in_memory_repo):
    username = 'thorke'
    password = 'abcd1A23'

    auth_services.add_user(username, password, in_memory_repo)
    
    with pytest.raises(auth_services.NameNotUniqueException):
        auth_services.add_user(username, password, in_memory_repo)

def test_auth_with_valid_credentials(in_memory_repo):
    new_username = 'pmccartney'
    new_password = 'abcd1A23'

    auth_services.add_user(new_username, new_password, in_memory_repo)

    try:
        auth_services.authenticate_user(new_username, new_password, in_memory_repo)
    except:
        assert False

def test_authentication_with_invalid_credentials(in_memory_repo):
    new_username = 'pmccartney'
    new_password = 'abcd1A23'

    auth_services.add_user(new_username, new_password, in_memory_repo)

    with pytest.raises(auth_services.AuthenticationException):
        auth_services.authenticate_user(new_username, '0987654321', in_memory_repo)

def test_can_add_review(in_memory_repo):
    new_username = 'pmccartney'
    new_password = 'abcd1A23'

    auth_services.add_user(new_username, new_password, in_memory_repo)

    movie_title = "Suicide Squad"
    review_text = "Lots of carnage"
    rating = 7

    movies_services.add_review(movie_title, review_text, new_username, rating, in_memory_repo)
    reviews_as_dict = movies_services.get_reviews_for_movie(movie_title, in_memory_repo)

    assert next(
        (dictionary['review_text'] for dictionary in reviews_as_dict if dictionary['review_text'] == review_text), 
        None
    ) is not None

def text_cannot_add_review_for_non_existent_movie(in_memory_repo):
    new_username = 'pmccartney'
    new_password = 'abcd1A23'

    auth_services.add_user(new_username, new_password, in_memory_repo)

    movie_title = "fake movie"
    review_text = "Lots of carnage"
    rating = 7

    with pytest.raises(NonExistentMovieException):
        movies_services.add_review(movie_title, review_text, new_username, rating, in_memory_repo)

def test_cannot_add_review_by_unknown_user(in_memory_repo):
    movie_title = "Suicide Squad"
    review_text = "Lots of carnage"
    rating = 7
    username = 'gmichael'

    with pytest.raises(movies_services.UnknownUserException):
        movies_services.add_review(movie_title, review_text, username, rating, in_memory_repo)
        
def test_can_get_movie(in_memory_repo):
    movie_title = "Suicide Squad"

    movie_as_dict = movies_services.get_movie(movie_title, in_memory_repo)

    assert movie_as_dict['title'] == "Suicide Squad"
    assert movie_as_dict['release'] == 2016
    assert movie_as_dict['description'] == "A secret government agency recruits some of the most dangerous incarcerated super-villains to form a defensive task force. Their first mission: save the world from the apocalypse."
    assert repr(movie_as_dict['director']) == "<Director David Ayer>"
    assert repr(movie_as_dict['actors']) == "[<Actor Will Smith>, <Actor Jared Leto>, <Actor Margot Robbie>, <Actor Viola Davis>]"
    assert repr(movie_as_dict['genres']) == "[<Genre Action>, <Genre Adventure>, <Genre Fantasy>]"
    assert movie_as_dict['runtime'] == 123
    assert movie_as_dict['revenue'] == 325.02
    assert len(movie_as_dict['reviews']) == 0

def test_cannot_get_non_existent_movie(in_memory_repo):
    movie_title = "fake movie"

    with pytest.raises(NonExistentMovieException):
        movies_services.get_movie(movie_title, in_memory_repo)

def test_get_reviews_for_movie(in_memory_repo):
    new_username = 'pmccartney'
    new_password = 'abcd1A23'

    auth_services.add_user(new_username, new_password, in_memory_repo)

    movie_title = "Suicide Squad"
    review_text = "Lots of carnage"
    rating = 7

    movies_services.add_review(movie_title, review_text, new_username, rating, in_memory_repo)
    reviews_as_dict = movies_services.get_reviews_for_movie(movie_title, in_memory_repo)


    reviews_as_dict = movies_services.get_reviews_for_movie("Suicide Squad", in_memory_repo)

    assert len(reviews_as_dict) == 1

    movies = [review['movie'].title for review in reviews_as_dict]
    assert movie_title in movies and len(movies) == 1

def test_get_reviews_for_non_existent_movie(in_memory_repo):
    with pytest.raises(NonExistentMovieException):
        reviews_as_dict = movies_services.get_reviews_for_movie("fake movie", in_memory_repo)

def test_get_reviews_for_movie_without_reviews(in_memory_repo):
    reviews_as_dict = movies_services.get_reviews_for_movie("Suicide Squad", in_memory_repo)
    assert len(reviews_as_dict) == 0