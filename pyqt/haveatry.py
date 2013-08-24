#coding:utf-8

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import ui_simpledialog

class TestDlg(QMainWindow, ui_simpledialog.Ui_MainWindow):
    def __init__(self, parent=None):
    	super(QMainWindow, self).__init__()
    	self.setupUi(self)
    	
if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	ex = TestDlg()
	ex.show()
	sys.exit(app.exec_())
    