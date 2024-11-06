#!/usr/bin/env python3
"""
This module configures Flask and Babel for a basic multilingual application.
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """ Basic configuration for the Flask application using Babel. """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """ Displays the home page. """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
