#!/usr/bin/env python3
"""Module for the Redis NoSQL data storage"""
from typing import Union, Callable
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

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        """Retrieve data from the cache using the specified key"""
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """Retrieve a string from the cache using the specified key"""
        return str(self._redis.get(key))

    def get_int(self, key: str) -> int:
        """Retrieve an integer from the cache using the specified key"""
        return int(self._redis.get(key))
