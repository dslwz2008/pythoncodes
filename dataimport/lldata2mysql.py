#-*-coding:utf-8-*-
__author__ = 'shenshen'

import mysql.connector
import datetime, time

DATAFILE = "D:/data/jiashandata/DY50_LL_DATA_6M.csv"

FIELDS = {
    'ldbh':0, 'ldmc':1, 'fx':2, 'zhll':3, 'pjcs':4, 'tddj':5,
    'createtime':6
}


def main():
    cnx = mysql.connector.connect(user='root', password='root',
                              host='192.168.1.88', database='traffic')
    cursor = cnx.cursor()

    sql_insert = ("insert into dy50_ll_data_6m (ldbh, ldmc, fx, zhll, pjcs, tddj, createtime) values " \
            "(%s,%s,%s,%s,%s,%s,%s)")

    for index, line in enumerate(open(DATAFILE, 'r')):
        if index == 0:
            continue
        else:
            try:
                items = line.split(',')
                data_insert = (
                    items[FIELDS['ldbh']].decode('gbk').strip("\""),
                    items[FIELDS['ldmc']].decode('gbk').strip("\""),
                    items[FIELDS['fx']].decode('gbk').strip("\""),
                    int(items[FIELDS['zhll']].decode('gbk').strip("\"")),
                    float(items[FIELDS['pjcs']].decode('gbk').strip("\"")),
                    items[FIELDS['tddj']].decode('gbk').strip("\""),
                    str(datetime.datetime.fromtimestamp(time.mktime(time.strptime(items[FIELDS['createtime']].decode('gbk').strip("\n").strip("\""),"%Y/%m/%d %H:%M:%S")))),
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
    print('finish')
