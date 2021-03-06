#!/usr/bin/env python3
""" Module of Session auth views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /auth_session/login
    Return:
      - User login
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    try:
        user = User.search({'email': email})
    except Exception:
        user = []

    if len(user) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    if not user[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user[0].id)
    user_json = jsonify(user[0].to_json())
    cookie = getenv('SESSION_NAME')
    user_json.set_cookie(cookie, session_id)
    return user_json


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout() -> str:
    """ DELETE /auth_session/logout
    Return:
      - User logout
    """
    from api.v1.app import auth
    if not auth.destroy_session(request):
        abort(404, description="Not found")
    return jsonify({}), 200
