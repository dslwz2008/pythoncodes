#-*-coding:utf-8-*-
__author__ = 'shenshen'

import turtle
import random
import timeit
import os
import os.path

#recursion practices
#1.Write a recursive function to compute the factorial of a number.
def fractorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * fractorial(num - 1)

#2.Write a recursive function to reverse a list.
def reverse(alist):
    if len(alist) == 1:
        return alist[0]
    else:
        return reverse(alist[1:]) + alist[0]

#3.
def tree(branchLen, t):
    if branchLen > 5:
        oldwidth = t.width()
        t.width(oldwidth - 2.5)
        t.forward(branchLen)
        angle = random.randint(15, 45)
        subtract = random.randint(5, 20)
        t.right(angle)
        tree(branchLen - subtract, t)
        t.left(angle * 2)
        tree(branchLen - subtract, t)
        t.right(angle)
        t.backward(branchLen)
        t.width(oldwidth)

def drawtree():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    t.width(20)
    tree(75,t)
    myWin.exitonclick()

#4.Find or invent an algorithm for drawing a fractal mountain. Hint: One approach to this uses triangles again.
#5.Write a recursive function to compute the Fibonacci sequence. How does the performance of the recursive function compare to that of an iterative version?
def fibonacci_rec(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

def fibonacci_ite(n):
    fab = [0] * (n + 1)
    fab[0] = 0
    fab[1] = 1
    for i in range(2, n + 1):
        fab[i] = fab[i - 1] + fab[i - 2]
    return fab[n]

# for i in [10, 100, 1000, 10000]:
#     fab_rec = timeit.Timer("fibonacci_rec(%d)" % i, "from __main__ import fibonacci_rec")
#     rec_time = fab_rec.timeit(number=100)
#     fab_ite = timeit.Timer("fibonacci_ite(%d)" % i, "from __main__ import fibonacci_ite")
#     ite_time = fab_ite.timeit(number=100)
#     print("%d, %10.3f, %10.3f" % (i, rec_time, ite_time))
#     #递归的执行时间要比迭代多得多

#6.Implement a solution to the Tower of Hanoi using three stacks to keep track of the disks.
def hanoi(height,fromPole, toPole, withPole):
    if height >= 1:
        hanoi(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        hanoi(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

#7.Using the turtle graphics module, write a recursive program to display a Hilbert curve.
basicpoints = [(20, 80), (80, 80), (20, 80), (80, 80)]
def drawZ(level, pos):
    points = []
    if pos == 0:
        pass
    elif pos == 1:
        pass
    elif pos == 2:
        points = basicpoints
    elif pos == 3:
        pass

def drawHilbert(level):
    if level == 1:
        for i in range(0, 4):
            drawZ(1, i)
    else:
        for i in range(0, 4):
            drawHilbert(level - 1)

#8.Using the turtle graphics module, write a recursive program to display a Koch snowflake.

#9.Write a program to solve the following problem: You have two jugs:
# a 4-gallon jug and a 3-gallon jug. Neither of the jugs have markings on them.
# There is a pump that can be used to fill the jugs with water.
# How can you get exactly two gallons of water in the 4-gallon jug?


def listDirectory(dir, indent):
    lists = os.listdir(dir)
    for i in lists:
        filename = dir + '/' + i
        if os.path.isfile(filename):
            print('%s%s' % (' '*indent, i))
        elif os.path.isdir(filename):
            print('%s%s/' % (' '*indent, i))
            listDirectory(filename, indent + 4)


if __name__ == '__main__':
    listDirectory('/Users/shenshen/Pictures', 0)
    # print(fractorial(0))
    # print(fractorial(1))
    # print(fractorial(5))
    # print(fractorial(10))
    #print(reverse('12345'))
    #print(reverse('abcdefg'))
    #drawtree()
    # print(fibonacci_rec(5))
    # print(fibonacci_rec(10))
    # print(fibonacci_ite(5))
    # print(fibonacci_ite(10))
    # hanoi(3, 'A', 'C', 'B')