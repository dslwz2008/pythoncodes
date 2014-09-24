#-*-coding:utf-8-*-
__author__ = 'shenshen'


class RingBuffer(object):
    def __init__(self, n):
        self.number = 0
        self.start = 0
        self.end = self.start - 1
        self.items = [None] * n

    def isEmpty(self):
        return self.number == 0

    def isFull(self):
        return self.number == len(self.items)

    def write(self, data):
        if self.isFull():
            return None
        self.end += 1
        self.items[self.end] = data
        self.number += 1
        return data

    def read(self):
        if self.isEmpty():
            return None
        obj = self.items[self.start]
        self.start += 1
        self.number -= 1
        return obj


def test():
    rb = RingBuffer(4)
    rb.write(3)
    rb.write(4)
    rb.write(2)
    rb.write(1)
    rb.write(5)
    for i in range(4):
        print(rb.read())


if __name__ == '__main__':
    test()