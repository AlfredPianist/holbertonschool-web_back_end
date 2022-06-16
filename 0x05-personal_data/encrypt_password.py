#!/usr/bin/env python3
"""Password encrypt and check module"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Returns a salted and hashed password as a byte string.
    Args:
        password: The password to be salted.
    Returns:
        The byte array hashed password.
    """
    return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks if a hashed password is valid.
    Args:
        hashed_password: The hashed password to be checked.
        password: The original password.
    Returns:
        True if valid, False otherwise.
    """
    return bcrypt.checkpw(bytes(password, 'utf-8'), hashed_password)
