
import click
from flask import current_app, g
from flask.cli import with_appcontext
from flask_mysqldb import MySQL
from abc import ABC, abstractmethod


class DB(ABC):

    @abstractmethod
    def execute(self, query, params):
        pass 

    @abstractmethod
    def commit(self):
        pass 

    @abstractmethod
    def close(self):
        pass 


class MYSQL_DB(DB):
    def __init__(self):
        self.db = MySQL()

    def execute(self, query, params=None):
        cur = self.db.connection.cursor()
        return cur.execute(query, params)

    def commit(self):
        self.db.connection.commit()

    def close(self):
        self.db.connection.close()


def get_db():
    if 'db' not in g:
        g.db = MYSQL_DB()
        g.db.init_app(current_app)

    return g.db

def init_db():
    db = get_db()

#    with current_app.open_resource('schema.sql') as f:
#        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    pass
    init_db()
    click.echo('Initialized the database.')

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
