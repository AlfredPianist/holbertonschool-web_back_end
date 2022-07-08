#!/usr/bin/env python3

"""Basic Flask app w/ Babel extension"""

from flask import Flask, render_template, request, flash, g
from flask_babel import Babel
from typing import Union

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config():
    """Configuration class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[dict, None]:
    """Returns a user dictionary"""
    try:
        login_as = int(request.args.get("login_as"))
        user = users[login_as]
    except Exception:
        user = None
    return user


@app.before_request
def before_request():
    """Operations before request"""
    user = get_user()
    g.user = user


@app.route('/')
def hello_world() -> str:
    """Renders 5-index template with Hello World"""
    return render_template("5-index.html")


@babel.localeselector
def get_locale():
    """Gets locale from a best match"""
    locale = request.args.get('locale')
    if locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
