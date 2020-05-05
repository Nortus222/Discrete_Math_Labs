
from PyQt5 import QtCore, QtGui, QtWidgets
from Qstyle import style
import matplotlib.pyplot as plt
import networkx as nx
from random import sample, randint
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from collections import OrderedDict

class IndexedQueue(OrderedDict):
    "Queue-like container with fast search"
    def push(self, item):
        self[item] = None

    def pop(self):
        return OrderedDict.popitem(self, last=False)[0]


class Ui_Window_2(object):

    nodesNum = 0
    tmp = -1

    def setupUi(self, MainWindow):

        MainWindow.resize(885, 500)

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        font = QtGui.QFont()

        self.frame_GraphPath = QtWidgets.QFrame(self.centralwidget)
        self.frame_GraphPath.setGeometry(QtCore.QRect(20, 40, 345, 214))
        self.frame_GraphPath.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_GraphPath.setFrameShadow(QtWidgets.QFrame.Raised)

        self.label_GraphSetPath = QtWidgets.QLabel(self.frame_GraphPath)
        self.label_GraphSetPath.setGeometry(QtCore.QRect(20, 20, 305, 20))
        font.setPointSize(18)
        font.setBold(True)
        self.label_GraphSetPath.setFont(font)
        font.setBold(False)

        self.label_PathStart = QtWidgets.QLabel(self.frame_GraphPath)
        self.label_PathStart.setGeometry(QtCore.QRect(40, 70, 155, 20))
        font.setPointSize(16)
        self.label_PathStart.setFont(font)

        self.label_PathEnd = QtWidgets.QLabel(self.frame_GraphPath)
        self.label_PathEnd.setGeometry(QtCore.QRect(40, 109, 130, 20))
        self.label_PathEnd.setFont(font)

        self.spinBox_PathStart = QtWidgets.QSpinBox(self.frame_GraphPath)
        self.spinBox_PathStart.setGeometry(QtCore.QRect(215, 70, 48, 24))

        self.spinBox_PathEnd = QtWidgets.QSpinBox(self.frame_GraphPath)
        self.spinBox_PathEnd.setGeometry(QtCore.QRect(215, 109, 48, 24))

        self.pushButton_PathCalculate = QtWidgets.QPushButton(self.frame_GraphPath)
        self.pushButton_PathCalculate.setGeometry(QtCore.QRect(110, 159, 113, 32))
        self.pushButton_PathCalculate.pressed.connect(self.levitAlgorithm)

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(365, 7, 500, 500))

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
        self.label_GraphSetPath.setText(_translate("MainWindow", "Визначення найкоротшого шляху"))
        self.label_PathStart.setText(_translate("MainWindow", "Початкова вершина"))
        self.label_PathEnd.setText(_translate("MainWindow", "Кінцева вершина"))
        self.pushButton_PathCalculate.setText(_translate("MainWindow", "Розрахувати"))

    def restoreGraph(self):
        edges = self.g.edges()
        for u,v in edges:
            self.g[u][v]['color']="b"
            self.g[u][v]['weight']=1
        global colors
        colors = [self.g[u][v]['color'] for u,v in edges]
        global weights
        weights = [self.g[u][v]['weight'] for u,v in edges]
        

    def graphCreate(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.gridLayout.addWidget(self.canvas, 0, 0, 0, 0)
        self.g = nx.DiGraph()

        for i in range(self.nodesNum):
            self.g.add_node(i)

        for i in range(self.nodesNum):
            num = randint(1, self.nodesNum)
            for k in sample(self.g.nodes(), num):
                self.g.add_edge(i, k)

        self.restoreGraph()
        global pos
        pos = nx.spring_layout(self.g)
        nx.draw_networkx(self.g, arrows=True, pos=pos, edge_color=colors, node_color="y", width=weights)   
        
    def colorEdges(self, path):
        pth = list()
        for i in range(len(path)-1):
            pth.append(tuple(list(path)[i:i+2]))

        self.restoreGraph()

        for i in pth:
            if i in self.g.edges():
                self.g[i[0]][i[1]]['color']="r"
                self.g[i[0]][i[1]]['weight']=3
        
        colors = [self.g[u][v]['color'] for u,v in self.g.edges()]
        weights = [self.g[u][v]['weight'] for u,v in self.g.edges()]
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.gridLayout.addWidget(self.canvas, 0, 0, 0, 0)
        nx.draw_networkx(self.g, arrows=True, pos=pos, edge_color=colors, node_color="y", width=weights)       
    
    def check(self):
        s1 = int(self.spinBox_PathStart.value())
        s2 = int(self.spinBox_PathEnd.value())
        if s1 < (self.nodesNum - 1) and s2 <= (self.nodesNum - 1) and s2 - s1 != 0:
            return True
        else:
            self.statusbar.setStyleSheet("color: red")
            self.statusbar.showMessage("Некоректно заданий проміжок", 5000)

    def levitAlgorithm(self):

        "(d,(c,(b,(a,())))) => (a, b, c, d)"
        restore_path = lambda tup: (*restore_path(tup[1]),tup[0]) if tup else ()

        def relax(u , v, w):
            if (dist[v] > dist[u] + w):
                dist[v] = dist[u] + w
                path[v] = (v, path[u])
                return True
            return False

        if self.tmp == -1 and self.check() or int(self.spinBox_PathStart.value()) != self.tmp:
            inf = 10000000000
            end = int(self.spinBox_PathEnd.value())
            v0 = int(self.spinBox_PathStart.value())
            dist = [inf for i in range(self.nodesNum)]
            dist[v0] = 0
            global path
            path = {v0:(v0,())}
            m0 = set()
            m1, m1_urg = IndexedQueue.fromkeys([v0]), IndexedQueue()
            m2 = set(self.g.nodes()) - {v0}

            while m1 or m1_urg:
                u = m1_urg.pop() if m1_urg else m1.pop()
                c = 1
                for v in list(self.g.successors(u)):
                    if v in m2:
                        m1.push(v)
                        m2.discard(v)
                        relax(u, v, c)
                    elif v in m1:
                        relax(u, v, c)
                    elif v in m0 and relax(u, v, c):
                        m1_urg.push(v)
                        m0.discard(v)
                m0.add(u)
            self.colorEdges(restore_path(path[end]))
            self.tmp = v0
        elif self.tmp >= 0 and self.check():
            self.colorEdges(restore_path(path[int(self.spinBox_PathEnd.value())]))
        
            
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Window_2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

