# -*- coding: utf-8 -*-
from PyQt4.QtGui import QMainWindow, QListWidgetItem, QMessageBox, QHeaderView
from ui_mainwindow import Ui_MainWindow
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt, pyqtSignal
from PyQt4.QtGui import QPalette, QColor
import salesman_solver

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.app = app
        self.btnSolve.clicked.connect(self.onBtnSolve)
        self.btnClearPoints.clicked.connect(self.onBtnClearPoints)
        self.wDrawing.mouseMoveEvent = self.onMouseDrawingMove
        self.wDrawing.setMouseTracking(True)
        self.wDrawing.leaveEvent = self.onMouseDrawingLeave
        self.wDrawing.mousePressEvent = self.onMousePressDrawing
        self.wDrawing.setAutoFillBackground(True)
        self.wDrawing.paintEvent = self.paintDrawingEvent
        self.points = []
        self.solving = False
        self.solution = None
        palette = QPalette()
        role = self.wDrawing.backgroundRole()
        palette.setColor(role, QColor('white'))
        self.wDrawing.setPalette(palette)
        self.wDrawing.update()
    def onBtnSolve(self):
        self.solving = True
        self.teLog.clear()
        mutation_probability = float(self.leMutationProbability.text())
        print("mutation probability:", mutation_probability)
        population_size = int(self.lePopulationSize.text())
        print("population size:", population_size)
        generations_num = int(self.leGenerationsNum.text())
        print("generations number:", generations_num)
        i = 0
        for (path_len, path) in salesman_solver.solve(self.points, population_size, mutation_probability, generations_num):
            print("path length:", path_len)
            print("path:", path)
            self.teLog.appendPlainText("Шаг %d. Лучший путь %s. Длина лучшего пути %d" % (i, path, path_len))
            self.solution = path
            self.pbSolutionFound.setValue(int((i / generations_num) * 100))
            i = i + 1
            if (i % 10 == 0):
                self.wDrawing.update()
        self.lePathLength.setText(str(path_len))
        self.solving = False
    def onMouseDrawingMove(self, event):
        self.lblMousePosition.setText("(%d, %d)" % (event.x(), event.y()))
    def onMouseDrawingLeave(self, event):
        self.lblMousePosition.setText("")
    def onBtnClearPoints(self):
        self.points = []
        self.wDrawing.update()
    def onMousePressDrawing(self, event):
        self.points.append((event.x(), event.y()))
        self.teLog.appendPlainText("Добавлена точка (%d, %d)" % (event.x(), event.y()))
        self.wDrawing.update()
    def paintDrawingEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self.wDrawing)
        pen = QtGui.QPen()
        pen.setColor(QColor('red'))
        pen.setWidth(3)
        qp.setPen(pen)
        for p in self.points:
            qp.drawPoint(p[0], p[1])
        if self.solving:
            for i in list(range(0, len(self.solution) - 1)):
                qp.drawLine(self.points[self.solution[i]][0], self.points[self.solution[i]][1], self.points[self.solution[i + 1]][0], self.points[self.solution[i + 1]][1])
        qp.end()
