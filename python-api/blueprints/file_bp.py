from flask import Blueprint, request, jsonify

file_bp = Blueprint('file_bp', __name__)

@file_bp.route('/', methods=['GET'])
def test_file():
    path = request.args.get('path', 'data.txt')
    try:
        with open(path, 'r') as f:
            content = f.read()
        return jsonify({ "content": content }), 200
    except IOError as e:
        return jsonify({ "error": "Fallo al leer archivo", "detalle": str(e) }), 500
