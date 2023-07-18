#!/usr/bin/env python3
""" Provides some stats about Nginx logs stored in MongoDB. """
from pymongo import MongoClient


client = MongoClient()
nginx_collection = client.logs.nginx

print("{} logs".format(nginx_collection.count_documents({})))
print("Methods:")

print("\t method GET: {}"
      .format(nginx_collection.count_documents({"method": "GET"})))
print("\t method POST: {}"
      .format(nginx_collection.count_documents({"method": "POST"})))
print("\t method PUT: {}"
      .format(nginx_collection.count_documents({"method": "PUT"})))
print("\t method PATCH: {}"
      .format(nginx_collection.count_documents({"method": "PATCH"})))
print("\t method DELETE: {}"
      .format(nginx_collection.count_documents({"method": "DELETE"})))

print("{} status check"
      .format(nginx_collection.count_documents(
              {"method": "GET", "path": "/status"})))
