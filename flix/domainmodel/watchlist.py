# import sys, os

# sys.path.insert(0, os.getcwd())

from flix.domainmodel.movie import Movie

class WatchList:
    def __init__(self):
        self.__watch_list: list[Movie] = list()
        self.__index = 0
    
    def add_movie(self, movie: Movie):  
        if type(movie) == Movie and movie not in self.__watch_list:
            self.__watch_list.append(movie)
    
    def remove_movie(self, movie: Movie):
        try:
            if type(movie) == Movie:
                self.__watch_list.remove(movie)
        except:
            pass

    def select_movie_to_watch(self, index):
        try:
            return self.__watch_list[index]
        except:
            return None

    def size(self):
        return len(self.__watch_list)

    def first_movie_in_watchlist(self):
        try:
            return self.__watch_list[0]
        except:
            return None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index > self.size()-1:
            raise StopIteration
        else:
            self.__index += 1
            return self.__watch_list[self.__index-1]