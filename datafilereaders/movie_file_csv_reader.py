import sys
import os

sys.path.insert(0, os.getcwd())

import csv

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director

class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies = list()
        self.__dataset_of_actors = list()
        self.__dataset_of_directors = list()
        self.__dataset_of_genres = list()

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            # index = 0
            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                movie = Movie(title, release_year)
                
                movie.description = row['Description']

                movie.director = Director(row['Director'])
                if Director(row['Director']) not in self.__dataset_of_directors:
                    self.__dataset_of_directors.append(Director(row['Director']))

                for actor in row['Actors'].split(','):
                    movie.add_actor(Actor(actor))
                    if Actor(actor) not in self.dataset_of_actors:
                        self.dataset_of_actors.append(Actor(actor))

                for genre in row['Genre'].split(','):
                    movie.add_genre(Genre(genre))
                    if Genre(genre) not in self.dataset_of_genres:
                        self.dataset_of_genres.append(Genre(genre))

                movie.runtime_minutes = int(row['Runtime (Minutes)'])
                
                try:
                    movie.revenue = float(row['Revenue (Millions)'])
                except:
                    pass
                
                self.__dataset_of_movies.append(movie)
                # print(f"Movie {index} with title: {title}, release year {release_year}")
                # index += 1

    @property
    def dataset_of_movies(self):
        return self.__dataset_of_movies

    @property
    def dataset_of_actors(self):
        return self.__dataset_of_actors

    @property
    def dataset_of_directors(self):
        return self.__dataset_of_directors

    @property
    def dataset_of_genres(self):
        return self.__dataset_of_genres