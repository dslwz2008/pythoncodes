# -*-coding:utf-8-*-
# Authoe: Shen Shen
# Email: dslwz2002@163.com
__author__ = 'Shen Shen'

import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://192.168.1.2", safe=True)

# get a handle to the school database
db = connection.traffic
taxi = db.taxi_gps


def find():
    query = {'cphm':u'浙F65T13'}

    try:
        cur = taxi.find()
        print(cur.count)
        for doc in cur:
            pos = doc['position']
            if pos == [0.0, 0.0] or pos[0] > 180.0 or pos[0] < -180.0 or \
                pos[1] > 90.0 or pos[1] < -90.0:
                print(doc)
                taxi.remove(doc)

    except:
        print "Unexpected error:", sys.exc_info()[0]


if __name__ == '__main__':
    find()