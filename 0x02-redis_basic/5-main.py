#!/usr/bin/env python3
"""
Main file
"""
import redis

r = redis.Redis(host='localhost', port=6379, db=0)
get_page = __import__('web').get_page

url = 'http://slowwly.robertomurray.co.uk'
content = get_page(url)
print(content)

count = r.get(f"count:{url}")
print(int(count))

# r.set(f"count:{url}", 0)
