
from PyQt5 import QtCore, QtGui, QtWidgets
from Qstyle import style
from Lab4002 import Ui_Window_2

class Ui_MainWindow(object):

    nzk = 9229
    tmp = 0

    def setupUi(self, MainWindow):

        MainWindow.setFixedSize(800, 282)

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.frame_Credentials = QtWidgets.QFrame(self.centralwidget)
        self.frame_Credentials.setGeometry(QtCore.QRect(20, 40, 260, 182))
        self.frame_Credentials.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Credentials.setFrameShadow(QtWidgets.QFrame.Raised)

        font = QtGui.QFont()

        self.label_Credentials1 = QtWidgets.QLabel(self.frame_Credentials)
        self.label_Credentials1.setGeometry(QtCore.QRect(20, 20, 220, 20))
        font.setPointSize(18)
        font.setBold(True)
        self.label_Credentials1.setFont(font)
        font.setBold(False)

        self.label_Credentials2 = QtWidgets.QLabel(self.frame_Credentials)
        self.label_Credentials2.setGeometry(QtCore.QRect(20, 50, 180, 40))
        font.setPointSize(16)
        self.label_Credentials2.setFont(font)

        self.label_Variant = QtWidgets.QLabel(self.frame_Credentials)
        self.label_Variant.setGeometry(QtCore.QRect(20, 100, 91, 20))
        self.label_Variant.setFont(font)

        self.pushButton_Variant = QtWidgets.QPushButton(self.frame_Credentials)
        self.pushButton_Variant.setGeometry(QtCore.QRect(20, 130, 113, 32))
        self.pushButton_Variant.setObjectName("pushButton_Variant")
        self.pushButton_Variant.pressed.connect(self.variantButtonPressed)

        self.label_GraphCreate = QtWidgets.QLabel(self.centralwidget)
        self.label_GraphCreate.setGeometry(QtCore.QRect(365, 10, 150, 20))
        font.setPointSize(18)
        font.setBold(True)
        self.label_GraphCreate.setFont(font)
        font.setBold(False)

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(300, 50, 165, 20))
        self.radioButton.setObjectName("example")
        self.radioButton.setChecked(True)
        self.radioButton.toggled.connect(lambda: self.radioButtonClicked(self.radioButton))

        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(485, 50, 155, 20))
        self.radioButton_2.setObjectName("random")
        self.radioButton_2.setChecked(False)
        self.radioButton.toggled.connect(lambda: self.radioButtonClicked(self.radioButton_2))

        self.frame_GraphCreate = QtWidgets.QFrame(self.centralwidget)
        self.frame_GraphCreate.setGeometry(QtCore.QRect(485, 80, 200, 145))
        self.frame_GraphCreate.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_GraphCreate.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_GraphCreate.setVisible(False)

        self.label_Nodes = QtWidgets.QLabel(self.frame_GraphCreate)
        self.label_Nodes.setGeometry(QtCore.QRect(20, 20, 200, 20))
        font.setPointSize(14)
        self.label_Nodes.setFont(font)

        self.spinBox = QtWidgets.QSpinBox(self.frame_GraphCreate)
        self.spinBox.setGeometry(QtCore.QRect(85, 60, 48, 24))

        self.pushButton_GraphCreate = QtWidgets.QPushButton(self.frame_GraphCreate)
        self.pushButton_GraphCreate.setGeometry(QtCore.QRect(45, 100, 113, 32))
        self.pushButton_GraphCreate.setObjectName("random")
        self.pushButton_GraphCreate.pressed.connect(lambda: self.openNewWindow(self.pushButton_GraphCreate))

        self.frame_GraphExample = QtWidgets.QFrame(self.centralwidget)
        self.frame_GraphExample.setGeometry(QtCore.QRect(300, 80, 165, 145))
        self.frame_GraphExample.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_GraphExample.setFrameShadow(QtWidgets.QFrame.Raised)

        self.pushButton_GraphExampleCreate = QtWidgets.QPushButton(self.frame_GraphExample)
        self.pushButton_GraphExampleCreate.setGeometry(QtCore.QRect(30, 56.5, 113, 32))
        self.pushButton_GraphExampleCreate.setObjectName("example")
        self.pushButton_GraphExampleCreate.pressed.connect(lambda: self.openNewWindow(self.pushButton_GraphExampleCreate))

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 22))

        self.menu = QtWidgets.QMenu(self.menubar)

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)


        MainWindow.setStatusBar(self.statusbar)

        self.action_2 = QtWidgets.QAction(MainWindow)

        self.action_2.triggered.connect(self.openNewWindow)

        self.menu.addAction(self.action_2)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        
        self.centralwidget.setStyleSheet(style)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("Вікно 1")
        self.label_Credentials1.setText(_translate("MainWindow", "Шерстюк Ігор Юрійович"))
        self.label_Credentials2.setText(_translate("MainWindow", "Група: ІВ-92 \nНомер у списку: 29"))
        self.label_Variant.setText(_translate("MainWindow", "Варіант: "))
        self.radioButton.setText(_translate("MainWindow", "Контрольний приклад"))
        self.radioButton_2.setText(_translate("MainWindow", "Випадковий граф"))
        self.pushButton_Variant.setText(_translate("MainWindow", "Розрахувати"))
        self.label_GraphCreate.setText(_translate("MainWindow", "Створити Граф"))
        self.label_Nodes.setText(_translate("MainWindow", "Кількість вершин графа"))
        self.pushButton_GraphCreate.setText(_translate("MainWindow", "Створити"))
        self.pushButton_GraphExampleCreate.setText(_translate("MainWindow", "Створити"))
        self.menu.setTitle(_translate("MainWindow", "Вікна"))
        self.action_2.setText(_translate("MainWindow", "Вікно 2"))
        self.action_2.setShortcut(_translate("MainWindow", "Ctrl+2"))

    def variantButtonPressed(self):
        if self.nzk == 9229:
            i = (self.nzk % 6) + 1
            self.label_Variant.setText(str(self.label_Variant.text()) + str(i))
            self.label_Variant.adjustSize()
            self.nzk += 1
    
    def radioButtonClicked(self, b):
        if b.isChecked():
            if b.objectName() == "random":
                self.frame_GraphExample.setVisible(False)
                self.frame_GraphCreate.setVisible(True)
            if b.objectName() == "example":
                self.frame_GraphCreate.setVisible(False)
                self.frame_GraphExample.setVisible(True)

    def createNewWindow(self, i, btn):
        if btn.objectName() == "random":
            if  i >= 1:
                self.window2 = QtWidgets.QMainWindow()
                self.ui2 = Ui_Window_2()
                Ui_Window_2.nodesNum = i
                Ui_Window_2.btn = btn.objectName()
                self.ui2.setupUi(self.window2)
                self.window2.setWindowTitle("Вікно 2")
                self.window2.show()
                self.tmp += 1
            elif i < 1:
                self.statusbar.setStyleSheet("color: red")
                self.statusbar.showMessage("Некоректно заданий граф", 5000)
        if btn.objectName() == "example":
            self.window2 = QtWidgets.QMainWindow()
            self.ui2 = Ui_Window_2()
            Ui_Window_2.btn = btn.objectName()
            self.ui2.setupUi(self.window2)
            self.window2.setWindowTitle("Вікно 2")
            self.window2.show()
            self.tmp += 1

    def openNewWindow(self, btn):
        i = int(self.spinBox.value())
        if self.tmp == 0:
            if btn.objectName() == "example":
                self.createNewWindow(0, btn)
            elif btn.objectName() == "random":
                self.createNewWindow(i,btn)
        elif self.tmp > 0:
            if btn.objectName() == "random":
                if Ui_Window_2.nodesNum == i:
                    self.window2.setWindowFlags(self.window2.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
                    self.window2.show()
                    self.window2.setWindowFlags(self.window2.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
                    self.window2.show()
                else:
                    self.createNewWindow(i, btn)
            elif btn.objectName() == "example":
                self.createNewWindow(0, btn)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

