import pytest
# import sys, os

# sys.path.insert(0, os.getcwd())

from flix.domainmodel.movie import Movie
from flix.domainmodel.review import Review
from flix.domainmodel.user import User

@pytest.fixture
def movie():
    return Movie("Moana", 2016)

@pytest.fixture
def review():
    return Review(Movie("Moana", 2016), "This movie was very enjoyable.", 8)

def test_init():
    user1 = User('Martin', 'pw12345')
    user2 = User('Ian', 'pw67890')
    user3 = User('Daniel', 'pw87465')

    assert repr(user1) == "<User martin>"
    assert repr(user2) == "<User ian>"
    assert repr(user3) == "<User daniel>"

def test_user_name():
    user1 = User('Martin', 'pw12345')
    assert user1.user_name == "martin"

    user2 = User('         Ian       ', 'pw67890')
    assert user2.user_name == "ian"

    user3 = User("", "pw87465")
    assert user3.user_name == None

    user4 = User(1, "pw87465")
    assert user4.user_name == None

def test_password():
    user1 = User('Martin', 'pw12345')
    assert user1.password == "pw12345"

    user2 = User('Ian', 1)
    assert user2.password == None

    user3 = User('Daniel', "")
    assert user3.password == None

def test_watched_movies():
    user1 = User('Martin', 'pw12345')
    assert repr(user1.watched_movies) == "[]"
    
def test_reviews():
    user1 = User('Martin', 'pw12345')
    assert repr(user1.reviews) == "[]"

def test_time_spend_watching_movies():
    user1 = User('Martin', 'pw12345')
    assert user1.time_spent_watching_movies_minutes == 0

def test_equal():
    user1 = User('Martin', 'pw12345')
    user2 = User('Ian', 'pw67890')
    user3 = User('Martin', 'pw12345')

    assert (user1 == user2) == False
    assert (user1 == user3) == True

def test_less_than():
    user1 = User('Martin', 'pw12345')
    user2 = User('Ian', 'pw67890')

    assert (user1 < user2) == False

def test_hash():
    user1 = User('Martin', 'pw12345')
    assert hash(user1) == hash("martin")

def test_watch_movie(movie):
    user1 = User('Martin', 'pw12345')
    movie.runtime_minutes = 107
    movie1 = Movie("IT", 2017)
    movie1.runtime_minutes = 146
    movie2 = Movie("Joker", 2019)
    movie2.runtime_minutes = 122
    movie3 = "Fake movie"

    assert repr(user1.watched_movies) == "[]"

    user1.watch_movie(movie)
    user1.watch_movie(movie1)
    user1.watch_movie(movie2)
    user1.watch_movie(movie3)

    assert repr(user1.watched_movies) == "[<Movie Moana, 2016>, <Movie IT, 2017>, <Movie Joker, 2019>]"
    assert user1.time_spent_watching_movies_minutes == 375

def test_add_review(review):
    user1 = User('Martin', 'pw12345')
    user1.add_review(review)

    assert repr(user1.reviews) == "[<Review: <Movie Moana, 2016>, Rating: 8>]"