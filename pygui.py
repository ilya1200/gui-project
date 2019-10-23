# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(787, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 50, 171, 521))
        self.listWidget.setObjectName("listWidget")
        self.select_folder_btn = QtWidgets.QPushButton(self.centralwidget)
        self.select_folder_btn.setGeometry(QtCore.QRect(0, 0, 171, 51))
        self.select_folder_btn.setObjectName("select_folder_btn")
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setGeometry(QtCore.QRect(340, 0, 171, 51))
        self.stop_btn.setObjectName("stop_btn")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(170, 0, 171, 51))
        self.start_btn.setObjectName("start_btn")
        self.logBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.logBrowser.setGeometry(QtCore.QRect(170, 50, 341, 521))
        self.logBrowser.setObjectName("logBrowser")
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setGeometry(QtCore.QRect(60, 520, 101, 31))
        self.clear_btn.setObjectName("clear_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.select_folder_btn.setText(_translate("MainWindow", "Select Folder"))
        self.stop_btn.setText(_translate("MainWindow", "Stop"))
        self.start_btn.setText(_translate("MainWindow", "Start"))
        self.clear_btn.setText(_translate("MainWindow", "Clear"))
