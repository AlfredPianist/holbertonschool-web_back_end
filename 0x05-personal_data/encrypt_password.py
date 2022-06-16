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
