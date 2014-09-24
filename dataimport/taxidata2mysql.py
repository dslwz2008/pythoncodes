#-*-coding:utf-8-*-
__author__ = 'shenshen'

import mysql.connector
import datetime, time

# 原始表结构,25个字段，后面一串x是不要的字段
# create table DY03_CLGPSDWXX
# (
#   zj          VARCHAR2(32) not null, 0
#   cljcxx_id   VARCHAR2(19), 1 xxxxxxxxxxxxxxx
#   jd          NUMBER(20,6), 2
#   wd          NUMBER(20,6), 3
#   sd          NUMBER(14,6), 4
#   fx          VARCHAR2(50), 5
#   clzt        VARCHAR2(255), 6
#   bjlx        VARCHAR2(25), 7
#   sj          DATE, 8
#   jdjm        NUMBER(20,6), 9 xxxxxxxxxxxxxxx
#   wdjm        NUMBER(20,6), 10 xxxxxxxxxxxxxxx
#   hqsjsj      DATE, 11
#   sfbj        NUMBER(14,4), 12
#   sfjm        NUMBER(14,4), 13 xxxxxxxxxxxxxxx
#   hbgd        NUMBER(14,4), 14 xxxxxxxxxxxxxxx
#   sbbh        VARCHAR2(32), 15 xxxxxxxxxxxxxxx
#   gc          NUMBER(12,2), 16
#   cphm        VARCHAR2(32), 17
#   geometry    MDSYS.SDO_GEOMETRY, 18 xxxxxxxxxxxxxxx
#   cpys        VARCHAR2(32), 19
#   alarmids    VARCHAR2(100), 20 xxxxxxxxxxxxxxx
#   isonline    INTEGER, 21
#   temperature NUMBER(18,2), 22 xxxxxxxxxxxxxxx
#   isempty     INTEGER, 23
#   cllx        VARCHAR2(32) 24
# )

DATAFILE = "D:/jiashandata/taxi_gps_amonth.txt"

FIELDS = {
    'zj':0, 'jd':2, 'wd':3, 'sd':4, 'fx':5, 'clzt':6, 'bjlx':7, 'sj':8, 'hqsjsj':11,
    'sfbj':12, 'gc':16, 'cphm':17, 'cpys':19, 'isonline':21, 'isempty':23, 'cllx':24
}

def main():
    cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1', database='traffic')
    cursor = cnx.cursor()

    sql_insert = ("insert into taxi_gps (zj, jd, wd, sd, fx, clzt, bjlx, sj, hqsjsj, sfbj, gc, " \
            "cphm, cpys, isonline, isempty, cllx) values " \
            "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

    for index, line in enumerate(open(DATAFILE, 'r')):
        if index <= 9945762:
            continue
        # elif index <= 5:
        else:
            try:
                items = line.split(';')
                data_insert = (
                    items[FIELDS['zj']].decode('gbk').strip(),
                    float(items[FIELDS['jd']].decode('gbk').strip()),
                    float(items[FIELDS['wd']].decode('gbk').strip()),
                    float(items[FIELDS['sd']].decode('gbk').strip()),
                    items[FIELDS['fx']].decode('gbk').strip(),
                    items[FIELDS['clzt']].decode('gbk').strip(),
                    items[FIELDS['bjlx']].decode('gbk').strip(),
                    str(datetime.datetime.fromtimestamp(time.mktime(time.strptime(items[FIELDS['sj']].decode('gbk').strip(),"%Y/%m/%d %H:%M:%S.000")))),
                    str(datetime.datetime.fromtimestamp(time.mktime(time.strptime(items[FIELDS['hqsjsj']].decode('gbk').strip(),"%Y/%m/%d %H:%M:%S.000")))),
                    bool(items[FIELDS['sfbj']].decode('gbk').strip()),
                    float(items[FIELDS['gc']].decode('gbk').strip()),
                    items[FIELDS['cphm']].decode('gbk').strip(),
                    items[FIELDS['cpys']].decode('gbk').strip(),
                    bool(items[FIELDS['isonline']].decode('gbk').strip()),
                    # float(items[FIELDS['temperature']].decode('gbk').strip()),
                    bool(items[FIELDS['isempty']].decode('gbk').strip()),
                    items[FIELDS['cllx']].decode('gbk').strip()

                )
                cursor.execute(sql_insert, data_insert)
                cnx.commit()
                if index % 10000 == 0:
                    print('insert %d ...' % index)
            except ValueError:
                continue
        # else:
        #     break

    cursor.close()
    cnx.close()

if __name__ == '__main__':
    main()
    print('finish')
