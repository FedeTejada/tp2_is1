import os

from flask import Flask, redirect, url_for

from tp2_is1.config import config
from tp2_is1.extensions import db


def create_app(enviroment='development'):
    app = Flask(__name__,instance_relative_config=True)

    #ensures that the instance folder exist
    os.makedirs(app.instance_path, exist_ok=True)

    #Initialize extensions

    app.config.from_object(config[enviroment])
    print(app.config.get("SQLALCHEMY_DATABASE_URI"))
    db.init_app(app)

    from tp2_is1 import models  # noqa: F401  (registra los modelos en el metadata)
    with app.app_context():
        db.create_all()  # provisorio hasta tener migraciones Alembic
        if app.config.get('SEED_DEMO_DATA'):
            from tp2_is1.services.seed import seed_demo_data
            seed_demo_data()

    #Routes
    from .routes.auth import auth_bp
    from .routes.questions import question_bp
    from .routes.users import user_bp
    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(question_bp)

    @app.get('/')
    def home():
        return redirect(url_for('questions.index'))
    return app


