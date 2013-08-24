#-*-coding:utf-8-*-
__author__ = 'Administrator'

import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://192.168.140.134", safe=True)

# get a handle to the school database
db = connection.school
students = db.students


def find():
    cursor = None
    try:
        cursor = students.find()
    except:
        print "Unexpected error:", sys.exc_info()[0]

    for doc in cursor:
        scores = doc['scores']
        query = {'_id':doc['_id']}
        s = 0
        for index,score in enumerate(scores):
            if index == 2:
                s = score['score']
            if index == 3:
                if s > score['score']:
                    del scores[3]
                else:
                    del scores[2]
        students.update(query,doc)



if __name__ == '__main__':
    find()
