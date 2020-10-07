from datetime import datetime

from flix.datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from flix.domain.model import Director, Genre, Actor, Movie, Review, User, WatchList
from flix.adapters.repository import AbstractRepository, RepositoryException

class MemoryRepository(AbstractRepository):
    def __init__(self):
        self.__movies = list()
        self.__genres = list()
        self.__directors = list()
        self.__actors = list()
        self.__users = list()
        self.__reviews = list()
        self.index = 0

    def add_user(self, user: User):
        self.__users.append(user)

    def get_user(self, name) -> User:
        return next((user for user in self.__users if user.user_name == name.strip().lower()), None)

    def add_movie(self, movie: Movie):
        self.__movies.append(movie)

    def get_movie(self, title) -> Movie:
        return next((movie for movie in self.__movies if movie.title == title), None)

    def get_movies(self):
        return self.__movies

    def get_number_of_movies(self) -> int:
        return len(self.__movies)

    def get_movies_by_title(self, search_item) -> Movie:
        return [movie for movie in self.__movies if search_item.lower() in movie.title.lower()]

    def get_movies_acted_by(self, actor: Actor):
        return [movie for movie in self.__movies if actor in movie.actors]

    def get_movies_in_genre(self, genre: Genre):
        return [movie for movie in self.__movies if genre in movie.genres]

    def get_movies_directed_by(self, director: Director):
        return [movie for movie in self.__movies if movie.director == director]

    def get_movies_released_in(self, release_year: int):
        return [movie for movie in self.__movies if movie.release_year == release_year]

    def add_genre(self, genre: Genre):
        self.__genres.append(genre)

    def get_genres(self):
        return self.__genres

    def add_director(self, director: Director):
        self.__directors.append(director)

    def get_directors(self):
        return self.__directors

    def add_actor(self, actor: Actor):
        self.__actors.append(actor)

    def get_actors(self):
        return self.__actors

    def add_review(self, review: Review):
        super().add_review(review)
        self.__reviews.append(review)

    def get_reviews(self):
        return self.__reviews    

    def populate(self, filename: str):
        movie_file_reader = MovieFileCSVReader(filename)
        movie_file_reader.read_csv_file()

        self.__movies = movie_file_reader.dataset_of_movies
        self.__actors = movie_file_reader.dataset_of_actors
        self.__directors = movie_file_reader.dataset_of_directors
        self.__genres = movie_file_reader.dataset_of_genres