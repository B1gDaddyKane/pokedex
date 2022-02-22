import pyodbc

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = pyodbc.connect(
            r'Driver={SQL Server Native Client 11.0};'
            r'Server=play-server.database.windows.net;'
            r'Database=pokedex_db;'
            r'Trusted_Connection=no;'
            r'UID=TestAdmin;'
            r'PWD=Cfd59ahg'
        )

    return g.db.cursor()


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
