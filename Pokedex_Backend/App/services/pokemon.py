from flask import (
    Blueprint, json
)

from werkzeug.exceptions import abort

from App.db.db import get_db, get_blobclient


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

    image = 'https://blobbyblobblob.blob.core.windows.net/pokeimages/images/{}.png'.format(
        f'{id:03}')
    return json_response(list(pokemon), image)


def json_response(data, image, status=200):
    res = {'pokeID': data[0],
           'pokename': data[1],
           'type': [data[2], data[3]],
           'HP': data[4],
           'Attack': data[5],
           'Defense': data[6],
           'Sp. Attack':  data[7],
           'Sp. Defense': data[8],
           'Speed': data[9],
           'image': image}
    return (json.dumps(res, sort_keys=False),
            status, {'content-type': 'application/json'})
