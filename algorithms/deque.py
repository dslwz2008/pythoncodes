#-*-coding:utf-8-*-
__author__ = 'shenshen'

from lists import DoublyLinkedList


class DequeL(object):
    def __init__(self):
        self.list = DoublyLinkedList()
        self.number = 0

    def size(self):
        return self.number

    def isEmpty(self):
        return self.number == 0

    def pushLeft(self, data):
        self.list.pushHead(data)
        self.number += 1

    def pushRight(self, data):
        self.list.pushTail(data)
        self.number += 1

    def popLeft(self):
        self.number -= 1
        return self.list.popHead()

    def popRight(self):
        self.number -= 1
        return self.list.popTail()


class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

def test():
    d=Deque()
    print(d.isEmpty())
    d.addRear(4)
    d.addRear('dog')
    d.addFront('cat')
    d.addFront(True)
    print(d.size())
    print(d.isEmpty())
    d.addRear(8.4)
    print(d.removeRear())
    print(d.removeFront())

#palindrome checker
def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

if __name__ == '__main__':
    #test()
    print(palchecker("lsdkjfskf"))
    print(palchecker("radar"))
