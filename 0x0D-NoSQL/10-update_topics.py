#!/usr/bin/env python3
"""Module updating a document"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """Updates a document in a collection"""
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}},
    )
