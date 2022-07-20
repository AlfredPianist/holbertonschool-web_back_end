#!/usr/bin/env python3
"""
    Exercise file
"""
import redis
import uuid
from typing import Union


class Cache:
    """Basic Redis cache class"""

    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis cache"""
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id
