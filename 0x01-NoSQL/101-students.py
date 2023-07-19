#!/usr/bin/env python3
""" Returns all students sorted by average score. """


def top_students(mongo_collection):
    """"""
    return mongo_collection.aggregate([
        {
            "$unwind": "$topics"
        },
        {
            "$group": {
                "_id": "$_id",
                "name": {"$first": "$name"},
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ])
