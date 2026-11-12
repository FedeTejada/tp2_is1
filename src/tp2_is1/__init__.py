import os
from config import config
from extensions import db
from flask import Flask

def create_app(enviroment='development'):
    app = Flask(__name__,instance_relative_config=True)

    #ensures that the instance folder exist
    os.makedirs(app.instance_path, exist_ok=True)

    #Initialize extensions

    app.config.from_object(config[enviroment])
    print(app.config.get("SQLALCHEMY_DATABASE_URI"))
    db.init_app(app)

    #Routes
    from .routes.users import user_bp

    app.register_blueprint(user_bp)

    return app


