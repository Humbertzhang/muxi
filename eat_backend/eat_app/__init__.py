import os
from flask import Flask
from flask_moment import Moment
from flask_debugtoolbar import DebugToolbarExtension

toolbar = DebugToolbarExtension()

def create_app():
    app = Flask(__name__)
    return app

app = create_app()
