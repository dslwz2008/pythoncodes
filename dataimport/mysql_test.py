#-*-coding:utf-8-*-
__author__ = 'shenshen'

import mysql.connector
from datetime import date, datetime, timedelta

x = 20
print(x)

def test1():
    print(x)

def main():
    global x
    x = 10
    print(x)
    test1()

# def main():
#     cnx = mysql.connector.connect(user='root', password='root',
#                               host='127.0.0.1', database='test')
#
#     cursor = cnx.cursor()
#     cur_del = cnx.cursor()
#
#     query = "SELECT * from city"
#     cursor.execute(query)
#
#     for item in cursor:
#       print(item)
#
#     delete_sql = "delete from city where id = 4079"
#     cursor.execute(delete_sql)
#     cnx.commit()
#
#     cursor.close()
#     cnx.close()


if __name__ == '__main__':
    main()