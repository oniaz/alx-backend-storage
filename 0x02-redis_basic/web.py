#!/usr/bin/env python3
"""Redis Basics Exercise"""
import functools
import redis
import requests
from typing import Callable


def count_requests(method: Callable) -> Callable:
    """Decorator that increments a temporary counter in Redis, keeping track of
    how many times each URL is requested. The counter lasts for 10 seconds"""
    def wrapper(url):
        """Wrapper function that replaces the original method and counts the
        number of times the URL passed as argument has been requested"""
        if url:
            key = "count:" + url
            r = redis.Redis(host='localhost', port=6379, db=0)
            r.incr(key)
            r.expire(key, 10)
        return method(url)
    return wrapper


@count_requests
def get_page(url: str) -> str:
    """Returns the HTML content of a URL"""
    response = requests.get(url).text
    return response
