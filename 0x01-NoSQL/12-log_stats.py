#!/usr/bin/env python3
"""This script provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    logs = client.logs.nginx

    print(logs.count_documents({}), "logs")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        rst = logs.count_documents({'method': method})
        print(f'\tmethod {method}: {rst}')
    st = logs.count_documents({'path': '/status', 'method': "GET"})
    print(f'{st} status check')
