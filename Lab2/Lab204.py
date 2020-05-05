from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import networkx as nx
import itertools

class Ui_Window_4(object):

    relatoinS = list()
    relationR = list()

    setA = set()
    setB = set()

    def setupUi(self, MainWindow):
        
        MainWindow.resize(1280, 760)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        
        self.pushButton_Show = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Show.setGeometry(QtCore.QRect(20, 40, 151, 32))
        self.pushButton_Show.setObjectName("pushButton_Show")
        self.pushButton_Show.pressed.connect(self.plotButtn)

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 100, 400, 300))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout_1 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_1.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_1.setObjectName("gridLayout_1")

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(440, 100, 400, 300))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(860, 100, 400, 300))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")

        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(20, 420, 400, 300))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")

        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(440, 420, 400, 300))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")

        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Show.setText(_translate("MainWindow", "Відобразити графи"))


    def graphUnion(self):
        self.figure_1 = plt.figure()
        self.figure_1.suptitle("R ∪ S")
        self.canvas_1 = FigureCanvas(self.figure_1)
        self.gridLayout_1.addWidget(self.canvas_1, 0, 0, 0, 0)
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

        self.g1.add_edges_from(unionSR)

        pos = nx.get_node_attributes(self.g1,'pos')
        
        nx.draw_networkx(self.g1, pos=pos, arrows=True, edge_color="b",edges=self.g1.edges(), with_labels=True,node_size = 300, font_size=8)
        

    def graphInter(self):
        self.figure_2 = plt.figure()
        self.figure_2.suptitle("R ∩ S")
        self.canvas_2 = FigureCanvas(self.figure_2)
        self.gridLayout_2.addWidget(self.canvas_2, 0, 0, 0, 0)
        tmp = 3
        
        self.g2 = nx.DiGraph()
        self.g2.clear()
        
        for n in self.setA:
            self.g2.add_node(n, pos=(tmp, 2))
            tmp += 3

        tmp = 3

        for n in self.setB:
            self.g2.add_node(n, pos=(tmp, 1))
            tmp += 3

        self.g2.add_edges_from(interseptSR)

        pos = nx.get_node_attributes(self.g2,'pos')
        
        nx.draw_networkx(self.g2, pos=pos, arrows=True, edge_color="b",edges=self.g2.edges(), with_labels=True,node_size = 300, font_size=8)
        

    def graphSubsRS(self):
        self.figure_3 = plt.figure()
        self.figure_3.suptitle("R \ S")
        self.canvas_3 = FigureCanvas(self.figure_3)
        self.gridLayout_3.addWidget(self.canvas_3, 0, 0, 0, 0)
        tmp = 3
        
        self.g3 = nx.DiGraph()
        self.g3.clear()
        
        for n in self.setA:
            self.g3.add_node(n, pos=(tmp, 2))
            tmp += 3

        tmp = 3

        for n in self.setB:
            self.g3.add_node(n, pos=(tmp, 1))
            tmp += 3

        self.g3.add_edges_from(substractRS)

        pos = nx.get_node_attributes(self.g3,'pos')
        
        nx.draw_networkx(self.g3, pos=pos, arrows=True, edge_color="b",edges=self.g3.edges(), with_labels=True,node_size = 300, font_size=8)
        

    def graphSubsUR(self):
        self.figure_4 = plt.figure()
        self.figure_4.suptitle("U\R")
        self.canvas_4 = FigureCanvas(self.figure_4)
        self.gridLayout_4.addWidget(self.canvas_4, 0, 0, 0, 0)
        tmp = 3
        
        self.g4 = nx.DiGraph()
        self.g4.clear()
        
        for n in self.setA:
            self.g4.add_node(n, pos=(tmp, 2))
            tmp += 3

        tmp = 3

        for n in self.setB:
            self.g4.add_node(n, pos=(tmp, 1))
            tmp += 3

        self.g4.add_edges_from(substractionUR)

        pos = nx.get_node_attributes(self.g4,'pos')
        
        nx.draw_networkx(self.g4, pos=pos, arrows=True, edge_color="b",edges=self.g4.edges(), with_labels=True,node_size = 300, font_size=8)
        

    def graphSturned(self):
        self.figure_5 = plt.figure()
        self.figure_5.suptitle("S^-1")
        self.canvas_5 = FigureCanvas(self.figure_5)
        self.gridLayout_5.addWidget(self.canvas_5, 0, 0, 0, 0)
        tmp = 3
        
        self.g5 = nx.DiGraph()
        self.g5.clear()
        
        for n in self.setA:
            self.g5.add_node(n, pos=(tmp, 2))
            tmp += 3

        tmp = 3

        for n in self.setB:
            self.g5.add_node(n, pos=(tmp, 1))
            tmp += 3

        self.g5.add_edges_from(sTurned)

        pos = nx.get_node_attributes(self.g5,'pos')
        
        nx.draw_networkx(self.g5, pos=pos, arrows=True, edge_color="b",edges=self.g5.edges(), with_labels=True,node_size = 300, font_size=8)
        

    def sUnionR(self):
        global unionSR
        unionSR = list()
        for i in self.relatoinS:
            unionSR.append(i)
            
        for i in self.relationR:
            if i not in unionSR:
                unionSR.append(i)


        
        self.graphUnion()


    def sInterR(self):
        global interseptSR
        interseptSR = list()

        for i in self.relatoinS:
            if i in self.relationR:
                interseptSR.append(i)

        
        self.graphInter()
        

    def rSubstrR(self):
        global substractRS
        substractRS = list()

        for i in self.relationR:
            if i not in self.relatoinS:
                substractRS.append(i)

        
        self.graphSubsRS()


    def uSubstrR(self):
        global substractionUR
        substractionUR = list()
        

        u = [[i, k] for i in list(self.setA) for k in list(self.setB)]

        

        for i in u:
            if i not in self.relationR:
                substractionUR.append(i)

        
        self.graphSubsUR()


    def sTurned(self):
        global sTurned
        sTurned = list()

        for i in self.relatoinS:
            sTurned.append([i[1],i[0]])

        
        self.graphSturned()


    def plotButtn(self):
        self.sUnionR()
        self.sInterR()
        self.rSubstrR()
        self.uSubstrR()
        self.sTurned()








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Window_4()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

