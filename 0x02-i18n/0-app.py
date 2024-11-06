#!/usr/bin/env python3
"""
This module contains a basic Flask application.
It defines a single route that displays a welcome message.
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """ Displays the home page with a title and a message. """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
