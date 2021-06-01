import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtGui, uic, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap

form_class = uic.loadUiType("myQT01.ui")[0]
#filename에 바로 실행시킬 파일명을 입력하면 됨

class MyWindow(QMainWindow, form_class):
    def __init__(self): 
        super().__init__()
        self.index = 0
        self.setupUi(self) 
        self.pb.clicked.connect(self.btnClick)
        
        
    def btnClick(self): 
        self.index += 1
        loc_index = self.index % 3
        self.pb.setIcon(QtGui.QIcon(str(loc_index) + '.png'))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()