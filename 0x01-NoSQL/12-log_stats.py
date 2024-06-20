#!/usr/bin/env python3
""" Provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    number_of_docs = collection.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    methods_count = [
        collection.count_documents({"method": method}) for method in methods]

    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"})

    print(f"{number_of_docs} logs")
    print("Methods:")
    for i in range(5):
        print(f"\tmethod {methods[i]}: {methods_count[i]}")
    print(f"{status_check} status check")
