from datetime import datetime

class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        if self.__director_full_name == other.__director_full_name:
            return True
        return False
        
    def __lt__(self, other):
        if self.__director_full_name < other.__director_full_name:
            return True
        return False

    def __hash__(self):
        return hash(self.__director_full_name)

class Genre:
    def __init__(self, genre_name: str):
        if genre_name == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name.strip()

    @property
    def name(self):
        return self.__genre_name

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        if self.__genre_name == other.__genre_name:
            return True
        return False
        
    def __lt__(self, other):
        if self.__genre_name < other.__genre_name:
            return True
        return False

    def __hash__(self):
        return hash(self.__genre_name)

class Actor:
    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()
        self.__actor_colleague: list[Actor] = list()
        # self.__actor_colleague = list()

    @property
    def name(self):
        return self.__actor_full_name

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        if self.__actor_full_name == other.__actor_full_name:
            return True
        return False
    
    def __lt__(self, other):
        if self.__actor_full_name < other.__actor_full_name:
            return True
        return False

    def __hash__(self):
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        self.__actor_colleague.append(colleague)
        colleague.__actor_colleague.append(self)

    def check_if_this_actor_worked_with(self, colleague):
        if colleague in self.__actor_colleague:
            return True
        return False

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
        self.__reviews = list()
        
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

    @property
    def reviews(self):
        return iter(self.__reviews)

    @property
    def number_of_reviews(self):
        return len(self.__reviews)

    def add_review(self, review: 'Review'):
        self.__reviews.append(review)

class Review:
    def __init__(self, user: 'User', movie: Movie, review_text: str, rating: int):
        self.__user = user

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
        elif rating > 10:
            self.__rating = 10
        elif rating < 0:
            self.__rating = 0
        
        self.__timestamp = datetime.today()
        self.__votes: int = None
        self.__metascore: int = None
    
    @property
    def user(self):
        return self.__user

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

    @property
    def votes(self) -> int:
        return self.__votes

    @votes.setter
    def votes(self, votes: int):
        if type(votes) == int and votes >= 0:
            self.__votes = votes

    @property
    def metascore(self) -> int:
        return self.__metascore

    @metascore.setter
    def metascore(self, metascore: int):
        if type(metascore) == int and metascore >=0 and metascore <= 100:
            self.__metascore = metascore

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

def make_review(review_text: str, user: User, movie: Movie, rating: int):
    review = Review(user, movie, review_text, rating)
    user.add_review(review)
    movie.add_review(review)

    return review