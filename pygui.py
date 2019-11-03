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
        MainWindow.resize(1054, 728)
        MainWindow.setMouseTracking(True)
        MainWindow.setFocusPolicy(QtCore.Qt.WheelFocus)
        MainWindow.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(95, 198, 203, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setStyleSheet("font: 20pt \"Mistral\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(98, 203, 163, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px;\n"
"border-width: 4px;\n"
"border-style: outset;\n"
"border-color: beige;\n"
"text-transform: capitalize;\n"
"text-decoration: none;")
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(800, 670, 171, 41))
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(98, 203, 163, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px;\n"
"border-width: 4px;\n"
"border-style: outset;\n"
"border-color: beige;\n"
"font: 75 10pt \"Segoe Script\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setEnabled(True)
        self.treeWidget.setGeometry(QtCore.QRect(30, 80, 371, 581))
        self.treeWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.treeWidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 246, 246, 246), stop:1 rgba(255, 255, 255, 255));\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;\n"
"border-width: 8px;\n"
"border-style: outset;\n"
"border-color: beige;\n"
"padding: 7px")
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        self.select_folder_btn = QtWidgets.QPushButton(self.centralwidget)
        self.select_folder_btn.setEnabled(True)
        self.select_folder_btn.setGeometry(QtCore.QRect(30, 10, 371, 61))
        self.select_folder_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.select_folder_btn.setAutoFillBackground(False)
        self.select_folder_btn.setStyleSheet("font: 20pt \"Mistral\";\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(84, 203, 9, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px;\n"
"border-width: 6px;\n"
"border-style: outset;\n"
"border-color: beige;\n"
"\n"
"")
        self.select_folder_btn.setObjectName("select_folder_btn")
        self.run_btn = QtWidgets.QPushButton(self.centralwidget)
        self.run_btn.setEnabled(True)
        self.run_btn.setGeometry(QtCore.QRect(440, 10, 141, 61))
        self.run_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.run_btn.setStyleSheet("font: 20pt \"Mistral\";\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(84, 203, 9, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px;\n"
"border-width: 4px;\n"
"border-style: outset;\n"
"border-color: beige;")
        self.run_btn.setObjectName("run_btn")
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setEnabled(True)
        self.stop_btn.setGeometry(QtCore.QRect(580, 10, 131, 61))
        self.stop_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stop_btn.setStyleSheet("font: 20pt \"Mistral\";\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(84, 203, 9, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px;\n"
"border-width: 4px;\n"
"border-style: outset;\n"
"border-color: beige")
        self.stop_btn.setObjectName("stop_btn")
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setEnabled(True)
        self.clear_btn.setGeometry(QtCore.QRect(860, 10, 151, 61))
        self.clear_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear_btn.setStyleSheet("font: 20pt \"Mistral\";\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(84, 203, 9, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px;\n"
"border-width: 4px;\n"
"border-style: outset;\n"
"border-color: beige")
        self.clear_btn.setObjectName("clear_btn")
        self.logBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.logBrowser.setGeometry(QtCore.QRect(445, 81, 571, 581))
        self.logBrowser.setMouseTracking(True)
        self.logBrowser.setAutoFillBackground(True)
        self.logBrowser.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 246, 246, 246), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px;\n"
"border-width: 4px;\n"
"border-style: outset;\n"
"border-color: beige")
        self.logBrowser.setObjectName("logBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(640, 670, 161, 41))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(98, 203, 163, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px;\n"
"border-width: 4px;\n"
"border-style: outset;\n"
"border-color: beige;\n"
"font: 75 10pt \"Segoe Script\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.log_btn = QtWidgets.QPushButton(self.centralwidget)
        self.log_btn.setGeometry(QtCore.QRect(710, 10, 151, 61))
        self.log_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.log_btn.setStyleSheet("font: 20pt \"Mistral\";\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(84, 203, 9, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px;\n"
"border-width: 4px;\n"
"border-style: outset;\n"
"border-color: beige\n"
"")
        self.log_btn.setObjectName("log_btn")
        self.select_all_btn = QtWidgets.QPushButton(self.centralwidget)
        self.select_all_btn.setGeometry(QtCore.QRect(50, 670, 161, 41))
        self.select_all_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.select_all_btn.setStyleSheet("font: 75 10pt \"Segoe Script\";")
        self.select_all_btn.setObjectName("select_all_btn")
        self.unselect_all_btn = QtWidgets.QPushButton(self.centralwidget)
        self.unselect_all_btn.setGeometry(QtCore.QRect(210, 670, 161, 41))
        self.unselect_all_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.unselect_all_btn.setStyleSheet("font: 75 10pt \"Segoe Script\";")
        self.unselect_all_btn.setObjectName("unselect_all_btn")
        self.select_folder_btn.raise_()
        self.run_btn.raise_()
        self.stop_btn.raise_()
        self.clear_btn.raise_()
        self.label_2.raise_()
        self.treeWidget.raise_()
        self.logBrowser.raise_()
        self.label.raise_()
        self.log_btn.raise_()
        self.select_all_btn.raise_()
        self.unselect_all_btn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Vlaeria Basov"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Files"))
        self.select_folder_btn.setText(_translate("MainWindow", "Select Files"))
        self.run_btn.setText(_translate("MainWindow", "Run"))
        self.stop_btn.setText(_translate("MainWindow", "Stop"))
        self.clear_btn.setText(_translate("MainWindow", "Clear"))
        self.label.setText(_translate("MainWindow", "Iliya Livshets"))
        self.log_btn.setText(_translate("MainWindow", "Log"))
        self.select_all_btn.setText(_translate("MainWindow", "check All"))
        self.unselect_all_btn.setText(_translate("MainWindow", "Uncheck All"))
