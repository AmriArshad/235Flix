from flask import Blueprint, render_template, url_for, request, session
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, TextAreaField, IntegerField, HiddenField
from wtforms.validators import DataRequired,Length, ValidationError
from better_profanity import profanity

from flix.domain.model import Actor, Director, Genre, Movie
import flix.adapters.repository as repo
import flix.movies.services as services
from flix.authentication.authentication import login_required

movies_blueprint = Blueprint('movies_bp', __name__)

@movies_blueprint.route('/')
def home():
    return render_template(
        'home.html'
    )

@movies_blueprint.route('/browse')
def browse_movies():
    movies = repo.repo_instance.get_movies()
    length = len(movies) - 1
    
    return render_template(
        'movies/browse_movies.html',
        movies = movies,
        index = repo.repo_instance.index,
        first_url = url_for('movies_bp.view', index = 0, length = length, view = "movies"),
        prev_url = url_for('movies_bp.view', index = repo.repo_instance.index - 1, length = length, view = "movies"),
        next_url = url_for('movies_bp.view', index = repo.repo_instance.index + 1, length = length, view = "movies"),
        last_url = url_for('movies_bp.view', index = length, length = length, view = "movies"),
    )

@movies_blueprint.route('/browse-actor', methods = ['GET', 'POST'])
def browse_by_actor():
    actorsMovies = movieByActor()

    if actorsMovies.validate_on_submit():
        post_actor = Actor(actorsMovies.actor_name.data)
        movies = repo.repo_instance.get_movies_acted_by(post_actor)

        return render_template(
            'movies/actors_movies.html',
            movies = movies,
            actor = post_actor
        )

    return render_template(
        'movies/get_actor.html',
        form = actorsMovies
    )

@movies_blueprint.route('/browse-genre', methods = ['GET', 'POST'])
def browse_by_genre():
    # genres = repo.repo_instance.get_genres()
    genreMovies = movieByGenre()
    genreMovies.genre_name.choices = [""] + [genre.name for genre in repo.repo_instance.get_genres()]

    if genreMovies.validate_on_submit():
        post_genre = Genre(genreMovies.genre_name.data)
        movies = repo.repo_instance.get_movies_in_genre(post_genre)

        return render_template(
            'movies/genres_movies.html',
            movies = movies,
            genre = post_genre
        )

    return render_template(
        'movies/get_genre.html',
        form = genreMovies
    )

@movies_blueprint.route('/browse-director', methods = ['GET', 'POST'])
def browse_by_director():
    directorMovies = movieByDirector()

    if directorMovies.validate_on_submit():
        post_director = Director(directorMovies.director_name.data)
        movies = repo.repo_instance.get_movies_directed_by(post_director)

        return render_template(
            'movies/directors_movies.html',
            movies = movies,
            director = post_director
        )
    
    return render_template(
        'movies/get_director.html',
        form = directorMovies
    )

@movies_blueprint.route('/find', methods = ['GET', 'POST'])
def find_movie():
    movieSearch = movieByTitle()

    if movieSearch.validate_on_submit():
        post_title = movieSearch.movie_title

        for movie in repo.repo_instance.get_movies():
            if post_title.data.lower() == movie.title.lower():
                return render_template(
                    'movies/list_movie.html',
                    movie = movie
                )
        
        return render_template(
            'movies/list_movie.html',
            movie = None
        )

    return render_template(
        'movies/find_movie.html',
        form = movieSearch,
    )

@movies_blueprint.route('/view', methods = ['GET'])
def view():
    index = int(request.args.get('index'))
    length = int(request.args.get('length'))

    if repo.repo_instance.index == 0 and index <= -1 or repo.repo_instance.index == length and index >= length:
        pass
    else:
        repo.repo_instance.index = index
    return browse_movies()

@movies_blueprint.route('/display', methods = ['GET'])
def list_movie():
    movie = None
    movie_name = request.args.get('movie')
    for movie in repo.repo_instance.get_movies():
        if movie_name.lower() == movie.title.lower():
            movie = movie
            break
    
    return render_template(
        'movies/list_movie.html',
        movie = movie
    )

@movies_blueprint.route('/review', methods = ['GET', 'POST'])
@login_required
def review_a_movie():
    username = session['username']

    form = ReviewForm()

    if form.validate_on_submit():
        movie_title = str(form.movie_title.data)

        services.add_review(movie_title, form.review.data, username, form.rating.data, repo.repo_instance)

        movie = services.get_movie(movie_title, repo.repo_instance)
        
        
        return render_template(
            'movies/list_movie.html',
            movie = repo.repo_instance.get_movie(movie_title)
        )
    
    if request.method == 'GET':
        movie_title = str(request.args.get('movie'))
        
        form.movie_title.data = movie_title
        movie = services.get_movie(movie_title, repo.repo_instance)

    else:
        movie_title = form.movie_title.data
        movie = services.get_movie(movie_title, repo.repo_instance)


    return render_template(
        'movies/review_a_movie.html',
        title = 'Edit movie',
        movie = movie,
        form = form,
    )
        

class movieByTitle(FlaskForm):
    movie_title = StringField('Movie title:', [DataRequired()])
    submit = SubmitField('Find movie')

class movieByActor(FlaskForm):
    actor_name = StringField('Actor:', [DataRequired()])
    submit = SubmitField('Find movies')

class movieByGenre(FlaskForm):
    genre_name = SelectField('Genre: ', [DataRequired()])
    submit = SubmitField('Find movies')

class movieByDirector(FlaskForm):
    director_name = StringField('Director: ', [DataRequired()])
    submit = SubmitField('Find movies')

class ProfanityFree:
    def __init__(self, message = None):
        if not message:
            message = u'Field must not contain profanity'
        self.message = message
    
    def __call__(self, form, field):
        if profanity.contains_profanity(field.data):
            raise ValidationError(self.message)

class ReviewForm(FlaskForm):
    review = TextAreaField('Review', [DataRequired(), Length(min = 3, message = 'your review is too short'), ProfanityFree(message = 'Your review must not contain profanity')])
    rating = IntegerField('Rating', [DataRequired()])
    movie_title = HiddenField('Movie title')
    submit = SubmitField('Submit')