# -*-coding:utf-8-*-
# Authoe: Shen Shen
# Email: dslwz2002@163.com
__author__ = 'Shen Shen'

import threading
import math
import mysql.connector
import pymongo
import multiprocessing


SERVERADDR = '192.168.1.2'#127.0.0.1

class Mysql2MongoThread(threading.Thread):
    def __init__(self, threadID, name, cphms):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.cphms = cphms

    def run(self):
        print("Start " + self.name)
        # connect to mysql
        cnx = mysql.connector.connect(user='root', password='root',
                              host=SERVERADDR, database='traffic')
        cur_sel = cnx.cursor()
        cur_del = cnx.cursor()

        # connect to mongodb
        conn_mongo = pymongo.Connection("mongodb://" + SERVERADDR, safe=True)
        db_mongo = conn_mongo.traffic_clean
        taxi = db_mongo.taxi_gps

        for cphm in self.cphms:
            sql_select = "select zj,jd,wd,sd,fx,sj,gc,cphm from taxi_gps where cphm = %s"
            print(self.threadID, cphm)
            cur_sel.execute(sql_select, (cphm, ))
            sjlist = []
            for (zj,jd,wd,sd,fx,sj,gc,cphm) in cur_sel:
                doc = {'zj' : int(zj), 'position' : [jd, wd], 'sd' : sd,
                       'fx' : float(fx), 'gc' : gc, 'cphm' : cphm, 'sj' : sj}
                taxi.insert(doc)


        cur_sel.close()
        cur_del.close()
        cnx.close()
        print("Finish " + self.name)


def get_distinct_cphm():
    cnx = mysql.connector.connect(user='root', password='root',
                              host=SERVERADDR, database='traffic')
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
            cphmlist = cphms[i*npt:(i+1)*npt]
        threads.append(Mysql2MongoThread(i, "Thread-" + str(i), cphmlist))

    for t in threads:
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    print("Exiting Main Thread")

if __name__ == '__main__':
    main()