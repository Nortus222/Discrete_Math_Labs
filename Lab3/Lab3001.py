
from PyQt5 import QtCore, QtGui, QtWidgets
from Qstyle import style
from Lab3002 import Ui_Window_2

class Ui_MainWindow(object):

    nzk = 9229
    tmp = 0

    def setupUi(self, MainWindow):

        MainWindow.setFixedSize(590, 282)

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

        self.frame_GraphCreate = QtWidgets.QFrame(self.centralwidget)
        self.frame_GraphCreate.setGeometry(QtCore.QRect(300, 40, 270, 182))
        self.frame_GraphCreate.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_GraphCreate.setFrameShadow(QtWidgets.QFrame.Raised)

        self.label_GraphCreate = QtWidgets.QLabel(self.frame_GraphCreate)
        self.label_GraphCreate.setGeometry(QtCore.QRect(65, 20, 150, 20))
        font.setPointSize(18)
        font.setBold(True)
        self.label_GraphCreate.setFont(font)
        font.setBold(False)

        self.label_Nodes = QtWidgets.QLabel(self.frame_GraphCreate)
        self.label_Nodes.setGeometry(QtCore.QRect(45, 55, 200, 20))
        font.setPointSize(16)
        self.label_Nodes.setFont(font)

        self.spinBox = QtWidgets.QSpinBox(self.frame_GraphCreate)
        self.spinBox.setGeometry(QtCore.QRect(120, 90, 48, 24))

        self.pushButton_GraphCreate = QtWidgets.QPushButton(self.frame_GraphCreate)
        self.pushButton_GraphCreate.setGeometry(QtCore.QRect(80, 129, 113, 32))
        self.pushButton_GraphCreate.pressed.connect(self.openNewWindow)

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
        self.pushButton_Variant.setText(_translate("MainWindow", "Розрахувати"))
        self.label_GraphCreate.setText(_translate("MainWindow", "Створити Граф"))
        self.label_Nodes.setText(_translate("MainWindow", "Кількість вершин графа"))
        self.pushButton_GraphCreate.setText(_translate("MainWindow", "Створити"))
        self.menu.setTitle(_translate("MainWindow", "Вікна"))
        self.action_2.setText(_translate("MainWindow", "Вікно 2"))
        self.action_2.setShortcut(_translate("MainWindow", "Ctrl+2"))

    def variantButtonPressed(self):
        if self.nzk == 9229:
            i = (self.nzk % 10) + 1
            self.label_Variant.setText(str(self.label_Variant.text()) + str(i))
            self.label_Variant.adjustSize()
            self.nzk += 1
    
    def createNewWindow(self, i):
        if  i > 1:
            self.window2 = QtWidgets.QMainWindow()
            self.ui2 = Ui_Window_2()
            Ui_Window_2.nodesNum = i
            self.ui2.setupUi(self.window2)
            self.window2.setWindowTitle("Вікно 2")
            self.window2.show()
            self.tmp += 1
        elif i <= 1:
            self.statusbar.setStyleSheet("color: red")
            self.statusbar.showMessage("Некоректно заданий граф", 5000)

    def openNewWindow(self):
        i = int(self.spinBox.value())
        if self.tmp == 0:
            self.createNewWindow(i)
        elif self.tmp > 0:
            if Ui_Window_2.nodesNum == i:
                self.window2.setWindowFlags(self.window2.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
                self.window2.show()
                self.window2.setWindowFlags(self.window2.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
                self.window2.show()
            else:
                self.createNewWindow(i)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

