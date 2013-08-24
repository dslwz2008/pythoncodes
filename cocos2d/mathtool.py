#code:utf-8
#define some math tools
import math
from cocos.euclid import Vector2

def radian2angle(radian):
    '''convert radian to angle unit'''
    return radian * 180 / math.pi
    
def angle2radian(angle):
    '''convert angle to radian unit'''
    return angle * math.pi / 180
    
def get_angle_of_2vectors(v1, v2):
    '''get angle of 2 vectors passed in'''
    cos = v1.dot(v2)/(v1.magnitude()*v2.magnitude())
    radian = math.acos(cos)
    return radian2angle(radian)
