#!/usr/bin/env python3
"""Module listing all schools with a specific topic"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """Lists all school with a specific topic"""
    return mongo_collection.find({"topics": topic})
