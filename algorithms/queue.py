#-*-coding:utf-8-*-
__author__ = 'shenshen'

import random

class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm #pages per minute
        self.currentTask = None
        self.timeRemaining = 0 #seconds

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() \
                             * 60/self.pagerate

class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp

def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

        if newPrintTask():
           task = Task(currentSecond)
           printQueue.enqueue(task)

        if (not labprinter.busy()) and \
                (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append( \
                nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."\
                    %(averageWait,printQueue.size()))

def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

def test():
    q=Queue()
    q.isEmpty()
    q.enqueue('dog')
    q.enqueue(4)
    q=Queue()
    q.isEmpty()
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)

def hotPotato(namelist, num):
    simqueue = Queue()
    for i in namelist:
        simqueue.enqueue(i)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        name = simqueue.dequeue()
        print('%s was eliminate!' % name)

    return simqueue.dequeue()

if __name__ == '__main__':
    #test()
    #print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
    for i in range(10):
        simulation(3600,5)

