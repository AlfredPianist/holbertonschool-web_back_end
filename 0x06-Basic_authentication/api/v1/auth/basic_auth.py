#!/usr/bin/env python3
""" Basic Auth module
"""
from api.v1.auth.auth import Auth
from base64 import b64decode


class BasicAuth(Auth):
    """ Basic Auth class
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> str:
        """ Returns base64 part of authorization header
        """
        if authorization_header is None or \
                type(authorization_header) is not str or \
                not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split()[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """ Decodes a base64 part of authorization header
        """
        if base64_authorization_header is None or \
                type(base64_authorization_header) is not str:
            return None
        try:
            base64_authorization_header = base64_authorization_header.encode(
                'utf-8')
            return b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """ Extracts user email and password from decoded base64 value.
        """
        if decoded_base64_authorization_header is None or \
                type(decoded_base64_authorization_header) is not str or \
                decoded_base64_authorization_header.find(":") == -1:
            return None, None
        return tuple(decoded_base64_authorization_header.split(":"))
