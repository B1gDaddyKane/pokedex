from flask import (
    Blueprint, g, redirect, request, json
)
from werkzeug.exceptions import abort

from App.services.auth import login_required
from App.db.db import get_db

bp = Blueprint('pokemon', __name__)


@bp.route('/pokemon/<int:id>', methods='GET')
def get_pokemon(id):
    pokemon = get_db().execute(
        "SELECT pokeid, pokename, poketype FROM pokemon p WHERE id = ?", (id)
    ).fetchone()

    if pokemon is None:
        abort(404, f"Pokemon id {id} does not exist")

    return json.dumps(pokemon)
