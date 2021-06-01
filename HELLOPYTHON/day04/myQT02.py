import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("myQT02.ui")[0]
#filename에 바로 실행시킬 파일명을 입력하면 됨

class MyWindow(QMainWindow, form_class):
#     def __init__(self):
#         super(MyWindow, self).__init__()
#         self.setupUi(self)
# class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self) 
        self.pb.clicked.connect(self.btnClick)
        self.a = 1
    def btnClick(self): 
        b = int(self.lbl.text())
        print(b)
        b+=1
        self.lbl.setText(str(b))
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()