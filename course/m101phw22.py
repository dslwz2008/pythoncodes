# -*-coding:utf-8-*-

import pymongo
import sys

# establish a connection to the database
conn = pymongo.Connection("mongodb://localhost", safe=True)
print conn

def remove_lowest_hw():
    db = conn.students
    grades = db.grades
    assert grades
    
    try:
        query = {'type':'homework'}
        sort = [('student_id',pymongo.ASCENDING),('score',pymongo.DESCENDING)]
        cursor = grades.find(query).sort(sort)#.limit(10)
        print cursor.count()
        counter = 0
        for doc in cursor:
            if counter == 1:
                print doc
                grades.remove(doc)
                counter = 0
            else:
                counter = counter + 1

    except:
        print "Unexpected error:", sys.exc_info()[0]
        
if __name__ == '__main__':
    remove_lowest_hw()
