import pytest, sys, os

sys.path.insert(0, os.getcwd())

from domainmodel.movie import Movie
from domainmodel.watchlist import WatchList

@pytest.fixture
def watchlist():
    return WatchList()

def test_init(watchlist):
    assert watchlist.size() == 0
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    assert watchlist.size() == 3

def test_add_movie(watchlist):
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie("Moana 2016")
    watchlist.add_movie(Movie("Moana", 2016))
    assert watchlist.size() == 1

def test_remove_movie(watchlist):
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    watchlist.remove_movie(Movie("Guardians of the Galaxy", 2012))
    assert watchlist.size() == 2
    
    watchlist.remove_movie(Movie("Guardians of the Galaxy", 2012))
    assert watchlist.size() == 2
    
def test_select_movie_to_watch(watchlist):
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))

    assert repr(watchlist.select_movie_to_watch(0)) == "<Movie Moana, 2016>"
    assert repr(watchlist.select_movie_to_watch(1)) == "<Movie Ice Age, 2002>"
    assert repr(watchlist.select_movie_to_watch(2)) == "<Movie Guardians of the Galaxy, 2012>"
    assert repr(watchlist.select_movie_to_watch(3)) == "None"

def test_first_movie_in_watchlist(watchlist):
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))

    assert repr(watchlist.first_movie_in_watchlist()) == "<Movie Moana, 2016>"
    watchlist.remove_movie(Movie("Moana", 2016))
    assert repr(watchlist.first_movie_in_watchlist()) == "<Movie Ice Age, 2002>"

def test_iterate(watchlist):
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    
    index = 0
    for movie in watchlist:
        assert repr(movie) == repr(watchlist.select_movie_to_watch(index))
        index += 1

    i = iter(watchlist)
    with pytest.raises(StopIteration):
        next(i)