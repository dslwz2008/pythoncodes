# -*-coding:utf-8-*-

import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# performs wholesale replacment of document
def using_update():

    print "updating record using update"
    # get a handle to the school database
    db = connection.school
    student = db.student

    print student.count()

    try:
        cursor = student.find()
        for doc in cursor:#for each doc
            #print doc
            min = -1
            smin = None
            for i, score in enumerate(doc['scores']):
                if score['type'] == 'homework':
                   if min == -1:
                       #print score['score']
                       min = i
                       smin = score['score']
                   else:
                       if score['score'] < smin:
                           min = i
                           smin = score['score']
            assert min != -1
            del(doc['scores'][min])
            print doc['scores']
            student.update({'_id':doc['_id']}, {'scores':doc['scores']})
            
#        # get the doc
#        score = student.find_one({'student_id':1, 'type':'homework'})
#        print "before: ", score
#
#        # add a review_date
#        score['review_date'] = datetime.datetime.utcnow()
#
#        # update the record with update. Note that there an _id but DB is ok with that
#        # because it matches what was there.
#        scores.update({'student_id':1, 'type':'homework'}, score)
#
#        score = scores.find_one({'student_id':1, 'type':'homework'})
#        print "after: ", score

    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

using_update()
