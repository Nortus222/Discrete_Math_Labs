
from PyQt5 import QtCore, QtGui, QtWidgets
from Lab8002 import Ui_Window_2
import os

class Ui_Window_3(object):
    A = set()
    B = set()
    C = set()
    U = set()
    final = set()
    i = 0
    cwd = os.getcwd()
    def setupUi(self, MainWindow):

        
        MainWindow.setFixedSize(630, 460)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
       
        self.label_C = QtWidgets.QLabel(self.centralwidget)
        self.label_C.setGeometry(QtCore.QRect(20, 80, 60, 16))
        
        self.label_tC = QtWidgets.QLabel(self.centralwidget)
        self.label_tC.setGeometry(QtCore.QRect(60, 80, 60, 16))
        
        self.label_B = QtWidgets.QLabel(self.centralwidget)
        self.label_B.setGeometry(QtCore.QRect(20, 50, 60, 16))
        
        self.label_tA = QtWidgets.QLabel(self.centralwidget)
        self.label_tA.setGeometry(QtCore.QRect(60, 20, 60, 16))
       
        self.label_tB = QtWidgets.QLabel(self.centralwidget)
        self.label_tB.setGeometry(QtCore.QRect(60, 50, 60, 16))
        
        self.label_D = QtWidgets.QLabel(self.centralwidget)
        self.label_D.setGeometry(QtCore.QRect(20, 110, 60, 16))
        
        self.label_A = QtWidgets.QLabel(self.centralwidget)
        self.label_A.setGeometry(QtCore.QRect(20, 20, 60, 16))
        
        self.label_tD = QtWidgets.QLabel(self.centralwidget)
        self.label_tD.setGeometry(QtCore.QRect(50, 110, 60, 16))
        
        self.label_func = QtWidgets.QLabel(self.centralwidget)
        self.label_func.setGeometry(QtCore.QRect(20, 150, 101, 31))
        
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(20, 240, 113, 32))
        self.pushButton_save.clicked.connect(self.saveButtonClicked)
        
        self.label_tStep = QtWidgets.QLabel(self.centralwidget)
        self.label_tStep.setGeometry(QtCore.QRect(150, 200, 60, 16))
        
        self.pushButton_step = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_step.setGeometry(QtCore.QRect(20, 190, 113, 32))
        self.pushButton_step.clicked.connect(self.func_short)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 630, 22))
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        
        MainWindow.setStatusBar(self.statusbar)

        self.A = Ui_Window_2.Aw2
        self.B = Ui_Window_2.Bw2
        self.C = Ui_Window_2.Cw2
        self.U = Ui_Window_2.Uw2

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_C.setText(_translate("MainWindow", "C = "))
        self.label_tC.setText(_translate("MainWindow", str(self.C)))
        self.label_tC.adjustSize()
        self.label_B.setText(_translate("MainWindow", "B = "))
        self.label_tA.setText(_translate("MainWindow", str(self.A)))
        self.label_tA.adjustSize()
        self.label_tB.setText(_translate("MainWindow", str(self.B)))
        self.label_tB.adjustSize
        self.label_D.setText(_translate("MainWindow", "D = "))
        self.label_A.setText(_translate("MainWindow", "A ="))
        self.label_tD.setText(_translate("MainWindow", "TextLabel"))
        self.label_func.setText(_translate("MainWindow", "D = B ∩ (A ∪ C)"))
        self.pushButton_save.setText(_translate("MainWindow", "Зберегти"))
        self.label_tStep.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_step.setText(_translate("MainWindow", "Крок"))

    def func_short(self):
        if self.i == 0:
            self.D_short = "{} ∩ ({} ∪ {})".format(self.B, self.A, self.C)
            self.label_tD.setText(str(self.D_short))
            self.label_tD.adjustSize()
            self.aUnionC = self.A | self.C
            self.label_tStep.setText("A ∪ C = {} ∪ {} = {}".format(self.A, self.C, self.aUnionC))
            self.label_tStep.adjustSize()
            self.i += 1
        elif self.i == 1:
            self.final = (self.B & self.aUnionC)
            self.label_tStep.setText("B ∩ (A ∪ C) = {} ∩ {} = {}".format(self.B, self.aUnionC, self.final))
            self.label_tStep.adjustSize()
            self.label_func.setText(self.label_func.text() + " = " + str(self.final))
            self.label_func.adjustSize()
            self.label_tD.setText(self.label_tD.text() + " = " + str(self.final))
            self.label_tD.adjustSize()
            self.i += 1
            
    def saveButtonClicked(self):
        if self.i < 2:
            self.statusbar.setStyleSheet("color: red")
            self.statusbar.showMessage("Спочатку зробіть всі кроки", 5000)
        else:
            with open(str(self.cwd) + "/D_Short.txt", "w", encoding="utf-8") as w:
                w.write(str(self.final) + "\n")
                w.write("D = " + str(self.label_tD.text()) + "\n")
                w.write(str(self.label_func.text()) + "\n")
                self.statusbar.setStyleSheet("color: green")
            self.statusbar.showMessage("Данні збережено", 10000)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Window_3()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
