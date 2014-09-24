#-*-coding:utf-8-*-
__author__ = 'shenshen'

import mysql.connector
import datetime, time

DATAFILE = "D:/jiashandata/DY50_XQ_SSSJ.csv"

FIELDS = {
    'sbbh':0, 'fx':1, 'zhll':2, 'pjcs':3, 'qssj':4, 'jssj':5,
    'createtime':6, 'operator':7, 'tjsj':8, 'fxms':9
}


def main():
    cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1', database='traffic')
    cursor = cnx.cursor()

    sql_insert = ("insert into dy50_xq_sssj (sbbh, fx, zhll, pjcs, qssj, jssj, createtime, operator, tjsj, fxms) values " \
            "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

    for index, line in enumerate(open(DATAFILE, 'r')):
        if index <= 477931:
            continue
        else:
            try:
                items = line.split(',')
                data_insert = (
                    items[FIELDS['sbbh']].strip("\""),
                    items[FIELDS['fx']].strip("\""),
                    int(items[FIELDS['zhll']].strip("\"")),
                    float(items[FIELDS['pjcs']].strip("\"")),
                    str(datetime.datetime.fromtimestamp(time.mktime(time.strptime(items[FIELDS['qssj']].strip("\""),"%Y/%m/%d %H:%M:%S")))),
                    str(datetime.datetime.fromtimestamp(time.mktime(time.strptime(items[FIELDS['jssj']].strip("\""),"%Y/%m/%d %H:%M:%S")))),
                    str(datetime.datetime.fromtimestamp(time.mktime(time.strptime(items[FIELDS['createtime']].strip("\""),"%Y/%m/%d %H:%M:%S")))),
                    items[FIELDS['operator']].strip("\""),
                    float(items[FIELDS['tjsj']].strip("\"")),
                    items[FIELDS['fxms']].strip("\n").strip("\"")
                )
                cursor.execute(sql_insert, data_insert)
                cnx.commit()
                if index % 10000 == 0:
                    print('insert %d ...' % index)
            except ValueError, err:
                print(err)
                continue

    cursor.close()
    cnx.close()

if __name__ == '__main__':
    print('start!')
    main()
    print('finish')
