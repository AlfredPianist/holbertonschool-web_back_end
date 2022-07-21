#!/usr/bin/env python3
"""
    Web file
"""
import redis
import requests
from typing import Callable
from functools import wraps

cache = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """Counts the number of requests to a page and stores it in a Redis DB"""
    @wraps(method)
    def wrapper(url):
        """Wrapper for decorator"""
        cached_resp_key = f'cached:{url}'
        cached_resp = cache.get(cached_resp_key)
        if cached_resp:
            return cached_resp.decode('utf-8')

        resp = method(url)
        cache.incr(f'count:{url}')
        cache.setex(cached_resp_key, 10, resp)
        return resp
    return wrapper


@count_requests
def get_page(url: str) -> str:
    """Gets a page using requests"""
    resp = requests.get(url)
    return resp.text
