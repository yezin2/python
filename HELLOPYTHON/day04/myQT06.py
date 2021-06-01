import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("myQT06.ui")[0]
#filename에 바로 실행시킬 파일명을 입력하면 됨

class MyWindow(QMainWindow, form_class):
    def __init__(self): 
        super().__init__() 
        self.setupUi(self) 
        self.pb.clicked.connect(self.pbClick)
    def pbClick(self): 
        a = int(self.le1.text())
        b = int(self.le2.text())
        sum = 0
        for i in range(a,b+1):
            if((i%2) == 0) :
                sum += i
        self.le3.setText(str(sum))
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()