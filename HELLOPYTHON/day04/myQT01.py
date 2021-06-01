import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("myQT01.ui")[0]
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
    def btnClick(self): 
        self.lbl.setText("good evening")
        print("버튼이 클릭되었습니다.")
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()