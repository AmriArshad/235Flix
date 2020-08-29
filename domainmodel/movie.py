import sys
import os

sys.path.insert(0, os.getcwd())

from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director

class Movie:
    def __init__(self, title :str, release_year :int):
        self.title = title

        if type(release_year) is int and release_year >= 1900:
            self.__release_year = release_year
        else:
            self.__release_year = None           

        self.__description: str = None
        self.__director: Director = None
        self.__actors: list[Actor] = list()
        self.__genres: list[Genre] = list()
        self.__runtime_minutes: int = 0
        self.__revenue: float = None #in millions
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()

    @property
    def release_year(self) -> int:
        return self.__release_year

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        if type(description) == str:
            self.__description = description.strip()

    @property
    def director(self) -> Director:
        return self.__director
    
    @director.setter
    def director(self, director: Director):
        try:
            if type(director) == Director and self.__director == None:
                self.__director = director
        except:
            pass

    @property
    def actors(self) -> list:
        return self.__actors

    @actors.setter
    def actors(self, actors: list):
        if not any(not isinstance(actor, Actor) for actor in actors):
            self.__actors = actors

    def add_actor(self, actor: Actor):
        if type(actor) == Actor:
            self.__actors.append(actor)

    def remove_actor(self, actor: Actor):
        if type(actor) == Actor:
            try:
                self.__actors.remove(actor)
            except ValueError:
                pass

    @property
    def genres(self) -> list:
        return self.__genres

    @genres.setter
    def genres(self, genres: list):
        if not any(not isinstance(genre, Genre) for genre in genres):
            self.__genres = genres

    def add_genre(self, genre: Genre):
        if type(genre) == Genre:
            self.__genres.append(genre)

    def remove_genre(self, genre: Genre):
        if type(genre) == Genre:
            try:
                self.__genres.remove(genre)
            except ValueError:
                pass
    
    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime_minutes: int):
        if runtime_minutes > 0 and type(runtime_minutes) == int:
            self.__runtime_minutes = runtime_minutes
        else:
            raise ValueError

    def __repr__(self) -> str:
        return f"<Movie {self.__title}, {self.__release_year}>"

    def __eq__(self, other) -> bool:
        if self.concat(self.__title, self.__release_year) == self.concat(other.__title, other.__release_year):
            return True
        return False
    
    def __lt__(self, other) -> bool:
        if self.concat(self.__title, self.__release_year) < self.concat(other.__title, other.__release_year):
            return True
        return False
    
    def __hash__(self):
        return hash(self.concat(self.__title, self.__release_year))

    def concat(self, title, release_year) -> str:
        return title + str(release_year)

    @property
    def revenue(self) -> float:
        return self.__revenue

    @revenue.setter
    def revenue(self, revenue: float):
        if type(revenue) == float and revenue >= 0:
            self.__revenue = revenue