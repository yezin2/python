import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtGui, uic, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap
from Cython.Compiler.Naming import self_cname
from conda.common._logic import TRUE

form_class = uic.loadUiType("myomock02.ui")[0]
#filename에 바로 실행시킬 파일명을 입력하면 됨
class MyWindow(QMainWindow, form_class):
    def __init__(self): 
        super().__init__()
        self.setupUi(self)
        self.flag_wb = True
        self.flag_go = True
        self.arr2D = self.arr2D = [[0 for col in range(20)] for row in range(20)]
        
        self.arr_seq = [
            {'i' : 0, 'j':0},
            {'i' : 0, 'j':1},
            {'i' : 0, 'j':2},
            {'i' : 0, 'j':3},
            {'i' : 0, 'j':4}
            ]
        self.arr_idx = 0
        
        self.pb2D = []
        
        self.rs.clicked.connect(self.resetClick)
        for i in range(0,20):
            pb_line = []
            for j in range(0,20):
                tmp = QPushButton(self)
                tmp.setToolTip(str(i) + "," + str(j))
                tmp.setGeometry(QRect((j*40),(i*40),40,40))
                tmp.setIconSize(QSize(40,40))
                tmp.setIcon(QtGui.QIcon('0.png'))
                tmp.clicked.connect(self.btnClick)
                
                pb_line.append(tmp)
            self.pb2D.append(pb_line)
        
        
    def myrender(self):
        for i in range(0,20):
            for j in range(0,20):
                if self.arr2D[i][j] == 0:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('0.png'))
                elif self.arr2D[i][j] == 1:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('1.png'))
                elif self.arr2D[i][j] == 2:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('2.png'))
            
        
        
    def btnClick(self):
        if self.flag_go == False:
            return
        bang = self.sender().toolTip()
        i = int(bang[0:1])
        j = int(bang[2:3])
        
        if self.arr2D[i][j] > 0:
            return
        
        stone = 1
        self.arr2D[i][j] = 1
        
        up = self.getUP(i,j,stone)
        dw = self.getDW(i,j,stone)
        lf = self.getLF(i,j,stone)
        rg = self.getRG(i,j,stone)
        uplf = self.getUPLF(i,j,stone)
        dwrg = self.getDWRG(i,j,stone)
        uprg = self.getUPRG(i,j,stone)
        dwlf = self.getDWLF(i,j,stone)
        
        self.myrender()
        
        if (up+dw+1) == 5 or (lf+rg+1) == 5 or (uplf+dwrg+1) == 5 or (uprg+dwlf+1) == 5 :
            QtWidgets.QMessageBox.about(self, 'GAME OVER', 'BLACK WIN!')
            self.flag_go = False
            return
                
        self.flag_wb = not self.flag_wb
        
        com_i = self.arr_seq[self.arr_idx]['i']
        com_j = self.arr_seq[self.arr_idx]['j']
        stone = 2
        self.arr2D[com_i][com_j] = 2
        self.arr_idx += 1
        
        up = self.getUP(com_i,com_j,stone)
        dw = self.getDW(com_i,com_j,stone)
        lf = self.getLF(com_i,com_j,stone)
        rg = self.getRG(com_i,com_j,stone)
        uplf = self.getUPLF(com_i,com_j,stone)
        dwrg = self.getDWRG(com_i,com_j,stone)
        uprg = self.getUPRG(com_i,com_j,stone)
        dwlf = self.getDWLF(com_i,com_j,stone)
        
        self.myrender()
        
        if (up+dw+1) == 5 or (lf+rg+1) == 5 or (uplf+dwrg+1) == 5 or (uprg+dwlf+1) == 5 :
            QtWidgets.QMessageBox.about(self, 'GAME OVER', 'WHITE WIN!')
            self.flag_go = False
                
        self.flag_wb = not self.flag_wb
    
    def resetClick(self):
        self.flag_go = True
        self.flag_wb = True
        for i in range(0,20):
            for j in range(0,20):
                self.arr2D[i][j] = 0
        
        self.arr_idx = 0
        self.myrender()
    
    def getUP(self, i, j, stone):
        cnt = 0
        try :
            while True:
                i += -1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else : 
                    return cnt
        except :
            return cnt
    
    def getDW(self, i, j, stone):
        cnt = 0
        try :
            while True:
                i += 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else : 
                    return cnt
        except :
            return cnt
        
    def getLF(self, i, j, stone):
        cnt = 0
        try :
            while True:
                j += -1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else : 
                    return cnt
        except :
            return cnt
        
    def getRG(self, i, j, stone):
        cnt = 0
        try :
            while True:
                j += 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else : 
                    return cnt
        except :
            return cnt
    
    def getUPLF(self, i, j, stone):
        cnt = 0
        try :
            while True:
                i += -1
                j += -1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else : 
                    return cnt
        except :
            return cnt
    
    def getDWRG(self, i, j, stone):
        cnt = 0
        try :
            while True:
                i += 1
                j += 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else : 
                    return cnt
        except :
            return cnt
        
    def getDWLF(self, i, j, stone):
        cnt = 0
        try :
            while True:
                i += 1
                j += -1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else : 
                    return cnt
        except :
            return cnt
        
    def getUPRG(self, i, j, stone):
        cnt = 0
        try :
            while True:
                i += -1
                j += 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else : 
                    return cnt
        except :
            return cnt

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()