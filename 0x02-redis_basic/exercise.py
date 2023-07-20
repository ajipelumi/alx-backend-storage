#!/usr/bin/env python3
""" Cache module. """
import redis
import uuid
from typing import Union


class Cache:
    """ Cache class. """

    def __init__(self):
        """ Initialize class instance. """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generate a random key, store input data in Redis using the random key
        and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
