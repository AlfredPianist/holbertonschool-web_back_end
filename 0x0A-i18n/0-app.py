#!/usr/bin/env python3

"""Basic Flask app"""

from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def hello_world() -> str:
    """Renders 0-index template with Hello World"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
