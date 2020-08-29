import pytest, sys, os

sys.path.insert(0, os.getcwd())

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director
from datafilereaders.movie_file_csv_reader import MovieFileCSVReader

def test_init():
    filename = 'datafiles/Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()

    assert len(movie_file_reader.dataset_of_movies) == 1000
    assert len(movie_file_reader.dataset_of_actors) == 1985
    assert len(movie_file_reader.dataset_of_directors) == 644
    assert len(movie_file_reader.dataset_of_genres) == 20

def test_movie():
    filename = 'datafiles/Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()

    assert repr(movie_file_reader.dataset_of_movies[0]) == "<Movie Guardians of the Galaxy, 2014>"
    assert repr(movie_file_reader.dataset_of_movies[0].genres) == "[<Genre Action>, <Genre Adventure>, <Genre Sci-Fi>]"
    assert movie_file_reader.dataset_of_movies[0].description == "A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe."
    assert repr(movie_file_reader.dataset_of_movies[0].director) == "<Director James Gunn>"
    assert repr(movie_file_reader.dataset_of_movies[0].actors) == "[<Actor Chris Pratt>, <Actor Vin Diesel>, <Actor Bradley Cooper>, <Actor Zoe Saldana>]"
    assert movie_file_reader.dataset_of_movies[0].rating == 8.1
    assert movie_file_reader.dataset_of_movies[0].revenue == 333.13
    assert movie_file_reader.dataset_of_movies[0].metascore == 76

    index = 0
    for movie in movie_file_reader.dataset_of_movies:
        assert repr(movie) == repr(movie_file_reader.dataset_of_movies[index])
        assert repr(movie.genres) == repr(movie_file_reader.dataset_of_movies[index].genres)
        assert movie.description == movie_file_reader.dataset_of_movies[index].description
        assert repr(movie.director) == repr(movie_file_reader.dataset_of_movies[index].director)
        assert repr(movie.actors) == repr(movie_file_reader.dataset_of_movies[index].actors)
        assert movie.rating == movie_file_reader.dataset_of_movies[index].rating
        assert movie.revenue == movie_file_reader.dataset_of_movies[index].revenue
        assert movie.metascore == movie_file_reader.dataset_of_movies[index].metascore
        index += 1