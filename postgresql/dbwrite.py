# -*-coding:utf-8-*-
# Author: Shen Shen
# Email: dslwz2002@163.com
__author__ = 'Shen Shen'

import psycopg2
import sys

INSERT_NO = 1000

def buildDbStorePic():
    print(sys._getframe().f_code.co_name)
    conn = psycopg2.connect("host=192.168.1.117 port=5432 dbname=test4 user=postgres password=111")
    cur = conn.cursor()

    idx = 1
    filename = 'SAM_105_3.jpg'
    with open(filename, 'rb') as picObj:
        data = picObj.read()
        for i in xrange(INSERT_NO):
            cur.execute("INSERT INTO IMAGEINFO (id, name, format, data) VALUES (%s, %s, %s, %s)",
                        (idx, filename, 'jpg', psycopg2.Binary(data)))
            idx += 1
            if idx % 100 == 0:
                print(idx)
        conn.commit()

    cur.close()
    conn.close()

def buildDbStoreLink():
    print(sys._getframe().f_code.co_name)
    conn = psycopg2.connect("host=192.168.1.117 port=5432 dbname=test4 user=postgres password=111")
    cur = conn.cursor()

    idx = 1
    filename = 'SAM_105_3.jpg'
    for i in xrange(INSERT_NO):
        cur.execute("INSERT INTO IMAGEINFOLINK (id, name, format, link) VALUES (%s, %s, %s, %s)",
                    (idx, filename, 'jpg', 'http://192.168.1.117/data/SAM_105_3.JPG'))
        idx += 1
        if idx % 100000 == 0:
            print(idx)
    conn.commit()

    cur.close()
    conn.close()


if __name__ == '__main__':
    buildDbStorePic()
    # buildDbStoreLink()