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

    pipeline = [
        {"$group": {
            "_id": "$ip",
            "count": {"$sum": 1}
        }},
        {"$sort": {"count": -1}}
    ]

    ip_counts_sorted = list(collection.aggregate(pipeline))
    sorted_ips = [ip_count['_id'] for ip_count in ip_counts_sorted]

    print(f"{number_of_docs} logs")
    print("Methods:")
    for i in range(5):
        print(f"\tmethod {methods[i]}: {methods_count[i]}")
    print(f"{status_check} status check")
    print("IPs:")
    for ip in sorted_ips[:10]:
        print('\t' + ip)
