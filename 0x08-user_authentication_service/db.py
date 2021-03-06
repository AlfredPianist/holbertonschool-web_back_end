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


def has_keys(**kwarg_dict):
    """Checks if a kwarg dict has all properties from a determined list"""
    column_set = ['id', 'email',
                  'session_id', 'reset_token', 'hashed_password']
    return all([True if key in column_set else False
                for key in kwarg_dict.keys()])


class DB:
    """
        DB class
        create model to manage the Database
    """

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

    def find_user_by(self, **kwargs) -> User:
        """
            Return a user with specificed kwargs.
        """
        if not has_keys(**kwargs):
            raise InvalidRequestError
        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
            Updates a user.
        """
        if not has_keys(**kwargs):
            raise ValueError
        user_found = self.find_user_by(id=user_id)
        [setattr(user_found, key, value) for key, value in kwargs.items()]
        return None
