#!/usr/bin/env python3
"""
    Exercise file
"""
import redis
import uuid
import sys
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Counts the calls to the Redis cache"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper for decorator"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Basic Redis cache class"""

    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis cache"""
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Gets data from Redis cache"""
        return fn(self._redis.get(key)) if fn else self._redis.get(key)

    def get_str(value: bytes) -> str:
        """Converts bytes value to string"""
        return value.decode('utf-8')

    def get_int(value: bytes) -> int:
        """Converts bytes value to int"""
        return int.from_bytes(value, sys.byteorder)
