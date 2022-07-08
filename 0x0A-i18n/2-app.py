#!/usr/bin/env python3

"""Basic Flask app w/ Babel extension"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config():
    """Configuration class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def hello_world() -> str:
    """Renders 2-index template with Hello World"""
    return render_template("2-index.html")


@babel.localeselector
def get_locale():
    """Gets locale from a best match"""
    return request.accept_languages.best_match(app.config.LANGUAGES)


if __name__ == "__main__":
    app.run()
