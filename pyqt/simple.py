#-*-coding:utf-8-*-
# simple.py
__author__ = 'Administrator'

import sys
from PyQt4 import QtGui
from PyQt4 import QtOpenGL

app = QtGui.QApplication(sys.argv)

widget = QtGui.QWidget()
widget.resize(250, 150)
widget.setWindowTitle('simple')
widget.show()

sys.exit(app.exec_())