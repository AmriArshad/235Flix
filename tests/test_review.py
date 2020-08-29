import pytest, sys, os
from datetime import datetime

sys.path.insert(0, os.getcwd())

from domainmodel.movie import Movie
from domainmodel.review import Review

@pytest.fixture
def review():
    return Review(Movie("Moana", 2016), "This movie was very enjoyable.", 8)

def test_init(review):
    assert repr(review) == "<Review: <Movie Moana, 2016>, Rating: 8>"

    review1 = Review(Movie("IT", 2017), "Ooo scaryyy", 10)
    assert repr(review1) == "<Review: <Movie IT, 2017>, Rating: 10>"

def test_movie(review):
    assert repr(review.movie) == "<Movie Moana, 2016>"

    review1 = Review("IT", "Ooo scaryyy", 10)
    assert review1.movie == None

def test_review_text(review):
    assert review.review_text == "This movie was very enjoyable."
    
    review1 = Review(Movie("IT", 2017), 1, 10)
    assert review1.review_text == None

def test_rating(review):
    assert repr(review.rating) == "8"

    review1 = Review(Movie("IT", 2017), "Ooo scaryyy", -1)
    assert review1.rating == None

    review1 = Review(Movie("Joker", 2019), "Thrilling", 11)
    assert review1.rating == None

# the following two tests will fail at times because of slight differences in the date
# def test_timestamp(review):
#     assert review.timestamp == datetime.today()

# def test_equal(review):
#     assert (review == Review(Movie("Moana", 2016), "This movie was very enjoyable.", 8)) == True
#     assert (review == Review(Movie("IT", 2017), "Ooo scaryyy", 10)) == False