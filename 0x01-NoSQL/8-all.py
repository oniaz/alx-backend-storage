#!/usr/bin/env python3
"""Listing all documents in a mongodb collection"""


def list_all(mongo_collection):
    """Listing all documents in a mongodb collection"""
    # cursor = mongo_collection.find()
    # return [document for document in cursor]
    # this works too
    return list(mongo_collection.find())
