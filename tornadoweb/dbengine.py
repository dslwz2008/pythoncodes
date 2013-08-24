#-*-coding:utf-8-*-
__author__ = 'shenshen'

import sys
import pymongo
import random
import datetime
import json

# establish a connection to the database
conn = 'mongodb://shenshen:shenshen@linus.mongohq.com:10024/mytest'
connection = pymongo.Connection(conn, safe=True)

alphabets = 'abcdefghij'
nums = '0123456789'
ports = ['hk','qd','sh','dl','tj']
work_types = ['aa','bb','cc','dd','ee']
warning_types = ['ff','gg','hh','ii','jj']

def gen_info(infos):
    name = []
    for _ in range(5):
        name.append(infos[random.randint(0,9)])
    return ''.join(name)

def insert_to_shipinfo():
    #print connection.mytest.collection_names()
    shipinfo = connection.mytest.shipinfo
    for _ in range(50):
        ship = {}
        ship['name'] = gen_info(alphabets)
        ship['beidou'] = gen_info(nums)
        ship['owner'] = gen_info(alphabets)
        ship['tele'] = gen_info(nums)
        ship['power'] = gen_info(nums)
        ship['port'] = ports[random.randint(0,4)]
        ship['worktype'] = work_types[random.randint(0,4)]
        shipinfo.insert(ship)
    print 'insert success!!!'

def show_shipinfo(page,rows,sidx,sord):
    # establish a connection to the database
    conn = 'mongodb://shenshen:shenshen@linus.mongohq.com:10024/mytest'
    connection = pymongo.Connection(conn, safe=True)
    shipinfo = connection.mytest.shipinfo
    infos = []
    page = int(page)
    rows = int(rows)
    cursor = shipinfo.find({},{'_id':0}).sort(sidx,pymongo.DESCENDING).skip((page-1)*rows).limit(rows)
    for si in cursor:
        infos.append(si)
    return infos

def insert_to_warninginfo():
    shipinfo = connection.mytest.shipinfo
    warninginfo = connection.mytest.warninginfo
    ship_names = [si['name'] for si in shipinfo.find()]
    for _ in range(50):
        warning_info = {}
        warning_info['shipname'] = ship_names[random.randint(0,49)]
        warning_info['type'] = warning_types[random.randint(0,4)]
        warning_info['time'] = datetime.datetime.now()
        warning_info['lattitude'] = random.randint(-90,90)
        warning_info['longtitude'] = random.randint(-180,180)
        warninginfo.insert(warning_info)
    print 'insert success!!!'

def show_warninginfo():
    warninginfo = connection.mytest.warninginfo
    for wi in warninginfo.find():
        print wi

if __name__ == '__main__':
    #insert_to_shipinfo()
    print show_shipinfo(1,10,'beidou','desc')
    #print json.dumps(show_shipinfo())
    #insert_to_warninginfo()
    #show_warninginfo()