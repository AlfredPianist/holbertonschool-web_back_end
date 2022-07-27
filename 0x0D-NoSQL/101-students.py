#!/usr/bin/env python3
"""Module listing all schools with a specific topic"""
import pymongo


def top_students(mongo_collection):
    """Lists all school with a specific topic"""
    return mongo_collection.aggregate([
        {"$project": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ])
