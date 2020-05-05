from PyQt5 import QtCore, QtGui, QtWidgets
from random import sample, randint
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import networkx as nx
from Lab204 import Ui_Window_4


class Ui_Window_3(object):

    setA = set()
    setB = set()

    meleList = list()
    femaleList = list()

    w1 = False

    def setupUi(self, MainWindow):
        
        MainWindow.resize(620, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        
        self.frame_setA = QtWidgets.QFrame(self.centralwidget)
        self.frame_setA.setGeometry(QtCore.QRect(20, 20, 210, 276))
        self.frame_setA.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_setA.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_setA.setObjectName("frame_setA")

        self.listWidget_setA = QtWidgets.QListWidget(self.frame_setA)
        self.listWidget_setA.setGeometry(QtCore.QRect(20, 36, 170, 220))
        self.listWidget_setA.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget_setA.setProperty("showDropIndicator", False)
        self.listWidget_setA.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listWidget_setA.setObjectName("listWidget_setA")

        self.label_setA = QtWidgets.QLabel(self.frame_setA)
        self.label_setA.setGeometry(QtCore.QRect(70, 10, 80, 16))
       
        self.frame_setB = QtWidgets.QFrame(self.centralwidget)
        self.frame_setB.setGeometry(QtCore.QRect(250, 20, 210, 276))
        self.frame_setB.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_setB.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_setB.setObjectName("frame_setB")

        self.listWidget_setB = QtWidgets.QListWidget(self.frame_setB)
        self.listWidget_setB.setGeometry(QtCore.QRect(20, 36, 170, 220))
        self.listWidget_setB.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget_setB.setProperty("showDropIndicator", False)
        self.listWidget_setB.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listWidget_setB.setObjectName("listWidget_setB")

        self.label_setB = QtWidgets.QLabel(self.frame_setB)
        self.label_setB.setGeometry(QtCore.QRect(70, 10, 80, 16))
        
        self.pushButton_S = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_S.setGeometry(QtCore.QRect(480, 40, 120, 32))
        self.pushButton_S.setObjectName("pushButton_S")
        self.pushButton_S.pressed.connect(self.relation_S)

        self.pushButton_R = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_R.setGeometry(QtCore.QRect(480, 100, 120, 32))
        self.pushButton_R.setObjectName("pushButton_R")
        self.pushButton_R.pressed.connect(self.relation_R)

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 301, 500, 260))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
    
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.gridLayout.addWidget(self.canvas, 0, 0, 0, 0)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")

        self.menu = QtWidgets.QMenu(self.menubar)
        MainWindow.setMenuBar(self.menubar)

        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("win_4")
        self.action_4.triggered.connect(lambda: self.menubarTriggered(self.action_4))

        self.menu.addAction(self.action_4)

        self.menubar.addAction(self.menu.menuAction())

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.refreshLists()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Вікно 3"))
        self.label_setA.setText(_translate("MainWindow", "Множина А"))
        self.label_setB.setText(_translate("MainWindow", "Множина B"))
        self.pushButton_S.setText(_translate("MainWindow", "Відобразити S"))
        self.pushButton_R.setText(_translate("MainWindow", "Відобразити R"))
        self.menu.setTitle(_translate("MainWindow", "Вікна"))
        self.action_4.setText(_translate("MainWindow", "Вікно 4"))
        self.action_4.setShortcut(_translate("MainWindow", "Ctrl+4"))
  

    def refreshLists(self):
        self.listWidget_setA.clear()
        self.listWidget_setB.clear()
        for i in self.setA:
            self.listWidget_setA.addItem(i)

        for i in self.setB:
            self.listWidget_setB.addItem(i)


    def plotS(self):
        
        tmp = 3
        self.w1 = True
        
        self.g1 = nx.DiGraph()
        self.g1.clear()
        for n in self.setA:
            self.g1.add_node(n, pos=(tmp, 2))
            tmp += 3

        tmp = 3

        for n in self.setB:
            self.g1.add_node(n, pos=(tmp, 1))
            tmp += 3

        self.g1.add_edges_from(relationS, color="b")

        edges = self.g1.edges()
        colors = [self.g1[u][v]['color'] for u,v in edges]
        pos = nx.get_node_attributes(self.g1,'pos')
        nx.draw_networkx(self.g1, pos=pos, arrows=True, with_labels=True, edges=edges,node_size = 300, font_size=8, edge_color=colors)
        self.figure.suptitle("S - blue  R - red", fontsize=10)
        self.canvas.draw_idle()
        

    def plotR(self):
        
        tmp = 3
        
        self.g1 = nx.DiGraph()
        self.g1.clear()
        
        for n in self.setA:
            self.g1.add_node(n, pos=(tmp, 2))
            tmp += 3

        tmp = 3

        for n in self.setB:
            self.g1.add_node(n, pos=(tmp, 1))
            tmp += 3

        self.g1.add_edges_from(relationR, color="r")

        edges = self.g1.edges()
        colors = [self.g1[u][v]['color'] for u,v in edges]
        pos = nx.get_node_attributes(self.g1,'pos')
        
        nx.draw_networkx(self.g1, pos=pos, arrows=True, edge_color=colors, with_labels=True, edges=edges,node_size = 300, font_size=8)
        self.canvas.draw_idle()
        

    def relation_S(self):
        global maleList1 
        global relationS 
        maleList1 = list()
        relationS = list()

        for i in self.setA:
            if i in self.meleList:
                maleList1.append(i)


        for i in sample(maleList1, len(maleList1)):
            num = randint(1, 3)
            for k in sample(self.setB, num):
                tmp = True
                for s in relationS:
                    if s[1] == k:
                        tmp = False
                    if i == k:
                        tmp = False
                if tmp:
                    relationS.append([i,k])

        self.plotS()


    def relation_R(self):
        if self.w1 == False:
            self.statusbar.setStyleSheet("color: red")
            self.statusbar.showMessage("Спочатку відобразіть S", 10000)
        elif self.w1:
            femaleList1 = list()
            global relationR 
            relationR = list()

            for i in self.setB:
                if i in self.femaleList:
                    femaleList1.append(i)

            for i in sample(maleList1, len(maleList1)):
                for k in sample(femaleList1, 1):
                    tmp = True
                    if [i,k] in relationS:
                        tmp = False

                    for s in relationR:
                        if s[1] == k:
                            tmp = False

                    if tmp:
                        relationR.append([i,k])
                    
            self.plotR()


    def menubarTriggered(self, m): 
        if m.objectName() == "win_4":
            self.window4 = QtWidgets.QMainWindow()
            self.ui4 = Ui_Window_4()
            Ui_Window_4.relatoinS = relationS
            Ui_Window_4.relationR = relationR
            Ui_Window_4.setA = self.setA
            Ui_Window_4.setB = self.setB
            self.ui4.setupUi(self.window4)
            self.window4.setWindowTitle("Вікно 4")
            self.window4.show()
            





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Window_3()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

