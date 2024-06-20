#!/usr/bin/env python3
"""Redis Basics Exercise"""

import redis
import uuid
from typing import Union


class Cache():
    """Cache class"""
    def __init__(self):
        """Initialize a new Cache object"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores input data to Redis for a randomly generated key using UUID
            and returns the key
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
