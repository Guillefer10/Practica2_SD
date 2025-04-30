from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from app import db
from models import Record

db_bp = Blueprint('db_bp', __name__)

@db_bp.route('/', methods=['GET'])
def test_db():
    # Si pedimos invalid=true, levantamos excepción a propósito
    if request.args.get('invalid') == 'true':
        try:
            # Simular fallo de transacción
            db.session.execute('SELECT * FROM no_existe')
        except SQLAlchemyError as e:
            return jsonify({ "error": "Fallo de acceso a BD", "detalle": str(e) }), 500

    # Caso feliz: creamos/consultamos un registro trivial
    try:
        # Creamos una tabla y un registro de ejemplo
        db.create_all()
        if Record.query.count() == 0:
            sample = Record(name='ejemplo', value='42')
            db.session.add(sample)
            db.session.commit()
        recs = [r.to_dict() for r in Record.query.all()]
        return jsonify({ "records": recs }), 200
    except SQLAlchemyError as e:
        return jsonify({ "error": "Error inesperado en BD", "detalle": str(e) }), 500
