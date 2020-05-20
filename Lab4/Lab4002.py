
from PyQt5 import QtCore, QtGui, QtWidgets
from Qstyle import style
import matplotlib.pyplot as plt
import networkx as nx
from random import sample, randint, choice
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Ui_Window_2(object):

    nodesNum = 0
    nodeExample = 10
    edgesExample = [[1, 2], [1, 6], [2, 3], [2, 6], [2, 7], [3, 4], [3, 7], [3, 9], [4, 5], [5, 9], [5, 10], [7, 8], [8, 9], [10, 8]]
    btn = "random"

    def setupUi(self, MainWindow):

        MainWindow.resize(885, 500)

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        font = QtGui.QFont()

        self.frame_GraphColor = QtWidgets.QFrame(self.centralwidget)
        self.frame_GraphColor.setGeometry(QtCore.QRect(20, 40, 250, 112))
        self.frame_GraphColor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_GraphColor.setFrameShadow(QtWidgets.QFrame.Raised)

        self.label_GraphSetColor = QtWidgets.QLabel(self.frame_GraphColor)
        self.label_GraphSetColor.setGeometry(QtCore.QRect(20, 20, 210, 20))
        font.setPointSize(18)
        font.setBold(True)
        self.label_GraphSetColor.setFont(font)
        font.setBold(False)

        self.pushButton_GraphColor = QtWidgets.QPushButton(self.frame_GraphColor)
        self.pushButton_GraphColor.setGeometry(QtCore.QRect(70, 60, 113, 32))
        self.pushButton_GraphColor.pressed.connect(self.colorGraph)

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(270, 7, 600, 500))

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 755, 22))

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.centralwidget.setStyleSheet(style)

        self.graphCreate()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label_GraphSetColor.setText(_translate("MainWindow", " Розфарбування графу"))
        self.pushButton_GraphColor.setText(_translate("MainWindow", "Розфарбувати"))
        

    def graphExampleCreate(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.gridLayout.addWidget(self.canvas, 0, 0, 0, 0)
        self.g = nx.Graph()

        tmp = 3

        for i in range(1, 6):
            self.g.add_node(i, pos=(tmp, 1.01))
            tmp += 3

        tmp = 3

        for i in range(6, 11):
            if i == 8 or i == 10:
                self.g.add_node(i,pos=(tmp, 0.998))
            else:
                self.g.add_node(i, pos=(tmp, 1))
            tmp += 3

        self.g.add_edges_from(self.edgesExample)
        global pos
        pos = nx.get_node_attributes(self.g,'pos')
        nx.draw_networkx(self.g, pos=pos, edge_color="black", node_color="white") 

    def graphRandomCreate(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.gridLayout.addWidget(self.canvas, 0, 0, 0, 0)
        self.g = nx.Graph()

        for i in range(1, self.nodesNum+1):
            self.g.add_node(i)
        if self.nodesNum == 2:
            self.g.add_edge(1, 2)
        elif self.nodesNum == 1:
            pass
        else:
            for i in range(1, self.nodesNum+1):
                if self.nodesNum == 3:
                    num = randint(1, 3)
                else:
                    num = randint(1,4)
                for k in sample(self.g.nodes(), num):
                    if i != k:
                        self.g.add_edge(i, k)

        global pos
        pos = nx.spring_layout(self.g)
        nx.draw_networkx(self.g, pos=pos, edge_color="black", node_color="white") 

    def graphCreate(self):
        if self.btn == "example":
            self.graphExampleCreate()
        elif self.btn == "random":
            self.graphRandomCreate()


    def degforming(self, n):
        def getkey(item):
            return item[0]

        degarr = [[0 for i in range(2)] for j in range(1, n+1)]

        for i in range(1, n+1):
            degarr[i-1][0] = self.g.degree(i)
            degarr[i-1][1] = i
        degarr.sort(key=getkey, reverse=True)

        return(degarr)

    def graphColor(self, clr, nclr):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.gridLayout.addWidget(self.canvas, 0, 0, 0, 0)
        
        color = list()
        for i in range(len(clr)):
           color.append(nclr[clr[i]-1])

        nx.draw_networkx(self.g, pos=pos, edge_color="black", node_color=color) 

    def colorGraph(self):
        def checkDop(k):
            p = True
            for j in range(n):
                if (j+1) in list(self.g.neighbors(k)) and colarr[j] == curcol:
                    p = False 
            return p

        def dyer(curcol, node):
            for i in range(n):
                if (i+1) not in list(self.g.neighbors(node)):
                    if colarr[i] == 0 and checkDop(i+1):
                        colarr[i] = curcol

        if self.btn == "example":
            n = self.nodeExample
        elif self.btn == "random":
            n = self.nodesNum

        curcol = 1
        colarr = [0 for i in range(n)]
        sortarr = self.degforming(n)

        for i in range(n):
            if not colarr[(sortarr[i][1] - 1)]:
                colarr[(sortarr[i][1] - 1)] = curcol
                dyer(curcol, sortarr[i][1])
                curcol += 1

        ncollar = ["#"+''.join([choice('0123456789ABCDEF') for i in range(6)])for i in range(len(set(colarr)))]
        self.graphColor(colarr, ncollar)
        


       



        
    

    
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Window_2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

