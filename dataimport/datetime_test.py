# -*-coding:utf-8-*-
# Authoe: Shen Shen
# Email: dslwz2002@163.com
__author__ = 'Shen Shen'

import pymongo
import sys
from datetime import datetime
import timeit

# establish a connection to the database
connection = pymongo.Connection("mongodb://192.168.1.2", safe=True)


def insert():

    # get a handle to the school database
    db=connection.test
    dt1= db.datetime1
    dt2 = db.datetime2

    try:
        print("insert....")
        year = 2014
        month = 4
        for day in range(30):
            print(day+1)
            for hour in range(24):
                for minute in range(60):
                    doc1 = {'datetime': datetime(year, month, day+1, hour, minute)}
                    doc2 = {'year':year, 'month':month, 'day':day+1,
                            'hour':hour, 'minute':minute}
                    dt1.insert(doc1)
                    dt2.insert(doc2)
        print('finish')

    except:
        print("Unexpected error:", sys.exc_info()[0])


def find1():
    # get a handle to the school database
    db=connection.test
    dt1= db.datetime1

    try:
        start = datetime(2014, 4, 28, 0, 0, 0)
        end = datetime(2014, 4, 30, 0, 0, 0)
        #print(dt1.find({'datetime': {'$gt': start, '$lt': end}}).explain())
        cur = dt1.find({'datetime': {'$gt': start, '$lt': end}})
        # for i in cur:
        #     print(i)
    except:
        print("Unexpected error:", sys.exc_info()[0])


def find2():
    # get a handle to the school database
    db=connection.test
    dt2 = db.datetime2

    try:

        #print(dt2.find({'year':2014, 'month':4, 'day':{'$gt':28, '$lt':30}}).explain())
        cur = dt2.find({'year':2014, 'month':4, 'day':{'$gt':28, '$lt':30}})

        # for i in cur:
        #     print(i)


    except:
        print("Unexpected error:", sys.exc_info()[0])

if __name__ == '__main__':
    #insert()
    print(timeit.timeit('find1()', setup="from __main__ import find1", number=100000))
    #t1.repeat(10, 10)

    print(timeit.timeit('find2()', setup="from __main__ import find2", number=100000))
    # t2 = timeit.Timer('find2()')
    # t2.repeat(10, 10000)