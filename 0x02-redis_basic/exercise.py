#!/usr/bin/env python3
""" Cache module. """
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Count the number of times a method is called.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function. """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Store the history of inputs and outputs for a particular function.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function. """
        input = str(args)
        input_key = method.__qualname__ + ":inputs"
        self._redis.rpush(input_key, input)

        output = str(method(self, *args, **kwargs))
        output_key = method.__qualname__ + ":outputs"
        self._redis.rpush(output_key, output)

        return output

    return wrapper


class Cache:
    """ Cache class. """

    def __init__(self):
        """ Initialize class instance. """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generate a random key, store input data in Redis using the random key
        and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] =
            None) -> Union[str, bytes, int, float]:
        """
        Convert data back to desired format.
        """
        data = self._redis.get(key)
        if data is None:
            return None

        if fn is not None:
            data = fn(data)

        return data

    def get_str(self, key: str) -> str:
        """ Get a string value from Redis. """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """ Get an integer value from Redis. """
        return self.get(key, int)


def replay(method: Callable):
    """
    Display the history of calls of a particular function.
    """
    r = redis.Redis()
    key = method.__qualname__
    count = r.get(key).decode('utf-8')
    inputs = r.lrange(key + ":inputs", 0, -1)
    outputs = r.lrange(key + ":outputs", 0, -1)

    print("{} was called {} times:".format(key, count))

    for input, output in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(key, input.decode('utf-8'),
                                     output.decode('utf-8')))
