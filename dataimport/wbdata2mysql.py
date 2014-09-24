#-*-coding:utf-8-*-
__author__ = 'shenshen'

import mysql.connector
import datetime, time

DATAFILE = "D:/data/jiashandata/DY50_WB_SSSJ.csv"

FIELDS = {
    'sbbh':0, 'fx':1, 'zhll':2, 'pjcs':3, 'qssj':4, 'jssj':5,
    'createtime':6, 'operator':7, 'tjsj':8, 'fxms':9 #最后两个没有数据，故放弃
}


def main():
    cnx = mysql.connector.connect(user='root', password='root',
                              host='192.168.1.88', database='traffic')
    cursor = cnx.cursor()

    sql_insert = ("insert into dy50_wb_sssj (sbbh, fx, zhll, pjcs, qssj, jssj, createtime, operator) values " \
            "(%s,%s,%s,%s,%s,%s,%s,%s)")

    for index, line in enumerate(open(DATAFILE, 'r')):
        if index == 0:
            continue
        else:
            try:
                items = line.split(',')
                data_insert = (
                    items[FIELDS['sbbh']].decode('gbk').strip("\""),
                    items[FIELDS['fx']].decode('gbk').strip("\""),
                    int(items[FIELDS['zhll']].decode('gbk').strip("\"")),
                    int(items[FIELDS['pjcs']].decode('gbk').strip("\"")),
                    str(datetime.datetime.fromtimestamp(time.mktime(time.strptime(items[FIELDS['qssj']].decode('gbk').strip("\""),"%Y/%m/%d %H:%M:%S")))),
                    str(datetime.datetime.fromtimestamp(time.mktime(time.strptime(items[FIELDS['jssj']].decode('gbk').strip("\""),"%Y/%m/%d %H:%M:%S")))),
                    str(datetime.datetime.fromtimestamp(time.mktime(time.strptime(items[FIELDS['createtime']].decode('gbk').strip("\""),"%Y/%m/%d %H:%M:%S")))),
                    items[FIELDS['operator']].decode('gbk').strip("\""),
                    # float(items[FIELDS['tjsj']].decode('gbk').strip("\"")),
                    # items[FIELDS['fxms']].decode('gbk').strip("\"")
                )
                cursor.execute(sql_insert, data_insert)
                cnx.commit()
                print('insert %d ...' % index)
            except ValueError, err:
                print(err)
                continue

    cursor.close()
    cnx.close()

if __name__ == '__main__':
    print('start!')
    main()
