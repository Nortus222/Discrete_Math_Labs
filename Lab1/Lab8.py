from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from random import randrange
from Lab8002 import Ui_Window_2
from Lab8003 import Ui_Window_3
from Lab8004 import Ui_Window_4
from Lab8005 import Ui_Window_5

class Ui_MainWindow(object):

    A = set()
    B = set()
    C = set()
    U = set()
    tmp = "random"

    def setupUi(self, MainWindow):

        MainWindow.setFixedSize(630, 590)

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.label_Initials = QtWidgets.QLabel(self.centralwidget)
        self.label_Initials.setGeometry(QtCore.QRect(30, 15, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_Initials.setFont(font)

        self.label_group = QtWidgets.QLabel(self.centralwidget)
        self.label_group.setGeometry(QtCore.QRect(30, 45, 150, 30))
        font.setPointSize(16)
        self.label_group.setFont(font)

        self.label_number = QtWidgets.QLabel(self.centralwidget)
        self.label_number.setGeometry(QtCore.QRect(30, 75, 175, 30))
        self.label_number.setFont(font)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 190, 71, 31))

        self.label_Result = QtWidgets.QLabel(self.centralwidget)
        self.label_Result.setGeometry(QtCore.QRect(100, 200, 60, 16))

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 230, 141, 16))

        self.label_A = QtWidgets.QLabel(self.centralwidget)
        self.label_A.setGeometry(QtCore.QRect(30, 440, 60, 16))
        
        self.label_B = QtWidgets.QLabel(self.centralwidget)
        self.label_B.setGeometry(QtCore.QRect(30, 470, 60, 16))
        
        self.label_C = QtWidgets.QLabel(self.centralwidget)
        self.label_C.setGeometry(QtCore.QRect(30, 500, 60, 16))
        
        self.label_tA = QtWidgets.QLabel(self.centralwidget)
        self.label_tA.setGeometry(QtCore.QRect(60, 440, 60, 16))
        
        self.label_tB = QtWidgets.QLabel(self.centralwidget)
        self.label_tB.setGeometry(QtCore.QRect(60, 470, 60, 16))
        
        self.label_tC = QtWidgets.QLabel(self.centralwidget)
        self.label_tC.setGeometry(QtCore.QRect(60, 500, 60, 16))

        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(220, 145, 161, 16))
        
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(230, 185, 48, 24))
        self.spinBox_3.setMaximum(500)
        
        self.spinBox_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_4.setGeometry(QtCore.QRect(310, 185, 48, 24))
        self.spinBox_4.setMaximum(500)
        
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(220, 165, 60, 16))
        
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(310, 165, 60, 16))
        
        self.pushButton_univSet = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_univSet.setGeometry(QtCore.QRect(230, 210, 113, 32))
        self.pushButton_univSet.clicked.connect(self.univSetCreate)

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(30, 250, 151, 20))
        self.radioButton.setObjectName("random")
        self.radioButton.setChecked(True)
        self.radioButton.toggled.connect(lambda: self.radioButtonClicked(self.radioButton))

        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(210, 250, 151, 20))
        self.radioButton_2.setObjectName("hands")
        self.radioButton_2.toggled.connect(lambda: self.radioButtonClicked(self.radioButton_2))

        self.labe_InputMessage = QtWidgets.QLabel(self.centralwidget)
        self.labe_InputMessage.setGeometry(QtCore.QRect(200, 390, 201, 16))
        self.labe_InputMessage.setVisible(False)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(400, 10, 201, 321))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(5)

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 181, 31))

        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(80, 40, 21, 21))

        self.horizontalSlider = QtWidgets.QSlider(self.frame)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 60, 160, 22))
        self.horizontalSlider.setMaximum(20)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("a")
        self.horizontalSlider.valueChanged.connect(lambda: self.sliderValueChanged(self.horizontalSlider))

        self.label_AOut = QtWidgets.QLabel(self.frame)
        self.label_AOut.setGeometry(QtCore.QRect(80, 90, 60, 16))
        self.label_AOut.setText(str(self.horizontalSlider.value()))

        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(80, 120, 21, 21))

        self.horizontalSlider_2 = QtWidgets.QSlider(self.frame)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(10, 150, 160, 22))
        self.horizontalSlider_2.setMaximum(20)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("b")
        self.horizontalSlider_2.valueChanged.connect(lambda: self.sliderValueChanged(self.horizontalSlider_2))

        self.label_BOut = QtWidgets.QLabel(self.frame)
        self.label_BOut.setGeometry(QtCore.QRect(80, 180, 60, 16))
        self.label_BOut.setText(str(self.horizontalSlider_2.value()))

        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(80, 210, 21, 21))

        self.horizontalSlider_3 = QtWidgets.QSlider(self.frame)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(10, 240, 160, 22))
        self.horizontalSlider_3.setMaximum(20)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("c")
        self.horizontalSlider_3.valueChanged.connect(lambda: self.sliderValueChanged(self.horizontalSlider_3))

        self.label_COut = QtWidgets.QLabel(self.frame)
        self.label_COut.setGeometry(QtCore.QRect(80, 270, 60, 16))
        self.label_COut.setText(str(self.horizontalSlider_3.value()))

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(200, 280, 161, 101))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setVisible(False)

        self.lineEdit_A = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_A.setGeometry(QtCore.QRect(40, 10, 113, 21))

        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 21, 21))

        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(10, 40, 21, 21))

        self.lineEdit_B = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_B.setGeometry(QtCore.QRect(40, 40, 113, 21))

        self.lineEdit_C = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_C.setGeometry(QtCore.QRect(40, 70, 113, 21))

        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(10, 70, 21, 21))

        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(30, 280, 141, 121))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)

        self.spinBox = QtWidgets.QSpinBox(self.frame_3)
        self.spinBox.setGeometry(QtCore.QRect(10, 40, 48, 24))
        self.spinBox.setMaximum(500)

        self.spinBox_2 = QtWidgets.QSpinBox(self.frame_3)
        self.spinBox_2.setGeometry(QtCore.QRect(10, 90, 48, 24))
        self.spinBox_2.setMaximum(500)

        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 60, 16))

        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(10, 0, 121, 21))

        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(10, 70, 60, 16))

        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(30, 110, 91, 16))
        font.setPointSize(15)
        self.label_13.setFont(font)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 130, 113, 32))
        self.pushButton.setObjectName("variantButton")
        self.pushButton.clicked.connect(self.button_VariantClicked)

        self.pushButton_genA = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_genA.setGeometry(QtCore.QRect(440, 330, 131, 32))
        self.pushButton_genA.setObjectName("genA")
        self.pushButton_genA.clicked.connect(lambda: self.genButtonClicked(self.pushButton_genA))

        self.pushButton_genB = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_genB.setGeometry(QtCore.QRect(440, 370, 131, 32))
        self.pushButton_genB.setObjectName("genB")
        self.pushButton_genB.clicked.connect(lambda: self.genButtonClicked(self.pushButton_genB))

        self.pushButton_genC = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_genC.setGeometry(QtCore.QRect(440, 410, 131, 32))
        self.pushButton_genC.setObjectName("genC")
        self.pushButton_genC.clicked.connect(lambda: self.genButtonClicked(self.pushButton_genC))

        self.label_Variant = QtWidgets.QLabel(self.centralwidget)
        self.label_Variant.setGeometry(QtCore.QRect(130, 110, 60, 16))
        self.label_Variant.setObjectName("label_Variant")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 629, 22))
        
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
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

        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("win_5")
        self.action_5.triggered.connect(lambda: self.menubarTriggered(self.action_5))

        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)
        self.menu.addAction(self.action_5)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lab8_Sherstiuk"))
        self.label_Initials.setText(_translate("MainWindow", "Шерстюк Ігор Юрійович"))
        self.label.setText(_translate("MainWindow", "Результат:"))
        self.label_Result.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "Елементи множин"))
        self.radioButton.setText(_translate("MainWindow", "Задання випадково"))
        self.radioButton_2.setText(_translate("MainWindow", "Задання вручну"))
        self.labe_InputMessage.setText(_translate("MainWindow", "Напишіть цифри через пробіл"))
        self.label_2.setText(_translate("MainWindow", "Потужність множин A,B,C"))
        self.label_3.setText(_translate("MainWindow", "A"))
        self.label_4.setText(_translate("MainWindow", "B"))
        self.label_5.setText(_translate("MainWindow", "C"))
        self.label_7.setText(_translate("MainWindow", "A"))
        self.label_8.setText(_translate("MainWindow", "B"))
        self.label_9.setText(_translate("MainWindow", "C"))
        self.label_10.setText(_translate("MainWindow", "Початок"))
        self.label_11.setText(_translate("MainWindow", "Визначте діапазон"))
        self.label_12.setText(_translate("MainWindow", "Кінець"))
        self.label_13.setText(_translate("MainWindow", "Мій варіант :"))
        self.pushButton.setText(_translate("MainWindow", "Розрахувати"))
        self.label_A.setText(_translate("MainWindow", "A = "))
        self.label_B.setText(_translate("MainWindow", "B = "))
        self.label_C.setText(_translate("MainWindow", "C = "))
        self.label_tA.setText(_translate("MainWindow", ""))
        self.label_tB.setText(_translate("MainWindow", ""))
        self.label_tC.setText(_translate("MainWindow", ""))
        self.pushButton_genA.setText(_translate("MainWindow", "Згенерувати  A"))
        self.pushButton_genB.setText(_translate("MainWindow", "Згенерувати  B"))
        self.pushButton_genC.setText(_translate("MainWindow", "Згенерувати  C"))
        self.label_Variant.setText(_translate("MainWindow", ""))
        self.label_14.setText(_translate("MainWindow", "Універсальна множина"))
        self.label_15.setText(_translate("MainWindow", "Початок"))
        self.label_16.setText(_translate("MainWindow", "Кінець"))
        self.pushButton_univSet.setText(_translate("MainWindow", "Підтвердити"))
        self.menu.setTitle(_translate("MainWindow", "Вікна"))
        self.action_2.setText(_translate("MainWindow", "Вікно 2"))
        self.action_2.setShortcut(_translate("MainWindow", "⌘2"))
        self.action_2.setStatusTip(_translate("MainWindow", "Відкрити викно 2"))
        self.action_3.setText(_translate("MainWindow", "Вікно 3"))
        self.action_3.setShortcut(_translate("MainWindow", "⌘3"))
        self.action_3.setStatusTip(_translate("MainWindow", "Відкрити викно 3"))
        self.action_4.setText(_translate("MainWindow", "Вікно 4"))
        self.action_4.setShortcut(_translate("MainWindow", "⌘4"))
        self.action_4.setStatusTip(_translate("MainWindow", "Відкрити викно 4"))
        self.action_5.setText(_translate("MainWindow", "Вікно 5"))
        self.action_5.setShortcut(_translate("MainWindow", "⌘5"))
        self.action_5.setStatusTip(_translate("MainWindow", "Відкрити викно 5"))

    def radioButtonClicked(self, b):
        if b.isChecked():
            if b.objectName() == "random":
                self.frame_2.setVisible(False)
                self.labe_InputMessage.setVisible(False)
                self.frame_3.setVisible(True)
                self.tmp = "random"
            if b.objectName() == "hands":
                self.frame_3.setVisible(False)
                self.frame_2.setVisible(True)
                self.labe_InputMessage.setVisible(True)
                self.tmp = "hands"

    def sliderValueChanged(self, s):
        if s.objectName() == "a":
            self.label_AOut.setText(str(s.value()))
        elif s.objectName() == "b":
            self.label_BOut.setText(str(s.value()))
        elif s.objectName() == "c":
            self.label_COut.setText(str(s.value()))

    def button_VariantClicked(self):
        G = 92
        N = 29
        M = "ІВ"
        self.label_group.setText("Моя група: {} - {}".format(M, G))
        self.label_number.setText("Мій номер у групі: {}".format(N))
        if M == "ІВ":
            N +=2
        self.label_Variant.setText(str((N + G%60)%30 + 1))

    def genButtonClicked(self,b):
        if b.objectName() == "genA":
            if self.tmp == "random":
                if int(self.spinBox.value()) > int(self.spinBox_2.value()):
                    self.statusbar.setStyleSheet("color: red")
                    self.statusbar.showMessage("Невірно вказано диапазон", 5000)
                elif int(self.spinBox_2.value()) - int(self.spinBox.value()) + 1 < self.horizontalSlider.value():
                    self.statusbar.setStyleSheet("color: red")
                    self.statusbar.showMessage("Діапазон менше ніж множина", 5000)
                elif self.horizontalSlider.value() == 0:
                    self.label_tA.setText("Виберить потужнисть більше 0")
                    self.label_tA.adjustSize()
                else:
                    self.A = set()
                    while len(self.A) != self.horizontalSlider.value():
                        self.A.add(randrange(int(self.spinBox.value()),int(self.spinBox_2.value())+1, 1))
                    self.label_tA.setText(str(self.A))
                    self.label_tA.adjustSize()
                    Ui_Window_2.Aw2 = self.A
            else:
                self.A = str(self.lineEdit_A.text()).split()
                for i in range(len(self.A)):
                    self.A[i] = int(self.A[i])
                self.label_tA.setText(str(self.A))
                self.label_tA.adjustSize()
                self.A = set(self.A)
                Ui_Window_2.Aw2 = self.A
        elif b.objectName() == "genB":
            if self.tmp == "random":
                if int(self.spinBox.value()) > int(self.spinBox_2.value()):
                    self.statusbar.setStyleSheet("color: red")
                    self.statusbar.showMessage("Невірно вказано диапазон", 5000)
                elif int(self.spinBox_2.value()) - int(self.spinBox.value()) + 1 < self.horizontalSlider_2.value():
                    self.statusbar.setStyleSheet("color: red")
                    self.statusbar.showMessage("Діапазон менше ніж множина", 5000)
                elif self.horizontalSlider_2.value() == 0:
                    self.label_tB.setText("Виберить потужнисть більше 0")
                    self.label_tB.adjustSize()
                else:
                    self.B = set()
                    while len(self.B) != self.horizontalSlider_2.value():
                        self.B.add(randrange(int(self.spinBox.value()),int(self.spinBox_2.value())+1, 1))
                    self.label_tB.setText(str(self.B))
                    self.label_tB.adjustSize()
                    Ui_Window_2.Bw2 = self.B
            else:
                self.B = str(self.lineEdit_B.text()).split()
                for i in range(len(self.B)):
                    self.B[i] = int(self.B[i])
                self.label_tB.setText(str(self.B))
                self.label_tB.adjustSize()
                self.B = set(self.B)
                Ui_Window_2.Bw2 = self.B
        elif b.objectName() == "genC":
            if self.tmp == "random":
                if int(self.spinBox.value()) > int(self.spinBox_2.value()):
                    self.statusbar.setStyleSheet("color: red")
                    self.statusbar.showMessage("Невірно вказано диапазон", 5000)
                elif int(self.spinBox_2.value()) - int(self.spinBox.value()) + 1 < self.horizontalSlider_3.value():
                    self.statusbar.setStyleSheet("color: red")
                    self.statusbar.showMessage("Діапазон менше ніж множина", 5000)
                elif self.horizontalSlider_3.value() == 0:
                    self.label_tC.setText("Виберить потужнисть більше 0")
                    self.label_tC.adjustSize()
                else:
                    self.C = set()
                    while len(self.C) != self.horizontalSlider_3.value():
                        self.C.add(randrange(int(self.spinBox.value()),int(self.spinBox_2.value())+1, 1))
                    self.label_tC.setText(str(self.C))
                    self.label_tC.adjustSize()
                    Ui_Window_2.Cw2 = self.C
            else:
                self.C = str(self.lineEdit_C.text()).split()
                for i in range(len(self.C)):
                    self.C[i] = int(self.C[i])
                self.label_tC.setText(str(self.C))
                self.label_tC.adjustSize()
                self.C = set(self.C)
                Ui_Window_2.Cw2 = self.C

    def univSetCreate(self):
        if int(self.spinBox_4.value()) < int(self.spinBox_4.value()):
            self.statusbar.setStyleSheet("color: red")
            self.statusbar.showMessage("Невірно задано диапазон", 5000)
        else:
            for i in range(int(self.spinBox_3.value()), int(self.spinBox_4.value()) + 1):
                self.U.add(i)
            Ui_Window_2.Uw2 = self.U

    def menubarTriggered(self, m):
        if self.A == set():
            self.statusbar.setStyleSheet("color: red")
            self.statusbar.showMessage("Створіть множину A", 5000)
        elif self.B == set():
            self.statusbar.setStyleSheet("color: red")
            self.statusbar.showMessage("Створіть множину B", 5000)
        elif self.C == set():
            self.statusbar.setStyleSheet("color: red")
            self.statusbar.showMessage("Створіть множину C", 5000)
        elif self.U == set():
            self.statusbar.setStyleSheet("color: red")
            self.statusbar.showMessage("Cтворіть універсальну множину", 5000)
        else:
            if m.objectName() == "win_2":
                self.window2 = QtWidgets.QMainWindow()
                self.ui2 = Ui_Window_2()
                self.ui2.setupUi(self.window2)
                self.window2.setWindowTitle("Вікно 2")
                self.window2.show()
            elif m.objectName() == "win_3":
                self.window3 = QtWidgets.QMainWindow()
                self.ui3 = Ui_Window_3()
                self.ui3.setupUi(self.window3)
                self.window3.setWindowTitle("Вікно 3")
                self.window3.show()
            elif m.objectName() == "win_4":
                self.window4 = QtWidgets.QMainWindow()
                self.ui4 = Ui_Window_4()
                self.ui4.setupUi(self.window4)
                self.window4.setWindowTitle("Вікно 4")
                self.window4.show()
            elif m.objectName() == "win_5":
                self.window5 = QtWidgets.QMainWindow()
                self.ui5 = Ui_Window_5()
                self.ui5.setupUi(self.window5)
                self.window5.setWindowTitle("Вікно 5")
                self.window5.show()

def window():
    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        win = Ui_MainWindow()
        win.setupUi(MainWindow)
        MainWindow.setWindowTitle("Головне вікно")
        MainWindow.show()
        sys.exit(app.exec_())

window()
