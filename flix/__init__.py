# initisalise flask app

from flask import Flask

import flix.adapters.repository as repo
from flix.adapters.memory_repository import MemoryRepository

def create_app(test_config = None):
    app = Flask(__name__)

    app.config.from_object("config.Config")
    data_path = "flix/datafiles/Data1000Movies.csv"

    if test_config is not None:
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    repo.repo_instance = MemoryRepository()
    repo.repo_instance.populate(data_path)

    with app.app_context():
        #insert blueprints
        from .movies import movies
        app.register_blueprint(movies.movies_blueprint)

        from .authentication import authentication
        app.register_blueprint(authentication.authentication_blueprint)

    return app