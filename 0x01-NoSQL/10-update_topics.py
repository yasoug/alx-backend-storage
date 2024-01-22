#!/usr/bin/env python3
"""Script for the function update_topics"""


def update_topics(mongo_collection, name, topics):
    """Funct that changes all topics of a school document based on the name"""
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
