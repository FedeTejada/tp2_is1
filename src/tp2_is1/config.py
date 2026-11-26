import os


class Config:
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'development-only')

    # Proveedor LLM para el patrón Strategy: 'openai' | 'gemini'
    LLM_PROVIDER = os.getenv('LLM_PROVIDER', 'openai')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')

    # Carga usuarios y categorías de prueba si la base está vacía
    SEED_DEMO_DATA = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SEED_DEMO_DATA = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}
