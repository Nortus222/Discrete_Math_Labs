
from PyQt5 import QtCore, QtGui, QtWidgets
import io
from Lab8002 import Ui_Window_2
import os, re

class Ui_Window_5(object):

    D_short = set()
    D_long = set()
    Z_self = set()
    Z_py = set()

    X = set()
    Y = set()

    cwd = os.getcwd()

    def setupUi(self, MainWindow):
        
        MainWindow.setFixedSize(630, 440)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        
        self.label_Dshort = QtWidgets.QLabel(self.centralwidget)
        self.label_Dshort.setGeometry(QtCore.QRect(20, 30, 111, 16))
        
        self.label_Dlong = QtWidgets.QLabel(self.centralwidget)
        self.label_Dlong.setGeometry(QtCore.QRect(20, 60, 101, 16))
        
        self.label_Zself = QtWidgets.QLabel(self.centralwidget)
        self.label_Zself.setGeometry(QtCore.QRect(20, 180, 81, 16))
        
        self.label_Zpy = QtWidgets.QLabel(self.centralwidget)
        self.label_Zpy.setGeometry(QtCore.QRect(20, 210, 81, 16))
        
        self.pushButton_Dcheck = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Dcheck.setGeometry(QtCore.QRect(10, 120, 113, 32))
        self.pushButton_Dcheck.clicked.connect(self.dCheck)
        
        self.pushButton_Zcheck = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Zcheck.setGeometry(QtCore.QRect(10, 270, 113, 32))
        self.pushButton_Zcheck.clicked.connect(self.zCheck)

        self.pushButton_Dload = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Dload.setGeometry(QtCore.QRect(10, 90, 113, 32))
        self.pushButton_Dload.clicked.connect(self.dLoad)
        
        self.pushButton_Zload = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Zload.setGeometry(QtCore.QRect(10, 240, 113, 32))
        self.pushButton_Zload.clicked.connect(self.zLoad)
        
        self.label_Dcheck = QtWidgets.QLabel(self.centralwidget)
        self.label_Dcheck.setGeometry(QtCore.QRect(125, 127, 60, 16))
        
        self.label_Zcheck = QtWidgets.QLabel(self.centralwidget)
        self.label_Zcheck.setGeometry(QtCore.QRect(125, 277, 60, 16))

        self.label_tDlong = QtWidgets.QLabel(self.centralwidget)
        self.label_tDlong.setGeometry(QtCore.QRect(140, 30, 60, 16))
        
        self.label_tDshort = QtWidgets.QLabel(self.centralwidget)
        self.label_tDshort.setGeometry(QtCore.QRect(130, 60, 60, 16))
        
        self.label_tZself = QtWidgets.QLabel(self.centralwidget)
        self.label_tZself.setGeometry(QtCore.QRect(100, 180, 60, 16))
        
        self.label_tZpy = QtWidgets.QLabel(self.centralwidget)
        self.label_tZpy.setGeometry(QtCore.QRect(100, 210, 60, 16))
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 630, 22))
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_Dshort.setText(_translate("MainWindow", "D(початкове)  ="))
        self.label_Dlong.setText(_translate("MainWindow", "D(спрощене) = "))
        self.label_Zself.setText(_translate("MainWindow", "Z(ручна) = "))
        self.label_Zpy.setText(_translate("MainWindow", "Z(python) = "))
        self.pushButton_Dcheck.setText(_translate("MainWindow", "Порівняти"))
        self.pushButton_Zcheck.setText(_translate("MainWindow", "Порівняти"))
        self.label_Dcheck.setText(_translate("MainWindow", ""))
        self.label_Zcheck.setText(_translate("MainWindow", ""))
        self.label_tDlong.setText(_translate("MainWindow", ""))
        self.label_tDshort.setText(_translate("MainWindow", ""))
        self.label_tZself.setText(_translate("MainWindow", ""))
        self.label_tZpy.setText(_translate("MainWindow", ""))
        self.pushButton_Dload.setText(_translate("MainWindow", "Завантажити"))
        self.pushButton_Zload.setText(_translate("MainWindow", "Завантажити"))

    def dLoad(self):
        print(self.cwd)
        with open(str(self.cwd) + "/D_Long.txt", "r", encoding="utf-8") as w:
            self.D_long = w.readline()
        with open(str(self.cwd) + "/D_Short.txt", "r", encoding="utf-8") as w:
            self.D_short = w.readline()
        
        self.label_tDlong.setText(str(self.D_long))
        self.label_tDlong.adjustSize()
        self.label_tDshort.setText(str(self.D_short))
        self.label_tDshort.adjustSize()
        
    def zLoad(self):
        with open(str(self.cwd) + "/Z_self.txt", "r", encoding="utf-8") as w:
            w.seek(4, io.SEEK_SET)
            self.Z_self = w.readline()
        self.label_tZself.setText(str(self.Z_self))
        self.label_tZself.adjustSize()

        self.X = Ui_Window_2.Uw2 - Ui_Window_2.Aw2
        self.Y = Ui_Window_2.Cw2
        self.Z_py = self.X ^ self.Y
        self.label_tZpy.setText(str(self.Z_py))
        self.label_tZpy.adjustSize()

    def dCheck(self):
        if self.label_tDlong.text() == "":
            self.statusbar.setStyleSheet("color: red")
            self.statusbar.showMessage("Спочатку завантажте множини", 5000)
        else: 
            if self.checking(self.D_short, self.D_long):
                self.label_Dcheck.setText("Співпадає")
                self.label_Dcheck.adjustSize()
                self.label_Dcheck.setStyleSheet("background-color: green; color: white")
            else:
                self.label_Dcheck.setText("Не співпадає")
                self.label_Dcheck.adjustSize()
                self.label_Dcheck.setStyleSheet("background-color: red; color: white")

    def zCheck(self):
        if self.label_tZself == "":
            self.statusbar.setStyleSheet("color: red")
            self.statusbar.showMessage("Спочатку завантажте множини", 5000)
            
        else:
            if self.checking(self.Z_py, self.Z_self):
                self.label_Zcheck.setText("Співпадає")
                self.label_Zcheck.adjustSize()
                self.label_Zcheck.setStyleSheet("background-color: green; color: white")
            else:
                self.label_Zcheck.setText("Не співпадає")
                self.label_Zcheck.adjustSize()
                self.label_Zcheck.setStyleSheet("background-color: red; color: white")

    def checking(self, a, b):
        a = str(a)
        b = str(b)
        self.bl = []
        self.al = []
        self.t = True

        if len(a) == len(b):
            self.bw = re.findall(r'\d{1,3}', b)
            self.aw = re.findall(r'\d{1,3}', a)
            print(self.bw)
            print(self.aw)

            for i, j in zip(self.bw, self.aw):
                self.bl.append(i)
                self.al.append(j)

            for i,j in zip(sorted(self.bl), sorted(self.al)):
                if i != j:
                    self.t = False
        else:
            self.t = False
        return self.t    


            



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Window_5()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
