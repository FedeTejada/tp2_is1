from flask import Flask


def create_app():
    app = Flask(__name__)
    print("Hello from tp2-is1!")
    return app
    
