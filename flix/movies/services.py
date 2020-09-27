from typing import List, Iterable

from flix.adapters.repository import AbstractRepository
from flix.domain.model import make_review, Movie, Review, Genre

class NonExistentMovieException(Exception):
    pass

class UnknownUserException(Exception):
    pass

def add_review(movie_title: str, review_text: str, username: str, rating: int, repo: AbstractRepository):
    movie = repo.get_movie(movie_title)
    if movie is None:
        raise NonExistentMovieException

    user = repo.get_user(username)
    if user is None:
        raise UnknownUserException

    review = make_review(review_text, user, movie, rating)
    repo.add_review(review)

def get_movie(movie_title: str, repo: AbstractRepository):
    movie = repo.get_movie(movie_title)

    if movie is None:
        raise NonExistentMovieException

    return movie_to_dict(movie)

def movie_to_dict(movie: Movie):
    movie_dict = {
        'title': movie.title,
        'release': movie.release_year,
        'description': movie.description,
        'director': movie.director,
        'actors': movie.actors,
        'genres': movie.genres,
        'runtime': movie.runtime_minutes,
        'revenue': movie.revenue,
        'reviews': reviews_to_dict(movie.reviews),
    }
    return movie_dict

def review_to_dict(review: Review):
    review_dict = {
        'username': review.user,
        'movie': review.movie,
        'review_text': review.review_text,
        'rating': review.rating,
        'timestamp': review.timestamp
    }
    return review_dict

def reviews_to_dict(reviews: Iterable[Review]):
    return [review_to_dict(review) for review in reviews]

def dict_to_movie(dict):
    movie = Movie(dict.title, dict.release)
    movie.description = dict.description
    movie.director = dict.director
    movie.actors = dict.actors
    movie.genres = dict.genres
    movie.runtime_minutes = dict.runtime
    movie.revenue = dict.revenue