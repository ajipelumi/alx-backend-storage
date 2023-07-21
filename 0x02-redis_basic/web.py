#!/usr/bin/env python3
""" Cache module. """
import redis
import requests


def get_page(url: str) -> str:
    """
    Get the HTML content of a particular URL and return it.
    """
    r = requests.get(url)
    html = r.text

    redis_client = redis.Redis()
    redis_client.setex(url, 10, html)

    count = "count:" + url
    redis_client.incr(count)

    return html
