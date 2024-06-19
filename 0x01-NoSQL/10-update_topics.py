#!/usr/bin/env python3
""" Updating documents"""


def update_topics(mongo_collection, name, topics):
    """Changes the topics field of all documents in a collection based on the
    name field."""
    mongo_collection.update_many(
        {"name": name},
        {'$set': {"topics": topics}}
    )
