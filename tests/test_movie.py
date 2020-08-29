import pytest, sys, os

sys.path.insert(0, os.getcwd())
from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.movie import Movie

def test_init():
    movie = Movie("Moana", 2016)
    assert repr(movie) == "<Movie Moana, 2016>"

    assert movie.title == "Moana"

    movie1 = Movie("", "1")
    assert repr(movie1) == "<Movie None, None>"

    director = Director("Ron Clements")
    movie.director = director
    assert repr(movie.director) == "<Director Ron Clements>"
    
    movie.description = "Moana, daughter of chief Tui, embarks on a journey to return the heart of goddess Te Fitti from Maui, a demigod, after the plants and the fish on her island start dying due to a blight."
    assert movie.description == "Moana, daughter of chief Tui, embarks on a journey to return the heart of goddess Te Fitti from Maui, a demigod, after the plants and the fish on her island start dying due to a blight."

    actors = [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]
    for actor in actors:
        movie.add_actor(actor)
    assert repr(movie.actors) == "[<Actor Auli'i Cravalho>, <Actor Dwayne Johnson>, <Actor Rachel House>, <Actor Temuera Morrison>]"
    
    movie.runtime_minutes = 107
    assert repr(movie.runtime_minutes) == "107"

def test_title():
    movie = Movie("   Moana   ", 2016)
    assert repr(movie) == "<Movie Moana, 2016>"

    new_title = "Test title"
    movie.title = new_title
    assert repr(movie) == "<Movie Test title, 2016>"

def test_release_year():
    movie = Movie("Old movie", 1890)
    assert repr(movie) == "<Movie Old movie, None>"

    movie1 = Movie("Less old movie", 1900)
    assert repr(movie1) == "<Movie Less old movie, 1900>"

def test_description():
    movie = Movie("Moana", 2016)
    assert movie.description == None
    movie.description = "              Moana, daughter of chief Tui, embarks on a journey to return the heart of goddess Te Fitti from Maui, a demigod, after the plants and the fish on her island start dying due to a blight.               "
    assert movie.description == "Moana, daughter of chief Tui, embarks on a journey to return the heart of goddess Te Fitti from Maui, a demigod, after the plants and the fish on her island start dying due to a blight."

def test_director():
    movie = Movie("Moana", 2016)
    director = Director("Ron Clements")
    movie.director = director
    assert repr(movie.director) == "<Director Ron Clements>"

    movie.director = "fake imposter director"
    assert repr(movie.director) == "<Director Ron Clements>"

    movie.director = Director("fake imposter director")
    assert repr(movie.director) == "<Director Ron Clements>"

def test_actor():
    movie = Movie("Moana", 2016)
    actors = [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]
    for actor in actors:
            movie.add_actor(actor)

    movie.add_actor("fake actor")
    assert repr(movie.actors) == "[<Actor Auli'i Cravalho>, <Actor Dwayne Johnson>, <Actor Rachel House>, <Actor Temuera Morrison>]"

    movie.actors = []
    assert repr(movie.actors) == "[]"

    movie.actors = [1,2,3]
    assert repr(movie.actors) == "[]"

def test_genre():
    movie = Movie("Moana", 2016)
    genres = [Genre("Animation"), Genre("Action"), Genre("Fantasy"), Genre("Children's film"), Genre("Adventure")]
    for genre in genres:
            movie.add_genre(genre)

    movie.add_genre("fake genre")
    assert repr(movie.genres) == "[<Genre Animation>, <Genre Action>, <Genre Fantasy>, <Genre Children's film>, <Genre Adventure>]"

    movie.genres = []
    assert repr(movie.genres) == "[]"

    movie.genres = [1,2,3]
    assert repr(movie.genres) == "[]"

def test_remove_actor():
    movie = Movie("Moana", 2016)
    actors = [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]
    for actor in actors:
        movie.add_actor(actor)
    assert repr(movie.actors) == "[<Actor Auli'i Cravalho>, <Actor Dwayne Johnson>, <Actor Rachel House>, <Actor Temuera Morrison>]"

    movie.remove_actor(Actor("Auli'i Cravalho"))
    assert repr(movie.actors) == "[<Actor Dwayne Johnson>, <Actor Rachel House>, <Actor Temuera Morrison>]"

    movie.remove_actor(Actor("Auli'i Cravalho"))
    assert repr(movie.actors) == "[<Actor Dwayne Johnson>, <Actor Rachel House>, <Actor Temuera Morrison>]"

def test_remove_genre():
    movie = Movie("Moana", 2016)
    genres = [Genre("Animation"), Genre("Action"), Genre("Fantasy"), Genre("Children's film"), Genre("Adventure")]

    for genre in genres:
        movie.add_genre(genre)

    assert repr(movie.genres) == "[<Genre Animation>, <Genre Action>, <Genre Fantasy>, <Genre Children's film>, <Genre Adventure>]"

    movie.remove_genre(Genre("Adventure"))
    assert repr(movie.genres) == "[<Genre Animation>, <Genre Action>, <Genre Fantasy>, <Genre Children's film>]"

    movie.remove_genre(Genre("Adventure"))
    assert repr(movie.genres) == "[<Genre Animation>, <Genre Action>, <Genre Fantasy>, <Genre Children's film>]"

def test_runtime_minutes():
    movie = Movie("Moana", 2016)
    with pytest.raises(ValueError):
        movie.runtime_minutes = -1

    movie.runtime_minutes = 107
    assert repr(movie.runtime_minutes) == "107"

def test_equal():
    movie = Movie("Moana", 2016)
    movie1 = Movie("IT", 2017)
    movie2 = Movie("Moana", 2016)

    assert (movie == movie1) == False
    assert (movie == movie2) == True

def test_less_than():
    movie = Movie("Moana", 2016)
    movie1 = Movie("IT", 2017)
    movie2 = Movie("Joker", 2019)

    assert (movie < movie1) == False
    assert (movie1 < movie2) == True

def test_hash():
    movie = Movie("Moana", 2016)
    movie1 = Movie("IT", 2017)
    movie2 = Movie("Joker", 2019)

    assert hash(movie) == hash("Moana2016")
    assert hash(movie1) == hash("IT2017")
    assert hash(movie2) == hash("Joker2019")

def test_rating():
    movie = Movie("Moana", 2016)
    assert movie.rating == None
    movie.rating = "amazing"
    assert movie.rating == None
    movie.rating = 7.7
    assert movie.rating == 7.7

def test_votes():
    movie = Movie("Moana", 2016)
    assert movie.votes == None
    movie.votes = "12321"
    assert movie.votes == None
    movie.votes = 118151
    assert movie.votes == 118151

def test_revenue():
    movie = Movie("Moana", 2016)
    assert movie.revenue == None
    movie.revenue = "N/A"
    assert movie.revenue == None
    movie.revenue = 248.75
    assert movie.revenue == 248.75

def test_metascore():
    movie = Movie("Moana", 2016)
    assert movie.metascore == None
    movie.metascore = "N/A"
    assert movie.metascore == None
    movie.metascore = 81
    assert movie.metascore == 81