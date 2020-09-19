from flask import Blueprint, render_template, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import flix.adapters.repository as repo

movies_blueprint = Blueprint('movies_bp', __name__)

@movies_blueprint.route('/')
def home():
    return render_template(
        'home.html',
        find_movie_url = url_for('movies_bp.find_movie'),
        browse_movies_url = url_for('movies_bp.browse_movies')
    )

@movies_blueprint.route('/listall')
def browse_movies():
    movies = repo.repo_instance.get_movies()
    length = len(movies) - 1
    
    return render_template(
        'browse_movies.html',
        movies = movies,
        index = repo.repo_instance.index,
        first_url = url_for('movies_bp.view', index = 0, length = length),
        prev_url = url_for('movies_bp.view', index = repo.repo_instance.index - 1, length = length),
        next_url = url_for('movies_bp.view', index = repo.repo_instance.index + 1, length = length),
        last_url = url_for('movies_bp.view', index = length, length = length),
        home_url = url_for('movies_bp.home'),
        find_movie_url = url_for('movies_bp.find_movie'),
        browse_movies_url = url_for('movies_bp.browse_movies')
    )

@movies_blueprint.route('/find', methods = ['GET', 'POST'])
def find_movie():
    form = SearchForm()

    if form.validate_on_submit():
        post_title = form.movie_title

        for movie in repo.repo_instance.get_movies():
            if post_title.data.lower() == movie.title.lower():
                return render_template(
                    'list_movie.html',
                    movie = movie,
                    home_url = url_for('movies_bp.home'),
                    find_movie_url = url_for('movies_bp.find_movie'),
                    browse_movies_url = url_for('movies_bp.browse_movies')
                )
        
        return render_template(
                'list_movie.html',
                movie = None,
                home_url = url_for('movies_bp.home'),
                find_movie_url = url_for('movies_bp.find_movie'),
                browse_movies_url = url_for('movies_bp.browse_movies')
            )

    return render_template(
        'find_movie.html',
        title = 'Search',
        form = form,
        home_url = url_for('movies_bp.home'),
        handler_url = url_for('movies_bp.find_movie'),
        find_movie_url = url_for('movies_bp.find_movie'),
        browse_movies_url = url_for('movies_bp.browse_movies')
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

class SearchForm(FlaskForm):
    movie_title = StringField('Movie title:')
    submit = SubmitField('Find')