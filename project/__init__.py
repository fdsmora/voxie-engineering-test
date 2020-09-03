import os

from flask import Flask, url_for

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
#        DATABASE=os.path.join(app.instance_path, 'voxie.db'),
        MYSQL_HOST = '172.18.0.2',
        MYSQL_DATABASE = "contacts",
        MYSQL_USER = "contacts",
        MYSQL_PASSWORD = "secret",
        MYSQL_PORT = "3306",
        MYSQL_DB = "hola"
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    # a simple page that says hello
    @app.route('/hello/')
    def hello():
        return 'Hello, World!'

    from . import import_team
    app.register_blueprint(import_team.bp)

    from . import view
    app.register_blueprint(view.bp)

    from . import team_detail 
    app.register_blueprint(team_detail.bp)

    from . import contact_detail 
    app.register_blueprint(contact_detail.bp)

    from . import search_contacts 
    app.register_blueprint(search_contacts.bp)

    return app
