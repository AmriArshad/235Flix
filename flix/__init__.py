# initisalise flask app

from flask import Flask

import flix.adapters.repository as repo
from flix.adapters.memory_repository import MemoryRepository

def create_app():
    app = Flask(__name__)

    app.config.from_object("config.Config")

    with app.app_context():
        #insert blueprints
        from .movies import movies
        app.register_blueprint(movies.movies_blueprint)

        from .authentication import authentication
        app.register_blueprint(authentication.authentication_blueprint)

        repo.repo_instance = MemoryRepository()
        repo.repo_instance.populate("flix/datafiles/Data1000Movies.csv")

    return app