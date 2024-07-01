from flask import Flask
from flask_bcrypt import Bcrypt
from mongoengine import connect
from .config import Config

bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize MongoDB
    connect(
        db=app.config['MONGO_DB_NAME'],
        host=app.config['MONGO_URI']
    )

    # Initialize Bcrypt
    bcrypt.init_app(app)

    # Register blueprints
    from .user_routes import main
    app.register_blueprint(main)

    return app
