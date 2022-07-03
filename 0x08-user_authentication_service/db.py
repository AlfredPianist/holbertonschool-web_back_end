#!/usr/bin/env python3
"""
Implement User class in DB
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import sessionmaker
from user import Base
from user import User
import re

USER_COLUMN_NAMES_SET = {'email', 'id', 'session_id',
                         'reset_token', 'hashed_password'}


class DB:
    """
        DB class
        create model to manage the Database
    """

    @staticmethod
    def has_keys(kwarg_dict, column_set):
        """Checks if a kwarg dict has all properties from a determined set"""
        if set(kwarg_dict.keys()).issubset(column_set):
            return True
        return False

    def __init__(self):
        """
            Constructor
            create the object BD
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """
            Create if not exists a db session
            Return the session
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
            Create an User and insert in Database
            Return the new User
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs: dict) -> User:
        """
            Return a user with specificed kwargs.
        """
        if not DB.has_keys(kwargs, USER_COLUMN_NAMES_SET):
            raise InvalidRequestError
        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound
        return user
