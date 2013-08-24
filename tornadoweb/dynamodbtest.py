#!/usr/bin/env python 
# -*- coding:utf-8 -*- 

import boto
import boto.dynamodb
import datetime

region = 'ap-southeast-1'

#print boto.dynamodb.regions()
conn = boto.dynamodb.connect_to_region(region)
tables = conn.list_tables()
table_name = 'pictures_test'
table = conn.get_table(tables[0])
print conn.describe_table(tables[0])

def additem():
    item_data = {'id':5, 'message':'wrtie through api', 'time':str(datetime.datetime.today())}
    #new item
    item = table.new_item(attrs = item_data)
    print item
    #modify item's attr
    item['time'] = str(datetime.datetime.now())
    item.put()#commit
    print item

def getitem():
    item = table.get_item(hash_key=5)
    print item
    
def updateitem():
    item = table.get_item(hash_key=2)
    item['message'] = u'第二个测试用例'
    item['time'] = str(datetime.datetime.now())
    item.put()
    
def deleteitem():
    item = table.get_item(hash_key=1)
    item.delete()
    
def deltetable():
    table.delete()
    #conn.delete_table(table)
    
def get_latest_item():
    table = conn.get_table(tables[table_name])
    
    
if __name__ == '__main__':
    #additem()
    getitem()
    updateitem()
    #deleteitem
