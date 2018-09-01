from flask import Flask

from . import views


def create_app():
    app = Flask(__name__)
    views.configure(app)
    return app
