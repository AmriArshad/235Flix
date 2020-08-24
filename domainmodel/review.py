from datetime import datetime
import sys, os

sys.path.insert(0, os.getcwd())

from domainmodel.movie import Movie

class Review:
    def __init__(self, movie: Movie, review_text: str, rating: int):
        if type(movie) == Movie:
            self.__movie = movie
        else:
            self.__movie = None

        if type(review_text) == str:
            self.__review_text = review_text
        else:
            self.__review_text = None

        if type(rating) == int and rating <= 10 and rating >= 0:
            self.__rating = rating
        else:
            self.__rating = None
        
        self.__timestamp = datetime.today()
        
    @property
    def movie(self):
        return self.__movie

    @property
    def review_text(self):
        return self.__review_text

    @property
    def rating(self):
        return self.__rating

    @property
    def timestamp(self):
        return self.__timestamp
        
    def __repr__(self):
        return f"<Review: {self.__movie}, Rating: {self.__rating}>"

    def __eq__(self, other):
        if self.__movie == other.__movie and self.__review_text == other.__review_text and self.__rating == other.__rating and self.__timestamp == other.__timestamp:
            return True
        return False