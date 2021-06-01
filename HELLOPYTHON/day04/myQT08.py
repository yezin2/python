import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("myQT08.ui")[0]
#filename에 바로 실행시킬 파일명을 입력하면 됨

class MyWindow(QMainWindow, form_class):
    def __init__(self): 
        super().__init__() 
        self.setupUi(self) 
        self.pb.clicked.connect(self.pbClick)
    def pbClick(self): 
        a = int(self.le1.text())
        res = ""
        for i in range(1,10):
            res += str(a) + " * " + str(i) + " = " + str(a*i) + "\n"
        
        self.te.setText(str(res))
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()