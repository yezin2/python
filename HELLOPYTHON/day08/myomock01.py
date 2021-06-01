import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtGui, uic, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap
from Cython.Compiler.Naming import self_cname

form_class = uic.loadUiType("myomock01.ui")[0]
#filename에 바로 실행시킬 파일명을 입력하면 됨
class MyWindow(QMainWindow, form_class):
    def __init__(self): 
        super().__init__()
        self.setupUi(self)
        self.sunseo = 1;
        self.arr2D = [
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0]                        
                    ]
        self.pb2D = []
        for i in range(0,10):
            pb_line = []
            for j in range(0,10):
                tmp = QPushButton(self)
                tmp.setToolTip(str(i) + "," + str(j))
                tmp.setGeometry(QRect((j*40),(i*40),40,40))
                tmp.setIconSize(QSize(40,40))
                tmp.setIcon(QtGui.QIcon('0.png'))
                tmp.clicked.connect(self.btnClick)
                
                pb_line.append(tmp)
            self.pb2D.append(pb_line)
        
        
    def myrender(self):
        self.sunseo = self.sunseo + 1
        for i in range(0,10):
            for j in range(0,10):
                if self.arr2D[i][j] == 0:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('0.png'))
                elif self.arr2D[i][j] == 1:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('1.png'))
                elif self.arr2D[i][j] == 2:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('2.png'))
            
        
        
    def btnClick(self):
        bang = self.sender().toolTip()
        i = int(bang[0:1])
        j = int(bang[2:3])
        
        if self.arr2D[i][j] > 0:
            return
        elif self.arr2D[i][j] == 0:
            self.arr2D[i][j] = (self.sunseo%2)+1
            
        
        self.myrender()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()