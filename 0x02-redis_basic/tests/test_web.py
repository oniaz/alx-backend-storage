import unittest
import time
import redis
from web import get_page

class TestGetPage(unittest.TestCase):
    def setUp(self):
        # Connect to Redis
        self.r = redis.Redis()

    def test_caching_and_counter(self):
        # Call get_page multiple times with the same URL
        url = "http://google.com"
        for _ in range(5):
            # Get the current count for the URL from Redis
            initial_count = int(self.r.get(f"count:{url}") or 0)

            # Call get_page
            response = get_page(url)

            # Assert that the response is correct
            self.assertIn("google", response.lower())

            # Get the new count for the URL from Redis
            new_count = int(self.r.get(f"count:{url}"))

            # Assert that the count has incremented
            self.assertEqual(new_count, initial_count + 1)

        # Wait for 10 seconds (cache expiration time)
        time.sleep(10)

        # Call get_page again
        response = get_page(url)

        # Assert that the count for the URL is 1 after expiration
        new_count = int(self.r.get(f"count:{url}"))
        self.assertEqual(new_count, 1)

    def test_annotations(self):
        # Check if the function annotations are correct
        self.assertEqual(get_page.__annotations__, {'url': str, 'return': str})

if __name__ == "__main__":
    unittest.main()
