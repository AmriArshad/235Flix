import pytest
from datetime import datetime

from flix.datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from flix.domain.model import Director, Genre, Actor, Movie, Review, User, WatchList, make_review
from flix.adapters.memory_repository import MemoryRepository
from flix.adapters.repository import RepositoryException

@pytest.fixture
def repo():
    repository = MemoryRepository()
    repository.populate("flix/datafiles/Data1000Movies.csv")
    return repository

def test_add_and_get_user(repo):
    repo.add_user(User("Martin", "pw12345"))
    assert repo.get_user("Martin") == User("Martin", "pw12345")

    assert repo.get_user("fake user") is None

def test_add_and_get_movie(repo):
    assert repo.get_number_of_movies() == 1000
    assert repo.get_movie("Moana") == Movie("Moana", 2016)

    repo.add_movie(Movie("test", 2020))
    assert repo.get_movie("test") == Movie("test", 2020)
    assert repo.get_number_of_movies() == 1001

    assert repo.get_movie("test1") == None

def test_get_movies(repo):
    movies = repo.get_movies()
    assert len(movies) == repo.get_number_of_movies()

def test_first_and_last_movie(repo):
    assert repo.get_first_movie() == Movie("Guardians of the Galaxy", 2014)
    assert repo.get_last_movie() == Movie("Nine Lives", 2016)

def test_get_movies_acted_by(repo):
    brads_movies = repo.get_movies_acted_by(Actor("Brad Pitt"))
    assert len(brads_movies) == 13
    assert len(repo.get_movies_acted_by(Actor("fake actor"))) == 0

def test_get_movies_in_genre(repo):
    action_movies = repo.get_movies_in_genre(Genre("Action"))
    assert len(action_movies) == 303
    assert len(repo.get_movies_in_genre(Genre("Fake genre"))) == 0

def test_get_movies_directed_by(repo):
    ron_clements_movies = repo.get_movies_directed_by(Director("Ron Clements"))
    assert len(ron_clements_movies) == 2
    assert len(repo.get_movies_directed_by(Director("fake director"))) == 0

def test_get_movies_released_in(repo):
    movies_2016 = repo.get_movies_released_in(2016)
    assert len(movies_2016) == 297
    assert len(repo.get_movies_released_in(2020)) == 0

def test_add_and_get_genre(repo):
    repo.add_genre(Genre("new genre"))
    assert Genre("new genre") in repo.get_genres()

    assert Genre("fake genre") not in repo.get_genres()

def test_add_and_get_director(repo):
    repo.add_director(Director("new director"))
    assert Director("new director") in repo.get_directors()

    assert Director("fake director") not in repo.get_directors()

def test_add_and_get_actor(repo):
    repo.add_actor(Actor("new actor"))
    assert Actor("new actor") in repo.get_actors()

    assert Actor("fake actor") not in repo.get_actors()

def test_add_and_get_reviews(repo):
    assert len(repo.get_reviews()) == 0
    
    review = make_review("Great movie", User("Martin", "pw12345"), Movie("Guardians of the Galaxy", 2014), 8)
    
    repo.add_review(review)
    assert review in repo.get_reviews()

def test_add_review_without_user(repo):
    with pytest.raises(RepositoryException):
        repo.add_review(Review(None, Movie("Guardians of the Galaxy", 2014), "Wow!", 9))
    
def test_add_review_without_movie_attached(repo):
    user = User("Martin", "pw12345")
    review = Review(user, Movie("Guardians of the Galaxy", 2014), "Wow!", 9)
    user.add_review(review)

    with pytest.raises(RepositoryException):
        repo.add_review(Review(None, Movie("Guardians of the Galaxy", 2014), "Wow!", 9))