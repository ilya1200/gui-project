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
        MainWindow.resize(583, 600)
        MainWindow.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(95, 198, 203, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("font: 20pt \"Mistral\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(98, 203, 163, 255), stop:1 rgba(255, 255, 255, 255));\n"
"text-decoration: underline;\n"
"border-radius: 10px;\n"
"border-width: 4px;\n"
"border-style: outset;\n"
"border-color: beige")
        self.centralwidget.setObjectName("centralwidget")
        self.select_folder_btn = QtWidgets.QPushButton(self.centralwidget)
        self.select_folder_btn.setGeometry(QtCore.QRect(10, 10, 211, 61))
        self.select_folder_btn.setStyleSheet("font: 20pt \"Mistral\";\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(84, 203, 9, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px;\n"
"border-width: 4px;\n"
"border-style: outset;\n"
"border-color: beige")
        self.select_folder_btn.setObjectName("select_folder_btn")
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setGeometry(QtCore.QRect(400, 10, 121, 61))
        self.stop_btn.setStyleSheet("font: 20pt \"Mistral\";\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(84, 203, 9, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px;\n"
"border-width: 4px;\n"
"border-style: outset;\n"
"border-color: beige")
        self.stop_btn.setObjectName("stop_btn")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(270, 10, 131, 61))
        self.start_btn.setStyleSheet("font: 20pt \"Mistral\";\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(84, 203, 9, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px;\n"
"border-width: 4px;\n"
"border-style: outset;\n"
"border-color: beige")
        self.start_btn.setObjectName("start_btn")
        self.logBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.logBrowser.setGeometry(QtCore.QRect(290, 80, 431, 471))
        self.logBrowser.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 246, 246, 246), stop:1 rgba(255, 255, 255, 255));\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;\n"
"border-width: 6px;\n"
"border-style: outset;\n"
"border-color: beige;\n"
"padding: 5px")
        self.logBrowser.setObjectName("logBrowser")
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setGeometry(QtCore.QRect(640, 10, 131, 61))
        self.clear_btn.setStyleSheet("font: 20pt \"Mistral\";\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(84, 203, 9, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px;\n"
"border-width: 4px;\n"
"border-style: outset;\n"
"border-color: beige")
        self.clear_btn.setObjectName("clear_btn")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(10, 80, 211, 471))
        self.treeWidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 246, 246, 246), stop:1 rgba(255, 255, 255, 255));\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;\n"
"border-width: 6px;\n"
"border-style: outset;\n"
"border-color: beige;\n"
"padding: 5px")
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.refresh_btn = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_btn.setGeometry(QtCore.QRect(520, 10, 121, 61))
        self.refresh_btn.setStyleSheet("font: 20pt \"Mistral\";\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(84, 203, 9, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px;\n"
"border-width: 4px;\n"
"border-style: outset;\n"
"border-color: beige")
        self.refresh_btn.setObjectName("refresh_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 560, 151, 31))
        self.label.setStyleSheet("font: 12pt \"Matura MT Script Capitals\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(98, 203, 163, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px;\n"
"border-width: 4px;\n"
"border-style: outset;\n"
"border-color: beige")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(520, 560, 151, 31))
        self.label_2.setStyleSheet("font: 12pt \"Matura MT Script Capitals\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(98, 203, 163, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px;\n"
"border-width: 4px;\n"
"border-style: outset;\n"
"border-color: beige")
        self.label_2.setObjectName("label_2")
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
        self.refresh_btn.setText(_translate("MainWindow", "Refresh"))
        self.label.setText(_translate("MainWindow", "Ilya Livshits"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
