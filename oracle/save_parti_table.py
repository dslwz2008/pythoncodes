# -*-coding:utf-8-*-
# Author: Shen Shen
# Email: dslwz2002@163.com
__author__ = 'Shen Shen'

from datetime import *
import time
import cx_Oracle
import logging

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='%s.log' % (datetime.now().strftime('%Y%m%d%H%M%S'),),
                filemode='w')


#定义一个StreamHandler，将DEBUG级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


# 根据交通局数据库情况自行修改
# test
server = {
    'user':'scott',
    'passwd':'Admin123',
    'ip':'192.168.1.2',
    'port':1521,
    'service':'vge.orcl'
}

# 每天一个分区
table = {
    'user':'scott',
    'name':'GRADERECORD',
    'parti_prefix':'GPS_HIS', # 前缀
    'start_date':datetime.strptime('20150401','%Y%m%d'),# 开始日期
    'end_date':datetime.strptime('20150701','%Y%m%d'),# 结束日期
    'key':'sno', # 用于排序的一个key，可以填主键
}

# 取的是这两个行号之间的记录，注意不包括这两行
config = {
    'minValue':0,
    'step':10000
}

def main():
    cnct = '%s/%s@%s:%d/%s' % (server['user'], server['passwd'], server['ip'],
                               server['port'], server['service'])
    con = cx_Oracle.connect(cnct)

    delta = table['end_date'] - table['start_date']
    for day in range(delta.days):
        cur_day = table['start_date'] + timedelta(day)
        cur_parti = table['parti_prefix'] + cur_day.strftime('%Y%m%d')
        logging.debug("start reading %s" % (cur_day.strftime('%Y%m%d'),))

        # 查询分区数据表的总记录条数
        stat_cur = con.cursor()
        query = 'select count(*) from %s.%s partition(%s)' % (table['user'], table['name'], cur_parti)
        stat_cur.execute(query)
        res = stat_cur.fetchall()
        total_cnt = int(res[0][0])
        stat_cur.close()

        filename = '%s_%s.csv' % (table['name'], cur_parti)
        fp = open(filename, 'w')

        # 开始查询记录
        iter_cnt = total_cnt % config['step'] + 1
        cur = con.cursor()
        for i in range(iter_cnt):
            query_start = time.time()
            min = config['minValue']
            max = min + config['step'] + 1
            query = 'select * from %s.%s partition(%s) where rowid in (' \
                        'select rid from (' \
                            'select rownum rn,rid from (' \
                                'select rowid rid,%s from %s.%s order by %s asc' \
                            ') where rownum < %d ' \
                        ') where rn > %d' \
                    ') order by %s asc' % (
                table['user'], table['name'], cur_parti, table['key'],
                table['user'], table['name'], table['key'], max, min, table['key']
            )

            cur.execute(query)
            res = cur.fetchall()
            # 写入文件
            for n in res:
                item_str = []
                for item in n:
                    item_str.append(str(item))
                fp.write(','.join(item_str)+'\n')

            query_elapsed = (time.time() - query_start)
            logging.debug("%f seconds"%(query_elapsed,))
            config['minValue'] = min + config['step']

        cur.close()
        fp.close()
    con.close()


if __name__ == '__main__':
    main()