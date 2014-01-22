#-*-coding:utf-8-*-
__author__ = 'shenshen'

import random
import time


base_num = 50000

def time_sort(arr):
    start = time.time()
    arr.sort()
    end = time.time()
    return end - start

def test_sort():
    arr = range(base_num)
    random.shuffle(arr)
    prev = time_sort(arr)
    for i in range(10):
        n = (2 * base_num) * (2 ** i)
        arr = range(n)
        random.shuffle(arr)
        curr = time_sort(arr)
        # curr = time_sort(random.shuffle(range(n)))
        print('%d   %f' % (n, curr))
        print('%f' % (curr / prev))
        prev = curr

if __name__ == '__main__':
    test_sort()