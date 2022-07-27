#!/usr/bin/env python3
"""Module providing stats about Nginx logs"""
from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017")
nginx_collection = client.logs.nginx


def count(filter: dict = {}) -> int:
    """Count the number of elements of the collection given a dict filter"""
    return nginx_collection.count_documents(filter)


if __name__ == "__main__":
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print('{} logs'.format(count()))
    print('Methods:')
    for method in methods:
        print('\tmethod {}: {}'.format(method, count({"method": method})))
    print('{} status check'.format(count(
        {"method": "GET", "path": "/status"}
    )))
    top_ips = nginx_collection.aggregate([
        {"$group": {
            "_id": "$ip",
            "count": {"$sum": 1}
        }},
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ])
    print("IPs:")
    for top_ip in top_ips:
        print(f'\t{top_ip.get("ip")}: {top_ip.get("count")}')
