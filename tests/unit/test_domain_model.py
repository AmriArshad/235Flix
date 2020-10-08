import pytest
from datetime import datetime

from flix.domain.model import Director, Genre, Actor, Movie, Review, User, WatchList, make_review

@pytest.fixture
def user():
    return User('Martin', 'pw12345')

@pytest.fixture
def movie():
    return Movie("Moana", 2016)

@pytest.fixture
def review(user, movie):
    return make_review("This movie was very enjoyable.", user, movie, 8)
    
@pytest.fixture
def watchlist():
    return WatchList()

# DIRECTOR tests
def test_init():
    director1 = Director("Taika Waititi")
    assert repr(director1) == "<Director Taika Waititi>"
    director2 = Director("")
    assert director2.director_full_name is None
    director3 = Director(42)
    assert director3.director_full_name is None

def test_equal():
    director1 = Director("Taika Waititi")
    director2 = Director("Peter Jackson")
    director3 = Director("Taika Waititi")

    assert (director1 == director2) == False
    assert (director1 == director3) == True

def test_less_than():
    director1 = Director("Taika Waititi")
    director2 = Director("Peter Jackson")

    assert (director1 < director2) == False

def test_hash():
    director1 = Director("Taika Waititi")
    assert hash(director1) == hash("Taika Waititi")
    director2 = Director("Peter Jackson")
    assert hash(director2) == hash("Peter Jackson")

# GENRE tests

def test_init():
    genre1 = Genre("Horror")
    assert repr(genre1) == "<Genre Horror>"
    genre2 = Genre("")
    assert repr(genre2) == "<Genre None>"

def test_equal():
    genre1 = Genre("Horror")
    genre2 = Genre("")
    genre3 = Genre("Horror")

    assert (genre1 == genre2) == False
    assert (genre1 == genre3) == True

def test_less_than():
    genre1 = Genre("Horror")
    genre2 = Genre("Comedy")

    assert (genre1 < genre2) == False

def test_hash():
    genre1 = Genre("Horror")
    assert hash(genre1) == hash("Horror")
    genre2 = Genre("Comedy")
    assert hash(genre2) == hash("Comedy")

# ACTOR tests

def test_init():
    actor1 = Actor("Angelina Jolie")
    assert repr(actor1) == "<Actor Angelina Jolie>"
    actor2 = Actor("")
    assert repr(actor2) == "<Actor None>"
    actor3 = Actor(42)
    assert repr(actor3) == "<Actor None>"

def test_equal():
    actor1 = Actor("Angelina Jolie")
    actor2 = Actor("Brad Pitt")
    actor3 = Actor("Angelina Jolie")

    assert (actor1 == actor2) == False
    assert (actor1 == actor3) == True

def test_less_than():
    actor1 = Actor("Angelina Jolie")
    actor2 = Actor("Brad Pitt")

    assert (actor1 < actor2) == True

def test_hash():
    actor1 = Actor("Angelina Jolie")
    assert hash(actor1) == hash("Angelina Jolie")
    actor2 = Actor("Brad Pitt")
    assert hash(actor2) == hash("Brad Pitt")

def test_add_colleague():
    actor1 = Actor("Angelina Jolie")
    actor2 = Actor("Brad Pitt")

    assert actor1.check_if_this_actor_worked_with(actor2) == False
    actor1.add_actor_colleague(actor2)
    assert actor1.check_if_this_actor_worked_with(actor2) == True
    assert actor2.check_if_this_actor_worked_with(actor1) == True

# MOVIE tests

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

def test_revenue():
    movie = Movie("Moana", 2016)
    assert movie.revenue == None
    movie.revenue = "N/A"
    assert movie.revenue == None
    movie.revenue = 248.75
    assert movie.revenue == 248.75

# REVIEW tests

def test_review_relationships(review, movie, user):

    assert review in user.reviews
    assert review.user is user
    assert review in movie.reviews
    assert review.movie is movie    

def test_init(review, user):
    assert repr(review) == "<Review: <Movie Moana, 2016>, Rating: 8>"

    review1 = Review(user, Movie("IT", 2017), "Ooo scaryyy", 10)
    assert repr(review1) == "<Review: <Movie IT, 2017>, Rating: 10>"

def test_review_text(review, user):
    assert review.review_text == "This movie was very enjoyable."
    
    review1 = Review(user, Movie("IT", 2017), 1, 10)
    assert review1.review_text == None

def test_rating(review, user):
    assert repr(review.rating) == "8"

    review1 = Review(user, Movie("IT", 2017), "Ooo scaryyy", -1)
    assert review1.rating == None

    review1 = Review(user, Movie("Joker", 2019), "Thrilling", 11)
    assert review1.rating == None

# the following two tests will fail at times because of slight differences in the date
# def test_timestamp(review):
#     assert review.timestamp == datetime.today()

# def test_equal(review):
#     assert (review == Review(Movie("Moana", 2016), "This movie was very enjoyable.", 8)) == True
#     assert (review == Review(Movie("IT", 2017), "Ooo scaryyy", 10)) == False

def test_votes(review):
    assert review.votes == None
    review.votes = "12321"
    assert review.votes == None
    review.votes = 118151
    assert review.votes == 118151

def test_metascore(review):
    assert review.metascore == None
    review.metascore = "N/A"
    assert review.metascore == None
    review.metascore = 81
    assert review.metascore == 81

# USER tests 

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

# WATCHLIST tests



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