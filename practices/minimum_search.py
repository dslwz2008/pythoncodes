#-*-coding:utf-8-*-
__author__ = 'shenshen'

def polynomial(x):
    """该函数定义了要用到的多项式函数"""
    return x * x - 4 * x + 4
    #return x * x - x + 2

def golden_section_search(fn, a, b, tol):
    """函数fn最小值在[a,b]区间内,tols是容差；
    该函数找到小于容差的最小值并返回"""
    goldsec = 0.618
    l = b - a
    p = a + (1 - goldsec) * l
    q = a + goldsec * l
    while l >= tol:
        if fn(p) > fn(q):
            a = p
            p = q
            l = b - a
            q = a + goldsec * l
        else:
            b = q
            q = p
            l = b - a
            p = a + (1 - goldsec) * l
    #返回区间的中点作为函数的极小点
    return (a + b) / 2

def fibonacci_search(fn, a, b, delta):
    """该函数利用fibonacci数列找到函数fn在区间[a,b]上的最小值"""
    #先给出斐波那契数列的前几项
    fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
    n = 0
    for index, item in enumerate(fibonacci):
        if item >= 1 / delta:
            n = index
            break
    #k = 1
    p = a + (b - a) * fibonacci[n - 2] / float(fibonacci[n])
    q = a + (b - a) * fibonacci[n - 1] / float(fibonacci[n])
    for k in range(2, n - 1):
        if abs(p - q) < 0.00001:
            q = q + 0.0001
        if fn(p) > fn(q):
            a = p
            p = q
            q = a + (b - a) * fibonacci[n - k] / float(fibonacci[n - k + 1])
        else:
            b = q
            q = p
            p = a + (b - a) * fibonacci[n - k - 1] / float(fibonacci[n - k + 1])
    return (a + b) / 2

if __name__ == '__main__':
    l = golden_section_search(polynomial, 0, 3, 0.08)
    print(l)
    l = fibonacci_search(polynomial, 0, 3, 0.08)
    print(l)
