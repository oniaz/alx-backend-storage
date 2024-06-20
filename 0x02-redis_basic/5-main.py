#!/usr/bin/env python3
"""
Main file
"""
import redis
import time

r = redis.Redis()
get_page = __import__('web').get_page

url = 'http://slowwly.robertomurray.co.uk'
content = get_page(url)
# print(content)

count = r.get(f"count:{url}")
print(int(count))

time.sleep(10)

count = r.get(f"count:{url}")
print(count)
# r.set(f"count:{url}", 0)
