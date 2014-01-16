#-*-coding:utf-8-*-
__author__ = 'shenshen'

# Josephus problem. N people sit in a circle and the one who count M will be killed.
# The final person left will be set free.
from queue import Queue

def josephus(N, M):
    q = Queue()
    for i in range(N):
        q.enqueue(i)
    result = []
    while not q.isEmpty():
        for i in range(M-1):
            q.enqueue(q.dequeue())
        result.append(q.dequeue())
    return result

if __name__ == '__main__':
    print(josephus(7, 2))