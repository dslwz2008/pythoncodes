#-*-coding:utf-8-*-
__author__ = 'shenshen'
import math

def combination(n, m):
    return math.factorial(n) / (math.factorial(n - m) * math.factorial(m))

def main(total, num):
    sum = 0
    for n in range(num):
        item = combination(total, n) * math.pow(0.32, n) * math.pow(0.68, total - n)
        sum = sum + item
    return 1 - sum

if __name__ == '__main__':
    # print(combination(5, 2))
    # print(combination(300, 1))
    # print(combination(10, 3))
    # print(combination(10, 7))
    print(main(300, 120))
