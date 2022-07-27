#!/usr/bin/env python3
"""Module listing all documents"""
import pymongo


def list_all(mongo_collection):
    """List all documents in a collection"""
    return mongo_collection.find() if mongo_collection is not None else []
