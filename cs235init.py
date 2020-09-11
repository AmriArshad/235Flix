from flix.datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from flix.domainmodel.user import User, Review, Movie

def main():
    filename = 'flix/datafiles/Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()



if __name__ == "__main__":
    main()