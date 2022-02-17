from flask import (
    Blueprint, g, redirect, request, json
)
from werkzeug.exceptions import abort

from App.services.auth import login_required
from App.db.db import get_db

bp = Blueprint('pokemon', __name__)


@bp.route('/pokemon/<int:id>', methods=['GET'])
def get_pokemon(id):
    pokemon = get_db().execute(
        'SELECT pokeid, pokename, firsttype, secondtype'
        ' FROM pokemon'
        ' WHERE pokeid = ?',
        ([id])
    ).fetchone()
    print(pokemon)
    if pokemon is None:
        abort(404, f"Pokemon id: {id} does not exist")

    return json.dumps(list(pokemon))


# @bp.route('/create', methods=['GET'])
# def create_pokemon():
#     db = get_db()
#     with open('C:/Users/jcj.it-minds.dk/it-minds/pokedex/Pokedex_Backend/App/services/pokedex.json', encoding="utf8") as data_file:
#         data = json.load(data_file)
#         for p in data:
#             if len(p['type']) < 2:
#                 p['type'].append(None)
#             try:
#                 db.execute(
#                     "INSERT INTO pokemon (pokeid, pokename, firsttype, secondtype) VALUES (?, ?, ?, ?)", (
#                         p['id'], p['name']['english'], p['type'][0], p['type'][1]),
#                 )
#                 print(p['name']['english'])
#             except db.IntegrityError:
#                 return f"Pokemon is already registered."
#         db.commit()
#     return "Done"
