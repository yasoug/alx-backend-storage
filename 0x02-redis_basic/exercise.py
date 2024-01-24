#!/usr/bin/env python3
"""Module for the Redis NoSQL data storage"""
from typing import Union, Callable, Any
import redis
from uuid import uuid4
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Track the number of calls made to a class method"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
        """It returns the given method after incrementing its call counter"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Tracks the call details of a method in a Cache class"""
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
        """returns the method's output after storing its inputs and output"""
        input_data = str(args)
        self._redis.rpush(input_key, input_data)
        output_data = method(self, *args, **kwargs)
        self._redis.rpush(output_key, output_data)
        return output_data

    return wrapper


class Cache:
    """class Cache : for storing data in a Redis data storage"""
    def __init__(self):
        """Initialize a Cache instance using Redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
