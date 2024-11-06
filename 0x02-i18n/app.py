#!/usr/bin/env python3
"""internationalization support."""
import pytz
from typing import Union, Dict
from flask_babel import Babel, format_datetime
from flask import Flask, render_template, request, g


class Config:
    """Configuration class for Flask Babel settings."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
    Retrieves a user based on a user ID from query parameters.
    Returns a user dictionary if found, otherwise None.
    """
    id = request.args.get('login_as', '')
    if id:
        return users.get(int(id), None)
    return None


@app.before_request
def before_request() -> None:
    """
    Executes routines before each request is processed.
    Sets the global user object based on the login ID.
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match for the user's locale.
    Order of preference: URL parameters, user settings, request headers,
    and finally default locale.
    """
    query = request.query_string.decode('utf-8').split('&')
    qt = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        query,
    ))
    local = qt.get('locale', '')
    if local in app.config["LANGUAGES"]:
        return local
    ud = getattr(g, 'user', None)
    if ud and ud['locale'] in app.config["LANGUAGES"]:
        return ud['locale']
    hl = request.headers.get('locale', '')
    if hl in app.config["LANGUAGES"]:
        return hl
    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone() -> str:
    """
    Determines the best match for the user's timezone.
    Order of preference: URL parameters, user settings, and finally default timezone.
    """
    tz = request.args.get('timezone', '').strip()
    if not tz and g.user:
        tz = g.user['timezone']
    try:
        return pytz.timezone(tz).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def get_index() -> str:
    """
    Renders the home/index page.
    Sets the current time formatted according to the user's locale and timezone.
    """
    g.time = format_datetime()
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
