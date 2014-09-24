#-*-coding:utf-8-*-
__author__ = 'shenshen'

from binary_search import *

# NlgN
def two_sum_fast(alist):
    alist.sort()
    count = 0
    for i in range(len(alist)):
        if binarySearch(alist, -alist[i]) > i:
            count += 1
    return count

# (N^2)lgN
def three_sum_fast(alist):
    alist.sort()
    count = 0
    for i in range(len(alist)):
        for j in range(i+1, len(alist)):
            if binarySearch(alist, -alist[i]-alist[j]) > j:
                count += 1
    return count


def test():
    fp = open('1Kints.txt', 'r')
    result = []
    for i in fp:
        result.append(float(i))
    print(two_sum_fast(result))
    print(three_sum_fast(result))


if __name__ == '__main__':
    test()