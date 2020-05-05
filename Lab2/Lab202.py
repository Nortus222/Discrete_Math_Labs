
from PyQt5 import QtCore, QtGui, QtWidgets
import os, re
from Lab203 import Ui_Window_3


class Ui_Window_2(object):

    maleList = [ "Артем", "Максим", "Іван", "Дмитро", "Олександр", "Давід", "Богдан", "Владислав", "Кирило", 
    "Денис", "Макар", "Михайло", "Роман", "Андрій", "Єгор"]

    femaleList = [ "Анастасія", "Сабіна", "Вікторія", "Марія", "Анна", "Софія", "Дарина", "Ангеліна", "Дарія", 
    "Вероніка", "Поліна", "Єлизавета", "Катерина", "Ксенія", "Любава"]

    setA = set()
    setB = set()

    cwd = os.getcwd()

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")

        MainWindow.resize(940, 520)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        
        self.frame_Male = QtWidgets.QFrame(self.centralwidget)
        self.frame_Male.setGeometry(QtCore.QRect(20, 20, 210, 352))
        self.frame_Male.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Male.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Male.setObjectName("frame_Male")

        self.listWidget_Male = QtWidgets.QListWidget(self.frame_Male)
        self.listWidget_Male.setGeometry(QtCore.QRect(20, 60, 170, 220))
        self.listWidget_Male.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.listWidget_Male.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget_Male.setObjectName("listWidget_Male")

        for i in self.maleList:
            item = QtWidgets.QListWidgetItem()
            item.setText(i)
            self.listWidget_Male.addItem(item)
        

        self.pushButton_CopyMale = QtWidgets.QPushButton(self.frame_Male)
        self.pushButton_CopyMale.setGeometry(QtCore.QRect(45, 300, 113, 32))
        self.pushButton_CopyMale.setObjectName("pushButton_CopyMale")
        self.pushButton_CopyMale.pressed.connect(lambda: self.copyList(self.pushButton_CopyMale))
        
        self.pushButton_resetMale = QtWidgets.QPushButton(self.frame_Male)
        self.pushButton_resetMale.setGeometry(QtCore.QRect(10, 300, 30, 30))
        self.pushButton_resetMale.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resetIcon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_resetMale.setIcon(icon)
        self.pushButton_resetMale.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_resetMale.setObjectName("pushButton_resetMale")
        self.pushButton_resetMale.pressed.connect(lambda: self.resetList(self.pushButton_resetMale))

        self.pushButton_selectAll_Male = QtWidgets.QPushButton(self.frame_Male)
        self.pushButton_selectAll_Male.setGeometry(QtCore.QRect(170, 300, 30, 30))
        self.pushButton_selectAll_Male.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("selectAllIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_selectAll_Male.setIcon(icon2)
        self.pushButton_selectAll_Male.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_selectAll_Male.setObjectName("pushButton_selectAll_Male")
        self.pushButton_selectAll_Male.pressed.connect(lambda: self.selectAllList(self.pushButton_selectAll_Male))


        self.label_NamesMale = QtWidgets.QLabel(self.frame_Male)
        self.label_NamesMale.setGeometry(QtCore.QRect(55, 20, 101, 20))
        

        self.frame_Female = QtWidgets.QFrame(self.centralwidget)
        self.frame_Female.setGeometry(QtCore.QRect(250, 20, 210, 352))
        self.frame_Female.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Female.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Female.setObjectName("frame")
        self.listWidget_Female = QtWidgets.QListWidget(self.frame_Female)
        self.listWidget_Female.setGeometry(QtCore.QRect(20, 60, 170, 220))
        self.listWidget_Female.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.listWidget_Female.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget_Female.setObjectName("listWidget_Female")

        for i in self.femaleList:
            item = QtWidgets.QListWidgetItem()
            item.setText(i)
            self.listWidget_Female.addItem(item)
        

        self.pushButton_CopyFemale = QtWidgets.QPushButton(self.frame_Female)
        self.pushButton_CopyFemale.setGeometry(QtCore.QRect(45, 300, 113, 32))
        self.pushButton_CopyFemale.setObjectName("pushButton_CopyFemale")
        self.pushButton_CopyFemale.pressed.connect(lambda: self.copyList(self.pushButton_CopyFemale))
    
        self.pushButton_resetFemale = QtWidgets.QPushButton(self.frame_Female)
        self.pushButton_resetFemale.setGeometry(QtCore.QRect(10, 300, 30, 30))
        self.pushButton_resetFemale.setText("")
        self.pushButton_resetFemale.setIcon(icon)
        self.pushButton_resetFemale.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_resetFemale.setObjectName("pushButton_resetFemale")
        self.pushButton_resetFemale.pressed.connect(lambda: self.resetList(self.pushButton_resetFemale))

        self.pushButton_selectAll_Female = QtWidgets.QPushButton(self.frame_Female)
        self.pushButton_selectAll_Female.setGeometry(QtCore.QRect(170, 300, 30, 30))
        self.pushButton_selectAll_Female.setText("")
        self.pushButton_selectAll_Female.setIcon(icon2)
        self.pushButton_selectAll_Female.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_selectAll_Female.setObjectName("pushButton_selectAll_Female")
        self.pushButton_selectAll_Female.pressed.connect(lambda: self.selectAllList(self.pushButton_selectAll_Female))

        self.label_NamesFemale = QtWidgets.QLabel(self.frame_Female)
        self.label_NamesFemale.setGeometry(QtCore.QRect(55, 20, 91, 16))
        
        self.frame_SetA = QtWidgets.QFrame(self.centralwidget)
        self.frame_SetA.setGeometry(QtCore.QRect(480, 132, 210, 241))
        self.frame_SetA.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_SetA.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_SetA.setObjectName("frame_SetA")

        self.listWidget_SetA = QtWidgets.QListWidget(self.frame_SetA)
        self.listWidget_SetA.setGeometry(QtCore.QRect(20, 40, 170, 180))
        self.listWidget_SetA.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.listWidget_SetA.setObjectName("listWidget_SetA")

        self.label_SetA = QtWidgets.QLabel(self.frame_SetA)
        self.label_SetA.setGeometry(QtCore.QRect(65, 10, 81, 20))
        
        self.frame_SetB = QtWidgets.QFrame(self.centralwidget)
        self.frame_SetB.setGeometry(QtCore.QRect(710, 132, 210, 241))
        self.frame_SetB.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_SetB.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_SetB.setObjectName("frame_SetB")

        self.listWidget_SetB = QtWidgets.QListWidget(self.frame_SetB)
        self.listWidget_SetB.setGeometry(QtCore.QRect(20, 40, 170, 180))
        self.listWidget_SetB.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.listWidget_SetB.setObjectName("listWidget_SetB")

        self.label_SetB = QtWidgets.QLabel(self.frame_SetB)
        self.label_SetB.setGeometry(QtCore.QRect(65, 10, 81, 20))
        
        self.frame_Copy = QtWidgets.QFrame(self.centralwidget)
        self.frame_Copy.setGeometry(QtCore.QRect(590, 20, 241, 80))
        self.frame_Copy.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Copy.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Copy.setObjectName("frame_Copy")

        self.radioButton_SetB = QtWidgets.QRadioButton(self.frame_Copy)
        self.radioButton_SetB.setGeometry(QtCore.QRect(110, 40, 100, 20))
        self.radioButton_SetB.setObjectName("radioButton_SetB")

        self.radioButton_SetA = QtWidgets.QRadioButton(self.frame_Copy)
        self.radioButton_SetA.setGeometry(QtCore.QRect(110, 20, 100, 20))
        self.radioButton_SetA.setObjectName("radioButton_SetA")
        self.radioButton_SetA.setChecked(True)

        self.label_Copy = QtWidgets.QLabel(self.frame_Copy)
        self.label_Copy.setGeometry(QtCore.QRect(20, 20, 81, 16))
        
        self.frame_SetA_File = QtWidgets.QFrame(self.centralwidget)
        self.frame_SetA_File.setGeometry(QtCore.QRect(20, 382, 440, 80))
        self.frame_SetA_File.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_SetA_File.setFrameShadow(QtWidgets.QFrame.Raised)
        
        self.label_SetA_2 = QtWidgets.QLabel(self.frame_SetA_File)
        self.label_SetA_2.setGeometry(QtCore.QRect(180, 10, 81, 20))
        
        self.pushButton_SetA_LoadFromFile = QtWidgets.QPushButton(self.frame_SetA_File)
        self.pushButton_SetA_LoadFromFile.setGeometry(QtCore.QRect(10, 40, 170, 32))
        self.pushButton_SetA_LoadFromFile.setObjectName("pushButton_SetA_LoadFromFile")
        self.pushButton_SetA_LoadFromFile.pressed.connect(lambda: self.loadFromFile(self.pushButton_SetA_LoadFromFile))

        self.pushButton_SetA_LoadToFile = QtWidgets.QPushButton(self.frame_SetA_File)
        self.pushButton_SetA_LoadToFile.setGeometry(QtCore.QRect(180, 40, 170, 32))
        self.pushButton_SetA_LoadToFile.setObjectName("pushButton_SetA_LoadToFile")
        self.pushButton_SetA_LoadToFile.pressed.connect(lambda: self.loadToFile(self.pushButton_SetA_LoadToFile))

        self.pushButton_SetA_Reset = QtWidgets.QPushButton(self.frame_SetA_File)
        self.pushButton_SetA_Reset.setGeometry(QtCore.QRect(350, 40, 80, 32))
        self.pushButton_SetA_Reset.setObjectName("pushButton_SetA_Reset")
        self.pushButton_SetA_Reset.pressed.connect(lambda: self.clearList(self.pushButton_SetA_Reset))

        self.frame_SetB_File = QtWidgets.QFrame(self.centralwidget)
        self.frame_SetB_File.setGeometry(QtCore.QRect(480, 382, 440, 80))
        self.frame_SetB_File.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_SetB_File.setFrameShadow(QtWidgets.QFrame.Raised)
        
        self.label_SetB_2 = QtWidgets.QLabel(self.frame_SetB_File)
        self.label_SetB_2.setGeometry(QtCore.QRect(180, 10, 81, 20))
        
        self.pushButton_SetB_LoadFromFile = QtWidgets.QPushButton(self.frame_SetB_File)
        self.pushButton_SetB_LoadFromFile.setGeometry(QtCore.QRect(10, 40, 170, 32))
        self.pushButton_SetB_LoadFromFile.setObjectName("pushButton_SetB_LoadFromFile")
        self.pushButton_SetB_LoadFromFile.pressed.connect(lambda: self.loadFromFile(self.pushButton_SetB_LoadFromFile))

        self.pushButton_SetB_LoadToFile = QtWidgets.QPushButton(self.frame_SetB_File)
        self.pushButton_SetB_LoadToFile.setGeometry(QtCore.QRect(180, 40, 170, 32))
        self.pushButton_SetB_LoadToFile.setObjectName("pushButton_SetB_LoadToFile")
        self.pushButton_SetB_LoadToFile.pressed.connect(lambda: self.loadToFile(self.pushButton_SetB_LoadToFile))
        
        self.pushButton_SetB_Reset = QtWidgets.QPushButton(self.frame_SetB_File)
        self.pushButton_SetB_Reset.setGeometry(QtCore.QRect(350, 40, 80, 32))
        self.pushButton_SetB_Reset.setObjectName("pushButton_SetB_Reset")
        self.pushButton_SetB_Reset.pressed.connect(lambda: self.clearList(self.pushButton_SetB_Reset))


        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 977, 22))

        self.menu = QtWidgets.QMenu(self.menubar)
        MainWindow.setMenuBar(self.menubar)
       

        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("win_3")
        self.action_3.triggered.connect(lambda: self.menubarTriggered(self.action_3))

        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("win_4")
        self.action_4.triggered.connect(lambda: self.menubarTriggered(self.action_4))

        
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)

        self.menubar.addAction(self.menu.menuAction())

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #self.centralwidget.setStyleSheet(Qstyle.style)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.listWidget_Male.isSortingEnabled()
        self.listWidget_Male.setSortingEnabled(False)
        self.listWidget_Male.setSortingEnabled(__sortingEnabled)
        self.pushButton_CopyMale.setText(_translate("MainWindow", "Копіювати"))
        self.label_NamesMale.setText(_translate("MainWindow", "Чоловічі Імена"))
        __sortingEnabled = self.listWidget_Female.isSortingEnabled()
        self.listWidget_Female.setSortingEnabled(False)

        self.menu.setTitle(_translate("MainWindow", "Вікна"))
       
        
        
        self.action_3.setText(_translate("MainWindow", "Вікно 3"))
        self.action_3.setShortcut(_translate("MainWindow", "Ctrl+3"))
        self.action_4.setText(_translate("MainWindow", "Вікно 4"))
        self.action_4.setShortcut(_translate("MainWindow", "Ctrl+4"))
        
        self.listWidget_Female.setSortingEnabled(__sortingEnabled)
        self.pushButton_CopyFemale.setText(_translate("MainWindow", "Копіювати"))
        self.label_NamesFemale.setText(_translate("MainWindow", "Жіночі Імена"))
        self.label_SetA.setText(_translate("MainWindow", "Множина А"))
        self.label_SetB.setText(_translate("MainWindow", "Множина B"))
        self.radioButton_SetB.setText(_translate("MainWindow", "Множину B"))
        self.radioButton_SetA.setText(_translate("MainWindow", "Множину А"))
        self.label_Copy.setText(_translate("MainWindow", "Копіювати в"))
        self.label_SetA_2.setText(_translate("MainWindow", "Множина А"))
        self.label_SetB_2.setText(_translate("MainWindow", "Множина B"))
        self.pushButton_SetA_LoadFromFile.setText(_translate("MainWindow", "Завантажити з файлу"))
        self.pushButton_SetB_LoadFromFile.setText(_translate("MainWindow", "Завантажити з файлу"))
        self.pushButton_SetA_LoadToFile.setText(_translate("MainWindow", "Завантажити у файл"))
        self.pushButton_SetB_LoadToFile.setText(_translate("MainWindow", "Завантажити у файл"))
        self.pushButton_SetA_Reset.setText(_translate("MainWindow", "Зтерти"))
        self.pushButton_SetB_Reset.setText(_translate("MainWindow", "Зтерти"))
        self.pushButton_SetA_LoadFromFile.setStatusTip(_translate("MainWindow", "Файл повинен мати ім\'я InputSetA.txt"))
        self.pushButton_SetB_LoadFromFile.setStatusTip(_translate("MainWindow", "Файл повинен мати ім\'я InputSetB.txt"))


    def resetList(self, m):
        if m.objectName() == "pushButton_resetMale":
            self.listWidget_Male.reset()
        elif m.objectName() == "pushButton_resetFemale":
            self.listWidget_Female.reset()


    def clearList(self, buttn):
        if buttn.objectName() == "pushButton_SetA_Reset":
            self.listWidget_SetA.clear()
            self.setA.clear()
        elif buttn.objectName() == "pushButton_SetB_Reset":
            self.listWidget_SetB.clear()
            self.setB.clear()


    def selectAllList(self, m):
        if m.objectName() == "pushButton_selectAll_Male":
            self.listWidget_Male.selectAll()
        elif m.objectName() == "pushButton_selectAll_Female":
            self.listWidget_Female.selectAll()


    def refreshList(self, s, listW):
        listW.clear()

        for i in s:
            listW.addItem(i)


    def addItem(self, itms, s, listW):
        for i in itms:
                s.add(i.text())

        self.refreshList(s, listW)


    def radioSelection(self, itms):
        if self.radioButton_SetA.isChecked():
            self.addItem(itms, self.setA, self.listWidget_SetA)

        elif self.radioButton_SetB.isChecked():
            self.addItem(itms, self.setB, self.listWidget_SetB)
            

    def copyList(self, buttn):
        if buttn.objectName() == "pushButton_CopyMale":
            items = self.listWidget_Male.selectedItems()
            self.radioSelection(items)

        elif buttn.objectName() == "pushButton_CopyFemale":
            items = self.listWidget_Female.selectedItems()
            self.radioSelection(items)


    def textLoadFromFile(self, txt, s, listW):
        try:
            with open(str(self.cwd) + txt, "r+", encoding="utf-8") as w:
                text = w.read()
                    
                self.statusbar.setStyleSheet("color: green")
                self.statusbar.showMessage("Данні зчитано", 10000)

            textR = re.findall(r'\w+', text)

            for i in textR:
                s.add(i)

            self.refreshList(s, listW)
            
        except(FileNotFoundError):
            self.statusbar.setStyleSheet("color: red")
            self.statusbar.showMessage("Файл не знайдено", 10000)


    def loadFromFile(self, buttn):
        if buttn.objectName() == "pushButton_SetA_LoadFromFile":
            self.textLoadFromFile("/InputSetA.txt", self.setA, self.listWidget_SetA)

        elif buttn.objectName() == "pushButton_SetB_LoadFromFile":
            self.textLoadFromFile("/InputSetB.txt", self.setB, self.listWidget_SetB)
            

    def textLoadToFile(self, txt, s):
        with open(str(self.cwd) + txt, "w+", encoding="utf-8") as w:
            for i in s:
                w.write(i + ", ")
                
            self.statusbar.setStyleSheet("color: green")
            self.statusbar.showMessage("Данні збережено", 10000)


    def loadToFile(self, buttn):
        if buttn.objectName() == "pushButton_SetA_LoadToFile":
            self.textLoadToFile("/OutputSetA.txt", self.setA)
        elif buttn.objectName() == "pushButton_SetB_LoadToFile":
            self.textLoadToFile("/OutputSetB.txt", self.setB)


    def menubarTriggered(self, buttn):
        if buttn.objectName() == "win_3":
            self.window3 = QtWidgets.QMainWindow()
            self.ui3 = Ui_Window_3()
            Ui_Window_3.setA = self.setA
            Ui_Window_3.setB = self.setB
            Ui_Window_3.meleList = self.maleList
            Ui_Window_3.femaleList = self.femaleList
            self.ui3.setupUi(self.window3)
            self.window3.setWindowTitle("Вікно 3")
            self.window3.show()
            
            

        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Window_2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

