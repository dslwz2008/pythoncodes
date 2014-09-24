#coding:utf-8

__author__ = 'shenshen'

import threading
import time
import mysql.connector
import multiprocessing

threadLock = threading.Lock()
datalist = []
TOTAL_RECORDS = 30000000
num_per_thread = 1250000

class CheckData(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        global datalist
        print("Starting" + self.name)
        cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1', database='traffic')
        cur_sel = cnx.cursor()
        cur_del = cnx.cursor()
        # read 1000 times
        times = 1000
        num_per_time = num_per_thread / times
        for index in range(times):
            sql_select = "select id,sj,cphm from taxi_gps limit %s,%s"
            start_num = (self.threadID - 1) * num_per_thread + index * num_per_time + 1
            count_num = num_per_time
            print(self.threadID, index, start_num, count_num)
            cur_sel.execute(sql_select, (start_num, count_num))
            delete_ids = []
            for (rid, sj, cphm) in cur_sel:
                if (sj, cphm) not in datalist:
                    # Get lock to synchronize threads
                    threadLock.acquire()
                    datalist.append((sj, cphm))
                    # Free lock to release next thread
                    threadLock.release()
                else:
                    delete_ids.append(rid)

            delete_sql = "delete from taxi_gps where id = %s" % \
                         (' or id = '.join([str(i) for i in delete_ids]), )
            print(delete_sql)
            cur_del.execute(delete_sql)
            cnx.commit()

        cur_sel.close()
        cur_del.close()
        cnx.close()


def main():
    cpus = multiprocessing.cpu_count()
    global num_per_thread
    num_per_thread = TOTAL_RECORDS / cpus
    print(num_per_thread)

    threads = []
    for i in range(cpus):
        threads.append(CheckData(i+1, "Thread-" + str(i+1)))

    for t in threads:
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()
    print("Exiting Main Thread")

if __name__ == '__main__':
    main()
