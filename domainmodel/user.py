import sys, os

sys.path.insert(0, os.getcwd())

from domainmodel.movie import Movie
from domainmodel.review import Review

class User:
    def __init__(self, user_name: str, password: str):
        if user_name == "" or type(user_name) is not str:
            self.__user_name = None
        else:
            self.__user_name = user_name.strip().lower()
            
        if password == "" or type(password) is not str:
            self.__password = None
        else:
            self.__password = password
            
        self.__watched_movies: list[Movie] = list()
        self.__reviews: list[Review] = list()
        self.__time_spent_watching_movies_minutes: int = 0

    @property
    def user_name(self):
        return self.__user_name

    @property
    def password(self):
        return self.__password

    @property
    def watched_movies(self):
        return self.__watched_movies

    @property
    def reviews(self):
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent_watching_movies_minutes

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other):
        if self.__user_name == other.__user_name:
            return True
        return False

    def __lt__(self, other):
        if self.__user_name < other.__user_name:
            return True
        return False

    def __hash__(self):
        return hash(self.__user_name)

    def watch_movie(self, movie: Movie):
        if type(movie) == Movie:
            if movie not in self.__watched_movies:
                self.__watched_movies.append(movie)
            self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review: Review):
        if type(review) == Review:
            if review not in self.__reviews:
                self.__reviews.append(review)