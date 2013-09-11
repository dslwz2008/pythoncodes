#-*-coding:utf-8-*-
__author__ = 'shenshen'

import turtle
import random

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(60)
        drawSpiral(myTurtle, lineLen - 1)

def tree(branchLen, t):
    if branchLen > 5:
        #t.width(branchLen)
        t.forward(branchLen)
        t.right(random.randint(15, 45))
        tree(branchLen - 15, t)
        t.left(random.randint(15, 45))
        tree(branchLen - 15, t)
        t.right(random.randint(15, 45))
        t.backward(branchLen)

#drawSpiral(myTurtle, 100)
#myWin.exitonclick()
def main1():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

def drawTriangle(points,color,myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,degree,myTurtle):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    drawTriangle(points,colormap[degree],myTurtle)
    if degree > 0:
        sierpinski([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)

def main2():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   myPoints = [[-100,-50],[0,100],[100,-50]]
   sierpinski(myPoints, 3, myTurtle)
   myWin.exitonclick()

import os
import os.path

def printDir(path, prefixlen, level):
    if level == 0:
        return
    contents = os.listdir(path)
    for i in contents:
        content = path + i
        if os.path.isfile(content):
            print('\t' * prefixlen + i)
        if os.path.isdir(content):
            print('\t' * prefixlen + i)
            printDir(content+'/', prefixlen + 1, level - 1)

def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

if __name__ == '__main__':
    #main2()
    #printDir('/Users/shenshen/Downloads/', 1, 2)
    moveTower(3,"A","B","C")

