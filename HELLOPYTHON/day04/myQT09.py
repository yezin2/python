import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from tkinter import messagebox


form_class = uic.loadUiType("myQT09.ui")[0]
#filename에 바로 실행시킬 파일명을 입력하면 됨
class MyWindow(QMainWindow, form_class):
    res = ""
    def __init__(self): 
        super().__init__() 
        self.setupUi(self) 
        self.btn1.clicked.connect(self.btn1Click)
        self.btn2.clicked.connect(self.btn2Click)
        self.btn3.clicked.connect(self.btn3Click)
        self.btn4.clicked.connect(self.btn4Click)
        self.btn5.clicked.connect(self.btn5Click)
        self.btn6.clicked.connect(self.btn6Click)
        self.btn7.clicked.connect(self.btn7Click)
        self.btn8.clicked.connect(self.btn8Click)
        self.btn9.clicked.connect(self.btn9Click)
        self.btn0.clicked.connect(self.btn0Click)
        self.btnCall.clicked.connect(self.btnCallClick)
        print("@")
        
    def btn1Click(self): 
        print("@@")
        a = self.btn1.text()
        print("@@@")
        self.res = self.res + a
        print("@@@@")
        self.le1.setText(str(self.res))
        
    def btn2Click(self): 
        a = self.btn2.text()
        self.res += a
        self.le1.setText(str(self.res))
        
    def btn3Click(self): 
        a = self.btn3.text()
        self.res += a
        self.le1.setText(str(self.res))
        
    def btn4Click(self): 
        a = self.btn4.text()
        self.res += a
        self.le1.setText(str(self.res))
        
    def btn5Click(self): 
        a = self.btn5.text()
        self.res += a
        self.le1.setText(str(self.res))
        
    def btn6Click(self): 
        a = self.btn6.text()
        self.res += a
        self.le1.setText(str(self.res))
        
    def btn7Click(self): 
        a = self.btn7.text()
        self.res += a
        self.le1.setText(str(self.res))
        
    def btn8Click(self): 
        a = self.btn8.text()
        self.res += a
        self.le1.setText(str(self.res))
        
    def btn9Click(self): 
        a = self.btn9.text()
        self.res += a
        self.le1.setText(str(self.res))
        
    def btn0Click(self): 
        a = self.btn0.text()
        self.res += a
        self.le1.setText(str(self.res))
        
    def btnCallClick(self): 
        messagebox.showinfo(title="연결중", message=self.res + "전화거는중")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()