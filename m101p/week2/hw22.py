#-*-coding:utf-8-*-
__author__ = 'Administrator'

import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://192.168.1.120", safe=True)

# get a handle to the school database
db = connection.students
grades = db.grades


def find():
    print "find, reporting for duty"
    query = {'type':'homework'}
    cursor = None
    try:
        cursor = grades.find(query)
    except:
        print "Unexpected error:", sys.exc_info()[0]

    last = None
    for doc in cursor:
        print 'processing: %s' % doc['student_id']
        if not last or last['student_id'] != doc['student_id']:
            last = doc
            continue
        else:
            if doc['score'] >= last['score']:
                grades.remove(last['_id'])
            else:
                grades.remove(doc['_id'])

if __name__ == '__main__':
    find()
