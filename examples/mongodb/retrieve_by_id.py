#!/usr/bin/env python

from pymongo import MongoClient
import pymongo.errors
from bson.objectid import ObjectId

username, password, host, dbname = 'user0', 'pwd0', '127.0.0.1', 'test_db'
client = MongoClient('mongodb://%s:%s@%s/%s' % (username, password, host, dbname))

try:
  db = client.test_db
  pycollection = db['pycollection']
  myId = ObjectId('5b052f7bbead9cca40fdd453')
  print(pycollection.find_one({'_id': myId}))

except pymongo.errors.OperationFailure as e:
  print("ERROR: %s" % (e))
