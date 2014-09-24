#-*-coding:utf-8-*-
__author__ = 'shenshen'


class Node(object):
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class DoublyLinkedNode(Node):
    def __init__(self, initdata):
        Node.__init__(self, initdata)
        self.prev = None

    def getPrevious(self):
        return self.prev

    def setPrevious(self, prev):
        self.prev = prev
