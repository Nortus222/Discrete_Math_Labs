from PyQt5 import QtCore, QtGui, QtWidgets
from Lab202 import Ui_Window_2
from Lab203 import Ui_Window_3
from Lab204 import Ui_Window_4

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")

        MainWindow.resize(500, 200)

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 722, 22))
        
        self.menu = QtWidgets.QMenu(self.menubar)
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        
        MainWindow.setStatusBar(self.statusbar)

        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("win_2")
        self.action_2.triggered.connect(lambda: self.menubarTriggered(self.action_2))

        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("win_3")
        self.action_3.triggered.connect(lambda: self.menubarTriggered(self.action_3))

        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("win_4")
        self.action_4.triggered.connect(lambda: self.menubarTriggered(self.action_4))

        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)

        self.menubar.addAction(self.menu.menuAction())

        self.label_Initials = QtWidgets.QLabel(self.centralwidget)
        self.label_Initials.setGeometry(QtCore.QRect(30, 15, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_Initials.setFont(font)

        self.label_Variant = QtWidgets.QLabel(self.centralwidget)
        self.label_Variant.setGeometry(QtCore.QRect(130, 110, 60, 16))
        self.label_Variant.setObjectName("label_Variant")

        self.label_group = QtWidgets.QLabel(self.centralwidget)
        self.label_group.setGeometry(QtCore.QRect(30, 45, 150, 30))
        font.setPointSize(16)
        self.label_group.setFont(font)

        self.label_number = QtWidgets.QLabel(self.centralwidget)
        self.label_number.setGeometry(QtCore.QRect(30, 75, 175, 30))
        self.label_number.setFont(font)

        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(30, 110, 91, 16))
        font.setPointSize(15)
        self.label_13.setFont(font)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 130, 113, 32))
        self.pushButton.setObjectName("variantButton")
        self.pushButton.clicked.connect(self.button_VariantClicked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.label_Initials.setText(_translate("MainWindow", "Шерстюк Ігор Юрійович"))
        self.label_13.setText(_translate("MainWindow", "Мій варіант :"))
        self.pushButton.setText(_translate("MainWindow", "Розрахувати"))
        self.menu.setTitle(_translate("MainWindow", "Вікна"))
        self.action_2.setText(_translate("MainWindow", "Вікно 2"))
        self.action_2.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.action_3.setText(_translate("MainWindow", "Вікно 3"))
        self.action_3.setShortcut(_translate("MainWindow", "Ctrl+3"))
        self.action_4.setText(_translate("MainWindow", "Вікно 4"))
        self.action_4.setShortcut(_translate("MainWindow", "Ctrl+4"))


    def button_VariantClicked(self):
        G = 92
        N = 29
        M = "ІВ"
        self.label_group.setText("Моя група: {} - {}".format(M, G))
        self.label_number.setText("Мій номер у групі: {}".format(N))
        if M == "ІO":
            N += 1
        self.label_Variant.setText(str((N + G%60)%30 + 1))


    def menubarTriggered(self, m):
        if m.objectName() == "win_2":
            self.window2 = QtWidgets.QMainWindow()
            self.ui2 = Ui_Window_2()
            self.ui2.setupUi(self.window2)
            self.window2.setWindowTitle("Вікно 2")
            self.window2.show()
        elif m.objectName() == "win_3":
            self.window3 = QtWidgets.QMainWindow()
            self.ui3 = Ui_Window_3()
            Ui_Window_3.setA = Ui_Window_2.setA
            Ui_Window_3.setB = Ui_Window_2.setB
            self.ui3.setupUi(self.window3)
            self.window3.setWindowTitle("Вікно 3")
            self.window3.show()
            
        elif m.objectName() == "win_4":
            self.window4 = QtWidgets.QMainWindow()
            self.ui4 = Ui_Window_4()
            self.ui4.setupUi(self.window4)
            self.window4.setWindowTitle("Вікно 4")
            self.window4.show()
            
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

