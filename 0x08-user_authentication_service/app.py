#!/usr/bin/env python3
"""
Auth module
"""
from flask import Flask, jsonify, request, abort
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route('/')
def index():
    """
        Welcome message
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user():
    """
        Register a user
    """
    try:
        user = AUTH.register_user(**request.form)
        return jsonify({"email": user.email, "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """
        User login
    """
    is_valid_login = AUTH.valid_login(**request.form)
    if not (all(['email', 'password'] for key in list(request.form.keys()))
            and is_valid_login):
        abort(401)
    session_id = AUTH.create_session(request.form['email'])
    response = jsonify({
        'email': request.form['email'],
        'message': 'logged in'
    })
    response.set_cookie('session_id', session_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
