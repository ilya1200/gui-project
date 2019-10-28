import subprocess
from subprocess import Popen
import sys
import os
import psutil
from builtins import super

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QCursor

import pygui


class ExampleApp(QtWidgets.QMainWindow, pygui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.treeWidget.setHeaderLabels(['Files'])
        self.treeWidget.setAlternatingRowColors(True)
        self.current_dir = ""

        self.select_folder_btn.clicked.connect(self.browse_folder)
        self.start_btn.clicked.connect(self.run_checked_tests)
        self.stop_btn.clicked.connect(self.stop_all_tests)
        self.clear_btn.clicked.connect(self.clear)
        self.refresh_btn.clicked.connect(self.print_logs)
        self.file_types = {
            ".js": "node",
            ".py": "python"
        }
        self.processes = []

        self.start_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.stop_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.select_folder_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.clear_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.refresh_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.stop_btn.setStyleSheet(
            "QPushButton:hover { background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FAFBFE, stop: 1 #DCDEF1) }")
        self.start_btn.setStyleSheet(
            "QPushButton:hover { background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FAFBFE, stop: 1 #DCDEF1) }")
        self.clear_btn.setStyleSheet(
            "QPushButton:hover { background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FAFBFE, stop: 1 #DCDEF1) }")
        self.select_folder_btn.setStyleSheet(
            "QPushButton:hover { background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FAFBFE, stop: 1 #DCDEF1) }")
        self.refresh_btn.setStyleSheet(
            "QPushButton:hover { background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FAFBFE, stop: 1 #DCDEF1) }")
        self.label_2.setOpenExternalLinks(True)
        self.label.setOpenExternalLinks(True)
        self.label_2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2.setStyleSheet(
            "QLabel:hover { background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FAFBFE, stop: 1 #DCDEF1) }")
        self.label.setStyleSheet(
            "QLabel:hover { background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FAFBFE, stop: 1 #DCDEF1) }")
        self.label_2.setText("<a href=\"https://www.linkedin.com/in/valeria-basova-58495318/\">Valeria Basov</a>")
        self.label.setText("<a href=\"https://www.linkedin.com/in/ilya-livshits-b12295108\">Iliya Livshits</a>")

    def browse_folder(self):
        self.current_dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Select a folder")
        if self.current_dir:
            self.treeWidget.clear()
            for file_name in os.listdir(self.current_dir):  # for each file in directory
                if self.is_allowed_file(file_name):
                    item = QtWidgets.QTreeWidgetItem(self.treeWidget, [file_name])
                    item.setCheckState(0, QtCore.Qt.Unchecked)

    def is_allowed_file(self, file_name):
        if not self.file_types:
            return True
        for eof in self.file_types:
            if file_name.endswith(eof):
                return True
        return False

    def find_checked(self):
        checked_items = list()
        root = self.treeWidget.invisibleRootItem()
        child_count = root.childCount()

        for i in range(child_count):
            i_child = root.child(i)
            if i_child.checkState(0) == QtCore.Qt.Checked:
                checked_items.append(i_child.text(0))
        return checked_items

    def run_file_with(self, file_name):
        if not self.file_types:
            return ""

        for eof in self.file_types:
            if file_name.endswith(eof):
                return self.file_types[eof]
        return ""

    def kill(self, proc_pid):
        Popen("TASKKILL /F /PID {pid} /T".format(pid=proc_pid))

    def run_checked_tests(self):
        checked_files = self.find_checked()
        if not checked_files:
            return

        for file_name in checked_files:
            print(f"Run file: {file_name}")
            process = subprocess.Popen(f"{self.run_file_with(file_name)} {file_name}", shell=True, cwd=self.current_dir)

            self.processes.append({"id": process.pid, "file_name": file_name, "process": process})

    def print_logs(self):
        logger_file_path = self.current_dir + "/log/"
        for file in os.listdir(logger_file_path):
            if file.endswith(".log"):
                logger_file_full_path = logger_file_path + file
                with open(logger_file_full_path, "r") as logger_file:
                    self.logBrowser.append(logger_file.read())

    def stop_all_tests(self):
        for p in self.processes:
            self.kill(p["id"])
        print("All tests stopped")

    def clear(self):
        self.logBrowser.clear()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
