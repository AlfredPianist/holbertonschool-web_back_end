#!/usr/bin/env python3
""" Auth module
"""
from flask import request
from typing import TypeVar, List
from os import getenv


class Auth():
    """ Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Function returning if a page requires authentication or not.
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths:
            return False
        for excluded_path in excluded_paths:
            if excluded_path[:-1] == path:
                return False
            if excluded_path.endswith("*"):
                if path.startswith(excluded_path[:-1]):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Function returning the authorization header.
        """
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """ Function returning the current user info.
        """
        return None

    def session_cookie(self, request=None):
        """ Function returning the current user info.
        """
        if request is None:
            return None
        SESSION_NAME = getenv("SESSION_NAME")
        return request.cookies.get(SESSION_NAME)
