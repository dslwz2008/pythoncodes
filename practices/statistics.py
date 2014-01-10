#-*-coding:utf-8-*-

from __future__ import division
import math

def mean(x):
    if len(x) == 0:
        raise ValueError
    return sum(x) / len(x)

def variance(x):
    if len(x) == 0:
        raise ValueError
    mx = mean(x)
    return sum([(i - mx) * (i - mx) for i in x]) / (len(x) - 1)

def stdev(x):
    return math.sqrt(variance(x))

def linear_regression(x, y):
    if len(x) != len(y):
        raise ValueError
    mx = mean(x)
    my = mean(y)
    sx = [i - mx for i in x]
    sy = [i - my for i in y]
    sxy = 0
    sxx = 0
    for _ in range(len(x)):
        sxy += sx[_] * sy[_]
        sxx += sx[_] * sx[_]
    b1 = sxy / sxx
    b0 = my - b1 * mx
    return b0, b1

if __name__ == '__main__':
    x = [10, 18, 25, 40, 50, 63, 42, 30, 5, 55]
    y = [25, 55, 50, 75, 110, 138, 90, 60, 10, 100]
    #y = [6.0, 14.0, 10.0, 14.0, 26.0]
    #x = [1.0, 3.0, 4.0, 5.0, 7.0]
    print(linear_regression(x, y))
