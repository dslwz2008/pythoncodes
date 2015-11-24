# -*-coding:utf-8-*-
# Author: Shen Shen
# Email: dslwz2002@163.com
__author__ = 'Shen Shen'


# @profile
def getImage():
    import psycopg2

    conn = psycopg2.connect("host=192.168.1.117 port=5432 dbname=test4 user=postgres password=111")
    cur = conn.cursor()

    idx = 1
    sql = "select data from IMAGEINFO where id < %s" % (10, )
    cur.execute(sql)
    for item in cur.fetchall():
        filename = 'test/1_%s.jpg' % (idx,)
        with open(filename, 'wb') as fp:
            fp.write(item[0])
        idx += 1

    # conn.commit()

    cur.close()
    conn.close()

# @profile
def getImageFromLink():
    import psycopg2
    import requests
    from PIL import Image
    from StringIO import StringIO

    conn = psycopg2.connect("host=192.168.1.117 port=5432 dbname=test4 user=postgres password=111")
    cur = conn.cursor()

    idx = 1
    sql = "select link from IMAGEINFOLINK limit %s" % (10, )
    cur.execute(sql)
    for item in cur.fetchall():
        filename = 'test/2_%s.jpg' % (idx,)
        r = requests.get(item[0])
        img = Image.open(StringIO(r.content))
        img.save(filename)
        idx += 1

    cur.close()
    conn.close()

if __name__ == '__main__':
    import time
    stime = time.time()
    getImage()
    etime = time.time()
    print(etime-stime)

    # stime = time.time()
    # getImageFromLink()
    # etime = time.time()
    # print(etime-stime)

    # import timeit
    # print(timeit.timeit("getImage()","from __main__ import getImage"))
    # print(timeit.timeit("getImageFromLink()","from __main__ import getImageFromLink"))
