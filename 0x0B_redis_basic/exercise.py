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
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper for decorator"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Stores the history of inputs and outputs from a function"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper for decorator"""
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"
        input = str(args)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(input_key, input)
        self._redis.rpush(output_key, output)
        return output
    return wrapper


def replay(fn: Callable):
    """Displays call history of a function"""
    cache = redis.Redis()
    fn_name = fn.__qualname__
    fn_call_count = cache.get(fn_name).decode('utf-8')
    print(f"{fn_name} was called {fn_call_count} times:")

    input_key = fn_name + ":inputs"
    output_key = fn_name + ":outputs"
    inputs = cache.lrange(input_key, 0, fn_call_count)
    outputs = cache.lrange(output_key, 0, fn_call_count)
    for inp, out in zip(inputs, outputs):
        print(f"{fn_name}(*{inp.decode('utf-8')}) -> {out.decode('utf-8')}")


class Cache:
    """Basic Redis cache class"""

    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
