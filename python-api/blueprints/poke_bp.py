import requests
from flask import Blueprint, request, jsonify
from requests.exceptions import RequestException

poke_bp = Blueprint('poke_bp', __name__)

@poke_bp.route('/', methods=['GET'])
def test_poke():
    name = request.args.get('name', 'pikachu')
    url = f'https://pokeapi.co/api/v2/pokemon/{name.lower()}'
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        # Devolvemos solo campos clave
        result = {
            "name": data['name'],
            "height": data['height'],
            "weight": data['weight'],
            "types": [t['type']['name'] for t in data['types']]
        }
        return jsonify(result), 200
    except RequestException as e:
        return jsonify({ "error": "Fallo en llamada a PokeAPI", "detalle": str(e) }), 502
