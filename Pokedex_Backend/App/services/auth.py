import functools
import re

from flask import (
    Blueprint, flash, g, redirect, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from App.db.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods='POST')
def register():
    username = request.form['username']
    password = request.form['password']
    db = get_db()
    error = None

    if not username:
        error = 'Please fill out username'
    elif not password:
        error = 'Please fill out password'

    if error is None:
        try:
            db.execute(
                "INSERT INTO trainer (trainername, pass) VALUES (?, ?)",
                (username, generate_password_hash(password)),
            )
            db.commit()
        except db.IntegrityError:
            error = f"Trainer {username} is already registered."
        else:
            return "Trainer successfully registered"
    flash(error)


@bp.route('/login', methods='POST')
def login():
    username = request.form['username']
    password = request.form['password']
    db = get_db()
    error = None
    trainer = db.execute(
        "SELECT * FROM trainer WHERE trainername = ?", (username)
    ).fetchone()

    if trainer is None:
        error = 'Incorrect trainername.'
    elif not check_password_hash(trainer['pass'], password):
        error = 'Incorrect password.'

    if error is None:
        session.clear()
        session['user_id'] = trainer['id']
        return redirect(url_for('index'))
    flash(error)


@bp.before_app_request
def load_logged_in_trainer():
    trainer_id = session.get('user_id')

    if trainer_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            "SELECT * FROM trainer WHERE id = ?", (trainer_id)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(call):
    @functools.wraps(call)
    def wrapped_call(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return call(**kwargs)

    return wrapped_call
