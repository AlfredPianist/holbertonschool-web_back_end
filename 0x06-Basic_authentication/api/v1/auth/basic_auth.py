#!/usr/bin/env python3
""" Basic Auth module
"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """ Basic Auth class
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> str:
        """ Returns base64 part of authorization header
        """
        if authorization_header is None or \
                not isinstance(authorization_header, str) or \
                not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split()[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """ Decodes a base64 part of authorization header
        """
        if base64_authorization_header is None or \
                not isinstance(base64_authorization_header, str):
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
                not isinstance(decoded_base64_authorization_header, str) or \
                decoded_base64_authorization_header.find(":") == -1:
            return None, None
        return tuple(decoded_base64_authorization_header.split(":", 1))

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str
                                     ) -> TypeVar('User'):
        """ Returns User instance based on email and password.
        """
        if user_email is None or not isinstance(user_email, str) or \
                user_pwd is None or not isinstance(user_email, str):
            return None

        try:
            users = User.search({"email": user_email})
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns User instance based on email and password.
        """
        auth_header = self.authorization_header(request)
        base64_auth_header = self.extract_base64_authorization_header(
            auth_header)
        decoded_base64_auth_header = self.decode_base64_authorization_header(
            base64_auth_header)
        user_email, user_pwd = self.extract_user_credentials(
            decoded_base64_auth_header)
        return self.user_object_from_credentials(user_email, user_pwd)
