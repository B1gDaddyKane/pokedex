import pyodbc

from flask import g


def get_db():
    if 'db' not in g:
        print(pyodbc.drivers())
        driver = pyodbc.drivers()[-1]
        g.db = pyodbc.connect(
            f'Driver={driver};'
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
