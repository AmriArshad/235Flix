import abc

from flix.domain.model import Director, Genre, Actor, Movie, Review, User, WatchList

class RepositoryException(Exception):
	def __init__(self, message = None):
		pass

repo_instance = None

class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_user(self, user: User):
        # adds a User to the repo
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, name) -> User:
        # returns the User named name from the repo
        # if there is no such User, return None
        raise NotImplementedError

    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        # adds a Movie to the repo
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self, title) -> Movie:
        # returns a Movie named title from the repo
        # if no such Movie exists, return None        
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies(self):
        # returns all movies in repo
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_movies(self) -> int:
        # returns number of movies in the repo
        raise NotImplementedError

    @abc.abstractmethod
    def get_first_movie(self) -> Movie:
        # returns the first movie in the repo
        # if repo is empty return None
        raise NotImplementedError

    @abc.abstractmethod
    def get_last_movie(self) -> Movie:
        # returns the last movie in the repo
        # if repo is empty return None
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_acted_by(self, actor: Actor):
        # returns a list of movies acted by actor
        # if there are no matches, return empty list
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_in_genre(self, genre: Genre):
        # returns a list of movies which are part of genre
        # if there are no matches, return empty list
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_directed_by(self, director: Director):
        # returns a list of movies that were directed by director
        # if there are no matches, return empty list
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_released_in(self, release_year: int):
        # returns a list of movies released in release_year
        # if there are no matches, return empty list
        raise NotImplementedError

    @abc.abstractmethod
    def add_genre(self, genre: Genre):
        # adds a Genre to the repo
        raise NotImplementedError

    @abc.abstractmethod
    def get_genres(self):
        # returns the genres in the repo
        raise NotImplementedError

    @abc.abstractmethod
    def add_director(self, director: Director):
        # adds a Director to the repo
        raise NotImplementedError

    @abc.abstractmethod
    def get_directors(self):
        # returns the directors in the repo
        raise NotImplementedError

    @abc.abstractmethod
    def add_actor(self, actor: Actor):
        # adds a Actor to the repo
        raise NotImplementedError

    @abc.abstractmethod
    def get_actors(self):
        # returns the actors in the repo
        raise NotImplementedError

    @abc.abstractmethod
    def add_review(self, review: Review):
        # adds a Review to the repo
        # if the review doesn't have bidirectional links
        # with a Movie and a User, return RepositoryException
        if review.user is None or review not in review.user.reviews:
            raise RepositoryException("Review not correctly attached to a User")
        if review.movie is None or review not in review.movie.reviews:
            raise RepositoryException("Review not correctly attached to a Movie")

    @abc.abstractmethod
    def get_reviews(self):
        # returns the Reviews in the repo
        raise NotImplementedError