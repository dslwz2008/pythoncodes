#-*-coding:utf-8-*-
__author__ = 'shenshen'
import math
import sys

# 找到数组中差值最小的一对数，要求NlogN级别
def find_nearest(alist):
    alist.sort()#NlogN
    min = sys.float_info.max
    j, k = alist[0:2]
    for i in range(len(alist) - 1):#N
        dist = math.fabs(alist[i] - alist[i+1])
        if dist < min:
            min = dist
            j, k = i, i + 1
    return alist[j], alist[k]


# 找到数组中差值最大的一对数，要求N级别
def find_farest(alist):
    min, max = alist[0:2]
    for i in alist[2:]:
        if i < min:
            min = i
        if i > max:
            max = i
    return min, max


def test():
    a = [0, -1, 23, -45, 86, -9, -23]
    print(find_farest(a))
    print(find_nearest(a))


if __name__ == '__main__':
    test()


