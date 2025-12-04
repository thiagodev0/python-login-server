from flask import Flask
from app import db
from app.routes import main_bp
from app.auth import auth_bp
from config import Config
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
