#-*-coding:utf-8-*-
__author__ = 'shenshen'

import random


class Bag(object):
    def __init__(self):
        self.items = []
        self.index = -1

    def add(self, item):
        self.items.append(item)

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __iter__(self):
        return self

    def next(self):
        self.index += 1
        if self.index < len(self.items):
            return self.items[self.index]
        else:
            raise StopIteration


class RandomBag(Bag):
    def __init__(self):
        Bag.__init__(self)

    def __iter__(self):
        random.shuffle(self.items)
        return self

def test():
    rb = RandomBag()
    rb.add(5)
    rb.add(4)
    rb.add(3)
    rb.add(2)
    rb.add(1)
    for x in rb:
        print(x)

if __name__ == '__main__':
    test()
