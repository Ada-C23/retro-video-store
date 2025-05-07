from flask import Flask
from .db import db, migrate
from .models import customer, rental, video
# Import Blueprints here
from .routes import customer_routes, video_routes, rental_routes
import os

def create_app(config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    if config:
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    app.register_blueprint(customer_routes.bp)
    app.register_blueprint(video_routes.bp)
    app.register_blueprint(rental_routes.bp)

    return app