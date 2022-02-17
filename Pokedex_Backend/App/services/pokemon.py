from importlib.metadata import requires
from pstats import SortKey
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
        'SELECT *'
        ' FROM pokemon'
        ' WHERE pokeid = ?',
        ([id])
    ).fetchone()
    if pokemon is None:
        abort(404, f"Pokemon id: {id} does not exist")
    print(list(pokemon)[0])

    return json_response(list(pokemon))


def json_response(data, status=200):
    return (json.dumps({'pokeID': data[0], 'pokename': data[1],
                        'type': [data[2], data[3]], 'HP': data[4],
                        'Attack': data[5], 'Defense': data[6], 'Sp. Attack':  data[7],
                        'Sp. Defense': data[8], 'Speed': data[9]}, sort_keys=False),
            status, {'content-type': 'application/json'}, )


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
#                     "INSERT INTO pokemon (pokeid, pokename, firsttype, secondtype, hp, atk, def, sp_atk, sp_def, speed) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
#                         p['id'], p['name']['english'], p['type'][0], p['type'][1],
#                         p['base']['HP'], p['base']['Attack'], p['base']['Defense'],
#                         p['base']['Sp. Attack'], p['base']['Sp. Defense'], p['base']['Speed']),
#                 )
#                 print(p['name']['english'])
#             except db.IntegrityError:
#                 return f"Pokemon is already registered."
#         db.commit()
#     return "Done"
