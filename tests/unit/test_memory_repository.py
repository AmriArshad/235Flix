import pytest
from datetime import datetime

from flix.datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from flix.domain.model import Director, Genre, Actor, Movie, Review, User, WatchList, make_review
from flix.adapters.memory_repository import MemoryRepository
from flix.adapters.repository import RepositoryException

def test_add_and_get_user(in_memory_repo):
    in_memory_repo.add_user(User("Martin", "pw12345"))
    assert in_memory_repo.get_user("Martin") == User("Martin", "pw12345")

    assert in_memory_repo.get_user("fake user") is None

def test_add_and_get_movie(in_memory_repo):
    assert in_memory_repo.get_number_of_movies() == 1000
    assert in_memory_repo.get_movie("Moana") == Movie("Moana", 2016)

    in_memory_repo.add_movie(Movie("test", 2020))
    assert in_memory_repo.get_movie("test") == Movie("test", 2020)
    assert in_memory_repo.get_number_of_movies() == 1001

    assert in_memory_repo.get_movie("test1") == None

def test_get_movies(in_memory_repo):
    movies = in_memory_repo.get_movies()
    assert len(movies) == in_memory_repo.get_number_of_movies()

def test_get_movies_in_genre(in_memory_repo):
    action_movies = in_memory_repo.get_movies_in_genre(Genre("Action"))
    assert len(action_movies) == 303
    assert len(in_memory_repo.get_movies_in_genre(Genre("Fake genre"))) == 0

def test_get_movies_directed_by(in_memory_repo):
    ron_clements_movies = in_memory_repo.get_movies_directed_by(Director("Ron Clements"))
    assert len(ron_clements_movies) == 2
    assert len(in_memory_repo.get_movies_directed_by(Director("fake director"))) == 0

def test_add_and_get_genre(in_memory_repo):
    in_memory_repo.add_genre(Genre("new genre"))
    assert Genre("new genre") in in_memory_repo.get_genres()

    assert Genre("fake genre") not in in_memory_repo.get_genres()

def test_add_and_get_director(in_memory_repo):
    in_memory_repo.add_director(Director("new director"))
    assert Director("new director") in in_memory_repo.get_directors()

    assert Director("fake director") not in in_memory_repo.get_directors()

def test_add_and_get_actor(in_memory_repo):
    in_memory_repo.add_actor(Actor("new actor"))
    assert Actor("new actor") in in_memory_repo.get_actors()

    assert Actor("fake actor") not in in_memory_repo.get_actors()

def test_add_and_get_reviews(in_memory_repo):
    assert len(in_memory_repo.get_reviews()) == 0
    
    review = make_review("Great movie", User("Martin", "pw12345"), Movie("Guardians of the Galaxy", 2014), 8)
    
    in_memory_repo.add_review(review)
    assert review in in_memory_repo.get_reviews()

def test_add_review_without_user(in_memory_repo):
    with pytest.raises(RepositoryException):
        in_memory_repo.add_review(Review(None, Movie("Guardians of the Galaxy", 2014), "Wow!", 9))
    
def test_add_review_without_movie_attached(in_memory_repo):
    user = User("Martin", "pw12345")
    review = Review(user, Movie("Guardians of the Galaxy", 2014), "Wow!", 9)
    user.add_review(review)

    with pytest.raises(RepositoryException):
        in_memory_repo.add_review(Review(None, Movie("Guardians of the Galaxy", 2014), "Wow!", 9))