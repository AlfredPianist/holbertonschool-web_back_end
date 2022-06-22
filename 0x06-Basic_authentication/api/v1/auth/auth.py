#!/usr/bin/env python3
""" Auth module
"""
from flask import request
from datetime import datetime
from typing import TypeVar, List, Iterable
from os import path
import json
import uuid


TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S"
DATA = {}


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
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Function returning the current user info.
        """
        return None
