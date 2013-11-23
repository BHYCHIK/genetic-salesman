# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Nov 23 23:57:37 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(980, 683)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 400, 961, 225))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.teLog = QtGui.QPlainTextEdit(self.layoutWidget)
        self.teLog.setObjectName(_fromUtf8("teLog"))
        self.verticalLayout_2.addWidget(self.teLog)
        self.pbSolutionFound = QtGui.QProgressBar(self.layoutWidget)
        self.pbSolutionFound.setProperty("value", 100)
        self.pbSolutionFound.setObjectName(_fromUtf8("pbSolutionFound"))
        self.verticalLayout_2.addWidget(self.pbSolutionFound)
        self.wDrawing = QtGui.QWidget(self.centralwidget)
        self.wDrawing.setGeometry(QtCore.QRect(20, 10, 731, 361))
        self.wDrawing.setObjectName(_fromUtf8("wDrawing"))
        self.lblMousePosition = QtGui.QLabel(self.centralwidget)
        self.lblMousePosition.setGeometry(QtCore.QRect(777, 380, 181, 20))
        self.lblMousePosition.setText(_fromUtf8(""))
        self.lblMousePosition.setObjectName(_fromUtf8("lblMousePosition"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(780, 12, 188, 286))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblGenerations = QtGui.QLabel(self.widget)
        self.lblGenerations.setObjectName(_fromUtf8("lblGenerations"))
        self.verticalLayout.addWidget(self.lblGenerations)
        self.leGenerationsNum = QtGui.QLineEdit(self.widget)
        self.leGenerationsNum.setObjectName(_fromUtf8("leGenerationsNum"))
        self.verticalLayout.addWidget(self.leGenerationsNum)
        self.lblMutationProbability = QtGui.QLabel(self.widget)
        self.lblMutationProbability.setObjectName(_fromUtf8("lblMutationProbability"))
        self.verticalLayout.addWidget(self.lblMutationProbability)
        self.leMutationProbability = QtGui.QLineEdit(self.widget)
        self.leMutationProbability.setObjectName(_fromUtf8("leMutationProbability"))
        self.verticalLayout.addWidget(self.leMutationProbability)
        self.lblPopulationSize = QtGui.QLabel(self.widget)
        self.lblPopulationSize.setObjectName(_fromUtf8("lblPopulationSize"))
        self.verticalLayout.addWidget(self.lblPopulationSize)
        self.lePopulationSize = QtGui.QLineEdit(self.widget)
        self.lePopulationSize.setObjectName(_fromUtf8("lePopulationSize"))
        self.verticalLayout.addWidget(self.lePopulationSize)
        self.btnSolve = QtGui.QPushButton(self.widget)
        self.btnSolve.setObjectName(_fromUtf8("btnSolve"))
        self.verticalLayout.addWidget(self.btnSolve)
        self.lblPathLength = QtGui.QLabel(self.widget)
        self.lblPathLength.setObjectName(_fromUtf8("lblPathLength"))
        self.verticalLayout.addWidget(self.lblPathLength)
        self.lePathLength = QtGui.QLineEdit(self.widget)
        self.lePathLength.setReadOnly(True)
        self.lePathLength.setObjectName(_fromUtf8("lePathLength"))
        self.verticalLayout.addWidget(self.lePathLength)
        self.btnClearPoints = QtGui.QPushButton(self.widget)
        self.btnClearPoints.setObjectName(_fromUtf8("btnClearPoints"))
        self.verticalLayout.addWidget(self.btnClearPoints)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Задача коммивояжер - генетический алгоритм", None, QtGui.QApplication.UnicodeUTF8))
        self.lblGenerations.setText(QtGui.QApplication.translate("MainWindow", "Число поколений", None, QtGui.QApplication.UnicodeUTF8))
        self.leGenerationsNum.setText(QtGui.QApplication.translate("MainWindow", "800", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMutationProbability.setText(QtGui.QApplication.translate("MainWindow", "Вероятность мутации", None, QtGui.QApplication.UnicodeUTF8))
        self.leMutationProbability.setText(QtGui.QApplication.translate("MainWindow", "0.03", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPopulationSize.setText(QtGui.QApplication.translate("MainWindow", "Размер популяции", None, QtGui.QApplication.UnicodeUTF8))
        self.lePopulationSize.setText(QtGui.QApplication.translate("MainWindow", "320", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSolve.setText(QtGui.QApplication.translate("MainWindow", "Решить", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPathLength.setText(QtGui.QApplication.translate("MainWindow", "Длина найденного маршрута", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClearPoints.setText(QtGui.QApplication.translate("MainWindow", "Очистить точки", None, QtGui.QApplication.UnicodeUTF8))

