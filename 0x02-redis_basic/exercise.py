#!/usr/bin/env python3
"""Redis Basics Exercise"""

import functools
import redis
from typing import Union, Optional, Callable
import uuid


def count_calls(method: Callable) -> Callable:
    """Decorator fucntion that replaces the original store method with a
        wrapper function that increments a counter in a Redis database each
        time the store method is called.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function that replaces the original method and counts the
            number of times it was called."""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache():
    """Cache class"""
    def __init__(self):
        """Initialize a new Cache object"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores input data to Redis for a randomly generated key using UUID
            and returns the key
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float]:
        """Retrieves data from redis and converts the it back to the desired
            format"""
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Parametrize Cache.get with str() conversion function"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """Parametrize Cache.get with int() conversion function"""
        return self.get(key, int)
