#!/usr/bin/env python3
"""Module for the Redis NoSQL data storage"""
from typing import Union
import redis
from uuid import uuid4


class Cache:
    """class Cache : for storing data in a Redis data storage"""
    def __init__(self):
        """Initialize a Cache instance using Redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in a Redis data storage and returns the key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
