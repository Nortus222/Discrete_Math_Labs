
from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_Window_2(object):
    Aw2 = set()
    Bw2 = set()
    Cw2 = set()
    Uw2 = set()
    final = set()
    i = 0
    cwd = os.getcwd()
    def setupUi(self, MainWindow):
        
        MainWindow.setFixedSize(630, 460)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        
        self.label_A = QtWidgets.QLabel(self.centralwidget)
        self.label_A.setGeometry(QtCore.QRect(20, 20, 60, 16))
        
        self.label_B = QtWidgets.QLabel(self.centralwidget)
        self.label_B.setGeometry(QtCore.QRect(20, 50, 60, 16))
        
        self.label_C = QtWidgets.QLabel(self.centralwidget)
        self.label_C.setGeometry(QtCore.QRect(20, 80, 60, 16))
        
        self.label_D = QtWidgets.QLabel(self.centralwidget)
        self.label_D.setGeometry(QtCore.QRect(20, 110, 60, 16))
        
        self.label_func = QtWidgets.QLabel(self.centralwidget)
        self.label_func.setGeometry(QtCore.QRect(20, 140, 161, 31))
        
        self.pushButton_step = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_step.setGeometry(QtCore.QRect(20, 170, 113, 32))
        self.pushButton_step.clicked.connect(lambda: self.func_long(MainWindow))

        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(20, 300, 113, 32))
        self.pushButton_save.clicked.connect(self.saveButtonClicked)
        
        self.label_tA = QtWidgets.QLabel(self.centralwidget)
        self.label_tA.setGeometry(QtCore.QRect(60, 20, 60, 16))
        
        self.label_tB = QtWidgets.QLabel(self.centralwidget)
        self.label_tB.setGeometry(QtCore.QRect(60, 50, 60, 16))
        
        self.label_tC = QtWidgets.QLabel(self.centralwidget)
        self.label_tC.setGeometry(QtCore.QRect(60, 80, 60, 16))
        
        self.label_tD = QtWidgets.QLabel(self.centralwidget)
        self.label_tD.setGeometry(QtCore.QRect(50, 110, 60, 16))
        
        self.label_tStep = QtWidgets.QLabel(self.centralwidget)
        self.label_tStep.setGeometry(QtCore.QRect(150, 180, 60, 16))

        self.label_nA = QtWidgets.QLabel(self.centralwidget)
        self.label_nA.setGeometry(QtCore.QRect(20, 220, 60, 16))
        
        self.label_nB = QtWidgets.QLabel(self.centralwidget)
        self.label_nB.setGeometry(QtCore.QRect(20, 250, 60, 16))
        
        self.label_nC = QtWidgets.QLabel(self.centralwidget)
        self.label_nC.setGeometry(QtCore.QRect(20, 280, 60, 16))
        
        self.label_tnA = QtWidgets.QLabel(self.centralwidget)
        self.label_tnA.setGeometry(QtCore.QRect(60, 220, 60, 16))
        
        self.label_tnB = QtWidgets.QLabel(self.centralwidget)
        self.label_tnB.setGeometry(QtCore.QRect(60, 250, 60, 16))
        
        self.label_tnC = QtWidgets.QLabel(self.centralwidget)
        self.label_tnC.setGeometry(QtCore.QRect(60, 280, 60, 16))
        
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
        self.label_A.setText(_translate("MainWindow", "A ="))
        self.label_B.setText(_translate("MainWindow", "B = "))
        self.label_C.setText(_translate("MainWindow", "C = "))
        self.label_D.setText(_translate("MainWindow", "D = "))
        self.label_func.setText(_translate("MainWindow", "D =  ̅((A ̅ ∪ B ̅) ∩ (B ̅ ∪ C ̅))"))
        self.pushButton_step.setText(_translate("MainWindow", "Крок"))
        self.pushButton_save.setText(_translate("MainWindow", "Зберегти"))
        self.label_tA.setText(_translate("MainWindow", str(self.Aw2)))
        self.label_tA.adjustSize()
        self.label_tB.setText(_translate("MainWindow", str(self.Bw2)))
        self.label_tB.adjustSize()
        self.label_tC.setText(_translate("MainWindow", str(self.Cw2)))
        self.label_tC.adjustSize()
        self.label_tD.setText(_translate("MainWindow", ""))
        self.label_tStep.setText(_translate("MainWindow", ""))
        self.label_nA.setText(_translate("MainWindow", " ̅A = "))
        self.label_nB.setText(_translate("MainWindow", " ̅B = "))
        self.label_nC.setText(_translate("MainWindow", " ̅C = "))
        self.label_tnA.setText(_translate("MainWindow", ""))
        self.label_tnB.setText(_translate("MainWindow", ""))
        self.label_tnC.setText(_translate("MainWindow", ""))

    def func_long(self, MainWindow):
        if self.i == 0:
            self.D_long = "  ̅(({} ̅ ∪ {} ̅) ∩ ({} ̅ ∪ {} ̅))".format(self.Aw2, self.Bw2, self.Bw2, self.Cw2)
            self.label_tD.setText(self.D_long)
            self.label_tD.adjustSize()
            self.uMinusA = self.Uw2 - self.Aw2
            self.label_tStep.setText(" ̅A = {} \\ {} = {}".format(self.Uw2, self.Aw2, self.uMinusA))
            self.label_tStep.adjustSize()
            self.label_tnA.setText(str(self.uMinusA))
            self.label_tnA.adjustSize()
            self.windowResize(MainWindow)
            self.i +=1
        elif self.i == 1:
            self.uMinusB = self.Uw2 - self.Bw2
            self.label_tStep.setText(" ̅B = {} \\ {} = {}".format(self.Uw2, self.Bw2, self.uMinusB))
            self.label_tStep.adjustSize()
            self.label_tnB.setText(str(self.uMinusB))
            self.label_tnB.adjustSize()
            self.windowResize(MainWindow)
            self.i += 1
        elif self.i == 2:
            self.mAuniteMb = self.uMinusA | self.uMinusB
            self.label_tStep.setText(" ̅A ∪  ̅B = {} ∪ {} = {}".format(self.uMinusA, self.uMinusB, \
                self.mAuniteMb))
            self.label_tStep.adjustSize()
            self.windowResize(MainWindow)
            self.i += 1
        elif self.i == 3:
            self.uMinusC = self.Uw2 - self.Cw2
            self.label_tStep.setText(" ̅C = {} \\ {} = {}".format(self.Uw2, self.Cw2, self.uMinusC))
            self.label_tStep.adjustSize()
            self.label_tnC.setText(str(self.uMinusC))
            self.label_tnC.adjustSize()
            self.windowResize(MainWindow)
            self.i += 1
        elif self.i == 4:
            self.mBuniteMc = self.uMinusB | self.uMinusC
            self.label_tStep.setText(" ̅B ∪  ̅C = {} ∪ {} = {}".format(self.uMinusB, self.uMinusC, \
                self.mBuniteMc))
            self.label_tStep.adjustSize()
            self.windowResize(MainWindow)
            self.i += 1
        elif self.i == 5:
            self.aUnBintersectionBunC = self.mAuniteMb & self.mBuniteMc
            self.label_tStep.setText("((A ̅ ∪ B ̅) ∩ (B ̅ ∪ C ̅)) = {} ∩ {} = {}".format(self.mAuniteMb, \
                self.mBuniteMc, self.aUnBintersectionBunC))
            self.label_tStep.adjustSize()
            self.windowResize(MainWindow)
            self.i += 1
        elif self.i == 6:
            self.final = (self.Uw2 - self.aUnBintersectionBunC)
            self.label_tStep.setText(" ̅((A ̅ ∪ B ̅) ∩ (B ̅ ∪ C ̅)) = {} \\ {} = {}".format(self.Uw2, \
                self.aUnBintersectionBunC, self.final))
            self.label_tStep.adjustSize()
            self.label_tD.setText(str(self.label_tD.text()) + " = " + str(self.final))
            self.label_tD.adjustSize()
            self.label_func.setText(str(self.label_func.text()) + " = " + str(self.final))
            self.label_func.adjustSize()
            self.windowResize(MainWindow)
            self.i += 1

    def saveButtonClicked(self):
        if self.i < 7:
            self.statusbar.setStyleSheet("color: red")
            self.statusbar.showMessage("Спочатку зробіть всі кроки", 5000)
            
        else:
            with open(str(self.cwd) + "/D_Long.txt", "w", encoding="utf-8") as w:
                w.write(str(self.final) + "\n")
                w.write("D = " + str(self.label_tD.text()) + "\n")
                w.write(str(self.label_func.text()) + "\n")
                self.statusbar.setStyleSheet("color: green")
            self.statusbar.showMessage("Данні збережено", 10000)

    def windowResize(self, MainWindow):
        self.tmp = int(self.label_tStep.size().width())
        if self.tmp > 460:
            MainWindow.setFixedSize(self.tmp + 175, 460)
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Window_2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
