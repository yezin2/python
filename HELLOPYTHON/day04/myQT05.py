import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("myQT05.ui")[0]
#filename에 바로 실행시킬 파일명을 입력하면 됨

class MyWindow(QMainWindow, form_class):
    def __init__(self): 
        super().__init__() 
        self.setupUi(self) 
        self.pb.clicked.connect(self.pbClick)
    def pbClick(self): 
        a = self.le1.text()
        d = random.random()
        b = ""
        c = ""
        if(d < 0.5):
            b = "홀"
        else :
            b = "짝"
        
        if(a == b) :
            c = "WIN!"
        else :
            c = "LOSEㅠ"
        self.le2.setText(str(b))
        self.le3.setText(str(c))
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()