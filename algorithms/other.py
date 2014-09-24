#-*-coding:utf-8-*-
__author__ = 'shenshen'
import math
import sys
import random
import numpy as np

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


# lgN
def local_minimum_of_array(alist):
    lo = 0
    hi = len(alist) - 1
    while lo <= hi:
        mid = (lo + hi) / 2
        if alist[mid] <= alist[mid-1] and alist[mid] <= alist[mid+1]:
            return mid
        else:
            if alist[mid-1] <= alist[mid+1]:
                hi = mid
            else:
                lo = mid
    return -1

# 2N*lgN
def local_minimum_of_matrix(mat):
    # find the minimum of row N/2
    row_num = mat.shape[0]/2
    row = mat[row_num]
    j = 1024
    minimum = 1024
    for index, item in enumerate(row):
        if item < minimum:
            minimum = item
            j = index
    col = [_[j] for _ in mat]
    i = local_minimum_of_array(col)
    return mat[i][j]


def bitonic(N):
    mid = np.random.randint(N)
    result = [5]
    i = 1
    while i < mid:
        result.append(result[i-1] + np.random.randint(N))
        i += 1
    while i < N:
        result.append(result[i-1] - np.random.randint(N))
        i += 1
    return result


def bitonic_max(alist, lo, hi):
    if lo == hi:
        return hi
    mid = lo + (hi - lo) / 2
    if alist[mid] < alist[mid + 1]:
        return bitonic_max(alist, mid + 1, hi)
    elif alist[mid] > alist[mid + 1]:
        return bitonic_max(alist, lo, mid)
    else:#they are equal
        if alist[mid] < alist[mid - 1]:
            return bitonic_max(alist, lo, mid)
        elif alist[mid] > alist[mid - 1]:
            return bitonic_max(alist, mid + 1, hi)
        else:
            #本算法无法处理三个数相等的情况
            return -1

# worst case: 3lgN
def bitonic_search(alist, num):
    max_ind = bitonic_max(alist, 0, len(alist) - 1)#lgN
    #lgN


def test_bitonic_max():
    N = 20
    rst = bitonic(N)
    #rst = [5, 18, 29, 39, 55, 64, 79, 90, 105, 114, 114, 118, 123, 113, 95, 89, 87, 80, 66, 54]
    print(rst)
    print(bitonic_max(rst, 0, N - 1))


def test_local_minimum_of_array():
    for i in range(100):
        n = 10
        temp = random.sample(xrange(100), n)
        # 确保数组有局部最小值存在
        if temp[0] < temp[1] or temp[len(temp)-1] < temp[len(temp)-2]:
            continue
        idx = local_minimum_of_array(temp)
        if idx != -1:
            print('the local minimum of array %s is %s.\n' % (str(temp), temp[idx]))
        else:
            print('this array does not have a minimum element.')


def test_local_minimum_of_matrix():
    m = np.random.randint(20, size=(10, 10))
    print(m)
    print(local_minimum_of_matrix(m))

def is_valid(pattern):
    from stack import Stack
    s = Stack()
    for i in pattern:
        if i in '1234':
            s.push(i)
        else:
            if s.isEmpty():
                return False
            else:
                s.pop()
    return True

def give_change():
    import itertools as it
    base = '12345678'
    result = []
    for x in it.permutations(base):
        if is_valid(x):
            result.append(x)
    return len(result)


def pattern_num(s):
    pattern = ['01', '10']
    count = []
    for p in pattern:
        count.append(s.count(p))
    return sum(count)


def stat_pattern(m, n, k):
    s1 = m * '0'
    s2 = n * '1'
    temp = []
    result = []
    import itertools as it
    for i in it.permutations(s1+s2):
        if i not in temp:
            temp.append(i)
            if pattern_num(''.join(i)) == k:
                result.append(i)
    return len(result)

if __name__ == '__main__':
    # test_local_minimum_of_array()
    # test_local_minimum_of_matrix()
    # print(bitonic(20))
    # test_bitonic_max()
    # print(give_change())
    #print(stat_pattern(5, 4, 4))
    print(stat_pattern(10, 12, 10))