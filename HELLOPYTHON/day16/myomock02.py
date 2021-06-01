import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import QtGui, uic, QtWidgets
from PyQt5.Qt import QPushButton, QSize, QRect
from tensorflow.keras.models import load_model
import numpy as np
from astropy.time.utils import split

model = load_model('models/20201213_202430.h5')
def getComIJ(arr2D):
    input = np.zeros((20,20))
    
    for i in range(20):
        for j in range(20):
            if arr2D[i][j] == 1:
                input[i][j] = 1
            if arr2D[i][j] == 2:
                input[i][j] = -1
            
    input = input.reshape((1,20,20,1))
    output = model.predict(input).squeeze()
    output = output.reshape((20, 20))
    for i in range(20):
        for j in range(20):
            if arr2D[i][j] > 0:
                output[i][j] = 0
    i, j = np.unravel_index(np.argmax(output), output.shape)
                
    return i,j

form_class = uic.loadUiType("myomock02.ui")[0]
#filename에 바로 실행시킬 파일명을 입력하면 됨
class MyWindow(QMainWindow, form_class):
    def __init__(self): 
        super().__init__()
        self.setupUi(self)
        self.flag_wb = True
        self.flag_go = True
        self.arr2D = [
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],

                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],

                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],

                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0]
            ]
        
        self.pb2D = []
        
        for i in range(20):
            pb_line = []
            for j in range(20):
                tmp = QPushButton(self)
                tmp.setToolTip(str(i) + "," + str(j))
                tmp.setIconSize(QSize(40,40))
                tmp.setGeometry(QRect((j*40),(i*40),40,40))
                tmp.setIcon(QtGui.QIcon('0.png'))
                tmp.clicked.connect(self.btnClick)
                pb_line.append(tmp)
            self.pb2D.append(pb_line)
        self.rs.clicked.connect(self.myreset)
        self.myrender()
        
    def myreset(self):
        self.flag_go = True
        self.flag_wb = True
        
        for i in range(20):
            for j in range(20):
                self.arr2D[i][j] = 0
        
        self.myrender()
        
    def myrender(self):
        for i in range(20):
            for j in range(20):
                if self.arr2D[i][j] == 0:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('0.png'))
                elif self.arr2D[i][j] == 1:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('1.png'))
                elif self.arr2D[i][j] == 2:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('2.png'))
            
        
        
    def btnClick(self):
        if not self.flag_go:
            return
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
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
        
        d1 = up + 1 + dw
        d2 = lf + 1 + rg
        d3 = uplf + 1 + dwrg
        d4 = uprg + 1 + dwlf
        
        self.myrender()
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5 :
            QtWidgets.QMessageBox.about(self, 'GAME OVER', 'BLACK WIN!')
            self.flag_go = False
            return
                
        self.flag_wb = not self.flag_wb
        
        com_i,com_j = getComIJ(self.arr2D)
        
        print(com_i,",", com_j)
        
        stone = 2
        self.arr2D[com_i][com_j] = 2
        
        up = self.getUP(com_i,com_j,stone)
        dw = self.getDW(com_i,com_j,stone)
        lf = self.getLF(com_i,com_j,stone)
        rg = self.getRG(com_i,com_j,stone)
        uplf = self.getUPLF(com_i,com_j,stone)
        dwrg = self.getDWRG(com_i,com_j,stone)
        uprg = self.getUPRG(com_i,com_j,stone)
        dwlf = self.getDWLF(com_i,com_j,stone)
        
        d1 = up + 1 + dw
        d2 = lf + 1 + rg
        d3 = uplf + 1 + dwrg
        d4 = uprg + 1 + dwlf
        
        self.myrender()
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5 :
            QtWidgets.QMessageBox.about(self, 'GAME OVER', 'WHITE WIN!')
            self.flag_go = False
                
        self.flag_wb = not self.flag_wb
    
    

    
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
    sys.exit(app.exec_())