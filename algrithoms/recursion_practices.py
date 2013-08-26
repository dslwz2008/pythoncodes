#-*-coding:utf-8-*-
__author__ = 'shenshen'

import turtle
import random

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


if __name__ == '__main__':
    # print(fractorial(0))
    # print(fractorial(1))
    # print(fractorial(5))
    # print(fractorial(10))
    #print(reverse('12345'))
    #print(reverse('abcdefg'))
    drawtree()