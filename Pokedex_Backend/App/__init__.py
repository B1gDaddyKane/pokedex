import os
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'pokedex.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/test')
    def test():
        return 'Test'

    from .db import db
    db.init_app(app)

    from .services import auth
    app.register_blueprint(auth.bp)

    from .services import pokemon
    app.register_blueprint(pokemon.bp)
    app.add_url_rule('/', endpoint="index")

    return app
