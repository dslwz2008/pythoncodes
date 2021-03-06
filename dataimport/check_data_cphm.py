#coding:utf-8

__author__ = 'shenshen'

import threading
import time
import math
import mysql.connector
import multiprocessing


class CheckData(threading.Thread):
    def __init__(self, threadID, name, cphms):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.cphms = cphms

    def run(self):
        print("Start " + self.name)
        cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1', database='traffic')
        cur_sel = cnx.cursor()
        cur_del = cnx.cursor()

        for cphm in self.cphms:
            if cphm != u"浙F86T13":
                continue
            sql_select = "select id,sj from taxi_gps where cphm = %s"
            print(self.threadID, cphm)
            cur_sel.execute(sql_select, (cphm, ))
            sjlist = []
            delete_ids = []
            for (rid, sj) in cur_sel:
                if sj not in sjlist:
                    sjlist.append(sj)
                else:
                    delete_ids.append(rid)

            if len(delete_ids) != 0:
                delete_sql = "delete from taxi_gps where id = %s" % \
                             (' or id = '.join([str(i) for i in delete_ids]), )
                print(delete_sql)
                cur_del.execute(delete_sql)
                cnx.commit()

        cur_sel.close()
        cur_del.close()
        cnx.close()
        print("Finish " + self.name)


def get_distinct_cphm():
    cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1', database='traffic')
    cur_sel = cnx.cursor()
    sql_select = "select DISTINCT cphm from taxi_gps"
    cur_sel.execute(sql_select)
    result = []
    for item in cur_sel:
        result.append(item[0])
    return result

def main():
    print("Start!")
    cpus = multiprocessing.cpu_count()
    cphms = get_distinct_cphm()
    # n cphm per thread
    npt = int(math.ceil(len(cphms)/float(cpus)))

    threads = []
    for i in range(cpus):
        cphmlist = []
        if i == cpus - 1:
            cphmlist = cphms[i*npt:]
        else:
            cphmlist = cphms[i*npt:(i+1)*npt-1]
        threads.append(CheckData(i, "Thread-" + str(i), cphmlist))

    for t in threads:
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    print("Exiting Main Thread")

if __name__ == '__main__':
    main()
