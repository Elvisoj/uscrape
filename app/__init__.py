from flask import Flask
from app.config import Config
from app.extensions import db, jwt, migrate
from app.scrapper import run_post_scrapper
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    from app.routes.scrapper import scrapper_bp
    app.register_blueprint(scrapper_bp)

    return app