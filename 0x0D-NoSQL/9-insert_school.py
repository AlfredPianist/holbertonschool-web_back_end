#!/usr/bin/env python3
"""Module listing all documents"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """Insert a document in a collection"""
    return mongo_collection.insert_one(kwargs)
