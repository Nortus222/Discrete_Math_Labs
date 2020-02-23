
from PyQt5 import QtCore, QtGui, QtWidgets
from Lab8002 import Ui_Window_2
import os


class Ui_Window_4(object):

    X = set()
    Y = set()
    Z = set()
    U = set()

    i = 0
    j = 0
    c = set()
    cwd = os.getcwd()
    def setupUi(self, MainWindow):

        
        MainWindow.setFixedSize(630, 460)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        
        self.label_X = QtWidgets.QLabel(self.centralwidget)
        self.label_X.setGeometry(QtCore.QRect(20, 20, 60, 16))
        
        self.label_Y = QtWidgets.QLabel(self.centralwidget)
        self.label_Y.setGeometry(QtCore.QRect(20, 50, 60, 16))
        
        self.label_tX = QtWidgets.QLabel(self.centralwidget)
        self.label_tX.setGeometry(QtCore.QRect(60, 20, 60, 16))
        
        self.label_tY = QtWidgets.QLabel(self.centralwidget)
        self.label_tY.setGeometry(QtCore.QRect(60, 50, 60, 16))
        
        self.label_Z = QtWidgets.QLabel(self.centralwidget)
        self.label_Z.setGeometry(QtCore.QRect(20, 90, 60, 16))
        
        self.label_tZ = QtWidgets.QLabel(self.centralwidget)
        self.label_tZ.setGeometry(QtCore.QRect(60, 90, 60, 16))
        
        self.X = Ui_Window_2.Uw2 - Ui_Window_2.Aw2
        self.Y = Ui_Window_2.Cw2

        self.pushButton_calc = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_calc.setGeometry(QtCore.QRect(10, 130, 113, 32))
        self.pushButton_calc.clicked.connect(lambda: self.simDiff(self.X, self.Y))
        
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(10, 180, 113, 32))
        self.pushButton_save.clicked.connect(self.saveButtonClicked)
        
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
        self.label_X.setText(_translate("MainWindow", "X = "))
        self.label_Y.setText(_translate("MainWindow", "Y = "))
        self.label_tX.setText(_translate("MainWindow", str(self.X)))
        self.label_tX.adjustSize()
        self.label_tY.setText(_translate("MainWindow", str(self.Y)))
        self.label_tY.adjustSize()
        self.label_Z.setText(_translate("MainWindow", "Z = "))
        self.label_tZ.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_calc.setText(_translate("MainWindow", "Розрахувати"))
        self.pushButton_save.setText(_translate("MainWindow", "Зберегти"))

    def simDiff(self, a, b):
        a = list(a)
        b = list(b)

        self.res = []

        for self.i in a:
            if self.i not in b and self.i not in self.res:
                self.res.append(self.i)

        for self.j in b:
            if self.j not in a and self.j not in self.res:
                self.res.append(self.j)

        self.res = set(self.res)
        self.label_tZ.setText(str(self.res))
        self.label_tZ.adjustSize()
        self.i += 1

    def saveButtonClicked(self):
        if self.i < 1:
            self.statusbar.setStyleSheet("color: red")
            self.statusbar.showMessage("Спочатку розрахуйте Z", 5000)
        else:
            with open(str(self.cwd) + "/Z_self.txt", "w", encoding="utf-8") as w:
                w.write("Z = " + str(self.label_tZ.text()))
                self.statusbar.setStyleSheet("color: green")
            self.statusbar.showMessage("Данні збережено", 10000)

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Window_4()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
