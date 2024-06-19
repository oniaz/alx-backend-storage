#!/usr/bin/env python3
""" Find + Query"""


def schools_by_topic(mongo_collection, topic):
    """Returns a list of school having a specific topic"""
    documents = mongo_collection.find(
        {"topics": {"$regex": topic}}
    )
    return list(documents)
