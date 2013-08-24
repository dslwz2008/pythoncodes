#-*-coding:utf-8-*-
__author__ = 'Administrator'


class AAA(object):
    @classmethod
    def clsmethod(cls):
        print 'class method: ' + cls.__name__

    @staticmethod
    def stmethod():
        print 'static method'

class BBB(AAA):
    pass


if __name__ == '__main__':
    print AAA.clsmethod()
    print AAA.stmethod()
    a = AAA()
    print a.clsmethod()
    print a.stmethod()

    print BBB.clsmethod()
    print BBB.stmethod()
    b = BBB()
    print b.clsmethod()
    print b.stmethod()
