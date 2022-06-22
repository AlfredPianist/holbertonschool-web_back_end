#!/usr/bin/env python3
""" Basic Auth module
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Basic Auth class
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ Returns base64 part of authorization header
        """
        if authorization_header is None or \
                type(authorization_header) is not str or \
                not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split()[1]
