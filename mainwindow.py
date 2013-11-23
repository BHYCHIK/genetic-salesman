# -*- coding: utf-8 -*-
from PyQt4.QtGui import QMainWindow, QListWidgetItem, QMessageBox, QHeaderView
from ui_mainwindow import Ui_MainWindow
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt, pyqtSignal
import salesman_solver

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.app = app
        self.btnSolve.clicked.connect(self.onBtnSolve)
        self.points = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0,5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (0, 13), (0, 14), (0, 15), (0, 16), (0, 17)]
    def onBtnSolve(self):
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
            self.pbSolutionFound.setValue(int((i / generations_num) * 100))
            i = i + 1
        self.lePathLength.setText(str(path_len))
