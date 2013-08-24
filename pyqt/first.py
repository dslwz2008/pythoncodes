__author__ = 'shenshen'

import sys
from PyQt4 import QtGui,QtCore

class Main(QtGui.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()

    def keyPressEvent(self,event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()



app = QtGui.QApplication(sys.argv)
ex = Main()
ex.show()
sys.exit(app.exec_())
