#!/usr/bin/env python3
""" Session Exp Auth module
"""
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """ Session Expired Auth class
    """

    def __init__(self):
        """ Initialize a SessionExpAuth instance
        """
        try:
            self.session_duration = int(getenv("SESSION_DURATION"))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """ Creates session ID for user_id
        """
        session_id = super().create_session()
        if session_id is None:
            return None
        session_id_val = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_id_val
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Returns a user_id based on a session_id
        """
        if session_id is None or \
                session_id not in self.user_id_by_session_id.keys():
            return None
        session_dict = self.user_id_by_session_id.get(session_id)
        user_id = session_dict.get('user_id')
        if self.session_duration <= 0:
            return user_id
        if 'created_at' not in session_dict.keys():
            return None
        session_delta = session_dict.get('created_at') + \
            timedelta(seconds=self.session_duration)
        if session_delta < datetime.now():
            return None
        return user_id
