import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("myQT07.ui")[0]
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
        if(d < 0.33):
            b = "가위"
        elif(d >= 0.33 and d < 0.66) :
            b = "바위"
        elif(d >= 0.66) :
            b = "보"
        
        if(a == "가위") :
            if(b == "가위") :
                c = "DRAW--"
            elif(b == "바위") :
                c = "LOSE..."
            elif(b == "보") :
                c = "WIN!"
        elif(a == "바위") :
            if(b == "가위") :
                c = "WIN!"
            elif(b == "바위") :
                c = "DRAW--"
            elif(b == "보") :
                c = "LOSE..."
        elif(a == "보") :
            if(b == "가위") :
                c = "LOSE..."
            elif(b == "바위") :
                c = "WIN!"
            elif(b == "보") :
                c = "DRAW--"
        
        self.le2.setText(str(b))
        self.le3.setText(str(c))
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()