#coding:utf-8
import math

class Vector3(object):
    'class for computing Vector3'
    version = 0.1
    
    def __init__(self, x=0, y=0, z=0):
        self._x = x
        self._y = y
        self._z = z
        
    def __mul__(self, value):
        return Vector3(value * self._x, value * self._y, value * self._z)
        
    def __str__(self):
        return 'x: %s, y: %s, z:%s'%(self._x, self._y, self._z)
    
    def dot(self, vector):
        return self._x * vector.x + \
        self._y * vector.y + \
        self._z * vector.z
    
    def cross(self,  vector):
        return Vector3(self._y * vector.z - self._z * vector.y, 
                       self._z * vector.x - self._x * vector.z, 
                       self._x * vector.y - self._y * vector.x)
        
    def magnitude(self):
        return math.sqrt(self._x**2 + self._y**2 + self._z**2)
        
    def projectiononto(self, vector):
        return vector * (self.dot(vector) / vector.magnitude()**2)
        
    @property
    def x(self):
        return self._x
        
    @x.setter
    def x(self, value):
        self._x = value
    
    @property
    def y(self):
        return self._y
        
    @y.setter
    def y(self, value):
        self._y = value
        
    @property
    def z(self):
        return self._z
        
    @z.setter
    def z(self, value):
        self._z = value
        
 #   @x.deleter
 #   def x(self):
 #       del self._x

def test():
    vector = Vector3()
    #print vector
    print dir(Vector3)
    v1 = Vector3(1, 2, 3)
    print v1.x
    v1.x = 99
    print v1.__dict__
    #del v1.x
    #print v1.__dict__
    #print v1.x
    p = Vector3(2, 2, 1)
    q = Vector3(1, -2, 0)
    print p.dot(q)
    print p.cross(q)
    print p.projectiononto(q)

if __name__ == '__main__':
    test()
