#-*-coding:utf-8-*-
__author__ = 'shenshen'

from euclid import Vector2

states = [Vector2(0,0), Vector2(0,1), Vector2(0,2), Vector2(0,3),
    Vector2(1,1), Vector2(2,2), Vector2(3,0), Vector2(3,1),
    Vector2(3,2), Vector2(3,3)]
decisions = [Vector2(0,2), Vector2(1,1), Vector2(2,0), Vector2(0,1), Vector2(1,0)]

start_state = Vector2(3,3)
end_state = Vector2(0,0)
#经过的路径
passed = []
path = []

def cross_river(state, coefficient):
    if state == end_state:
        return True

    for d in decisions:
        newstate = state + coefficient * d
        #路过的点要记录下来，以免重复造成无限循环
        if newstate not in states or [state, newstate] in passed\
            or [newstate, state] in passed:
            continue
        else:
            passed.append([state, newstate])
            if cross_river(newstate, -coefficient):
                path.append(newstate)
                return True
    return False

if __name__ == '__main__':
    cross_river(start_state, -1)
    path.append(start_state)
    while len(path) > 0:
        print(path.pop())
