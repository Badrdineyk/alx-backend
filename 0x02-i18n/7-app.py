#!/usr/bin/env python3
"""
Initialization of a Flask application with Babel
for text localization
and timezone management.
"""
from flask import Flask, request, g, render_template
from flask_babel import Babel, gettext
import pytz
from pytz.exceptions import UnknownTimeZoneError


app = Flask(__name__)
babel = Babel(app)


app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Retrieves the user from the 'login_as' URL parameter.
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """
    Executes before each request to set the global user.
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    Selects the appropriate locale based on:
    1. URL parameters
    2. User settings
    3. Default locale
    """
    locale = request.args.get('locale')
    if locale and locale in ['en', 'fr']:
        return locale
    if g.user and g.user['locale'] in ['en', 'fr']:
        return g.user['locale']
    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone():
    """
    Selects the appropriate timezone based on:
    1. URL parameters
    2. User settings
    3. Default timezone
    """
    tz_name = request.args.get('timezone')
    if tz_name:
        try:
            pytz.timezone(tz_name)
            return tz_name
        except UnknownTimeZoneError:
            pass
    if g.user and g.user['timezone']:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except UnknownTimeZoneError:
            pass
    return 'UTC'


app.jinja_env.globals['get_locale'] = get_locale
app.jinja_env.globals['get_timezone'] = get_timezone


@app.route('/')
def index():
    """
    Displays the home page.
    """
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run(debug=True)
