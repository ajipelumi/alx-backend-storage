#!/usr/bin/env python3
""" Provides some stats about Nginx logs stored in MongoDB. """
from pymongo import MongoClient

if __name__ == "__main__":
    """ Provides some stats about Nginx logs stored in MongoDB. """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    print("{} logs".format(logs_collection.count_documents({})))
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print("\tmethod {}: {}"
              .format(method,
                      logs_collection.count_documents({"method": method})))

    print("{} status check".format(
          logs_collection.count_documents({"method": "GET",
                                          "path": "/status"})))

    print("IPs:")
    ips = logs_collection.aggregate([
        {
            "$match": {}
        },
        {
            "$group": {
                "_id": "$ip",
                "count": {"$count": {}}
            }
        },
        {
            "$sort": {"count": -1}
        },
        {
            "$limit": 10
        }
    ])

    for ip in ips:
        print("\t{}: {}".format(ip.get('_id'), ip.get('count')))
