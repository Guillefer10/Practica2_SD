from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///practica2.db'
db = SQLAlchemy(app)

# Importamos blueprints
from blueprints.file_bp import file_bp
from blueprints.db_bp import db_bp
from blueprints.poke_bp import poke_bp

app.register_blueprint(file_bp, url_prefix='/file-test')
app.register_blueprint(db_bp, url_prefix='/db-test')
app.register_blueprint(poke_bp, url_prefix='/poke-test')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
