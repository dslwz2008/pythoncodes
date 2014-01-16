#-*-coding:utf-8-*-
__author__ = 'shenshen'

import copy


class StaticSETofInts(object):
    def __init__(self, keys):
        self.items = copy.deepcopy(keys)
        self.items.sort()

    def contains(self, key):
        return self.rank(key) != -1

    def rank(self, key):
        lo = 0
        hi = len(self.items) - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if key < self.items[mid]:
                hi = mid - 1
            elif key > self.items[mid]:
                lo = mid + 1
            else:
                return mid
        return -1

    def howmany(self):
        pass


def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


def binarySearchRecursion(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            if item<alist[midpoint]:
                return binarySearchRecursion(alist[:midpoint],item)
            else:
                return binarySearchRecursion(alist[midpoint+1:],item)

if __name__ == '__main__':
    testlist1 = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    print(binarySearch(testlist1, 3))
    print(binarySearch(testlist1, 13))
    testlist2 = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    print(binarySearchRecursion(testlist2, 3))
    print(binarySearchRecursion(testlist2, 13))
