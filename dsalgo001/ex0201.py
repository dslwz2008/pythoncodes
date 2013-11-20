#-*-coding:utf-8-*-
__author__ = 'shenshen'

import Queue

queues1 = {
    '1': Queue.Queue(),
    '2': Queue.Queue(),
    '3': Queue.Queue(),
    '4': Queue.Queue(),
    '5': Queue.Queue(),
    '6': Queue.Queue(),
    '7': Queue.Queue(),
    '8': Queue.Queue(),
    '9': Queue.Queue()
}
queues2 = {
    'A': Queue.Queue(),
    'B': Queue.Queue(),
    'C': Queue.Queue(),
    'D': Queue.Queue(),
}
def main():
    """
    使用队列对扑克牌排序
    """
    n = int(raw_input())
    pokerstr = raw_input()
    pokers = pokerstr.split()
    for i in range(n):
        queues1[pokers[i][1]].put(pokers[i])

    for i in '123456789':
        output = ''
        for j in range(queues1[i].qsize()):
            item = queues1[i].get()
            output += (item+' ')
            queues2[item[0]].put(item)
        print('Queue%d:%s' % (int(i), output))

    result = []
    for i in 'ABCD':
        q = queues2[i]
        output = ''
        for x in range(q.qsize()):
            item = q.get()
            output += (item + ' ')
            result.append(item)
        print('Queue%s:%s' % (i, output))

    print(' '.join(result))

if __name__ == '__main__':
    main()
