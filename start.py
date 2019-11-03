import subprocess
from subprocess import Popen
import sys
import os
import psutil
from builtins import super
from datetime import date
import datetime

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QCursor

import pygui


class ExampleApp(QtWidgets.QMainWindow, pygui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.file_types = {
            ".js": "node"
        }
        self.processes = []
        self.current_dir = ""

        # Event Handlers
        self.select_folder_btn.clicked.connect(self.browse_folder)
        self.run_btn.clicked.connect(self.run_checked_tests)
        self.stop_btn.clicked.connect(self.stop_all_tests)
        self.clear_btn.clicked.connect(self.clear)
        self.log_btn.clicked.connect(self.print_logs)
        self.select_all_btn.clicked.connect(self.select_all)
        self.unselect_all_btn.clicked.connect(self.unselect_all)

        # Styles
        self.treeWidget.setHeaderLabels(['Files'])

    def select_all(self):
        tree_children = self.get_tree_children()
        for file in tree_children:
            file.setCheckState(0, QtCore.Qt.Checked)

    def unselect_all(self):
        tree_children = self.get_tree_children()
        for file in tree_children:
            file.setCheckState(0, QtCore.Qt.Unchecked)

    def browse_folder(self):
        default_dir = "C:/Users/ilya1/OneDrive/Desktop/Automation Selenium Project/Tests"
        self.current_dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Select a folder", directory=default_dir)
        if not self.current_dir:
            return

        self.treeWidget.clear()
        allowed_files = filter(lambda file_name: self.is_allowed_file(file_name), os.listdir(self.current_dir))
        for allowed_file in allowed_files:
            QtWidgets.QTreeWidgetItem(self.treeWidget, [allowed_file]).setCheckState(0, QtCore.Qt.Unchecked)

    def is_allowed_file(self, file_name):
        if not self.file_types:
            return True
        for eof in self.file_types:
            if file_name.endswith(eof):
                return True
        return False

    def get_tree_children(self):
        tree_children = []
        root = self.treeWidget.invisibleRootItem()
        child_count = root.childCount()

        for i in range(child_count):
            i_child = root.child(i)
            tree_children.append(i_child)

        return tree_children

    def run_file_with(self, file_name):
        if not self.file_types:
            return ""

        for eof in self.file_types:
            if file_name.endswith(eof):
                return self.file_types[eof]
        return ""

    def kill(self, pid):
        try:
            process = psutil.Process(pid)
            for process_child in process.children(recursive=True):
                process_child.kill()
            process.kill()
        except Exception as e:
            print(f'Got exception: {e}')

    def run_checked_tests(self):
        checked_files = list(map(lambda file: file.text(0),
                                 filter(lambda file: file.checkState(0) == QtCore.Qt.Checked,
                                        self.get_tree_children())))
        if not checked_files:
            return

        run_command = " && ".join(
            list(map(lambda file_name: f"{self.run_file_with(file_name)} {file_name}", checked_files)))
        process = subprocess.Popen(run_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,
                                   shell=True, cwd=self.current_dir, universal_newlines=True, start_new_session=True)
        self.processes.append({"id": process.pid})
        self.run_btn.setEnabled(False)

    def print_logs(self):
        logger_file_path = self.current_dir + "/log/"
        for file in os.listdir(logger_file_path):
            if file.endswith(".log"):
                logger_file_full_path = logger_file_path + file
                logger_file = open(logger_file_full_path, "r")
                log_content = logger_file.read()
                self.logBrowser.append(log_content)  # log to screen

                # log to file
                now = datetime.datetime.now().strftime("%H-%M-%S %Y-%m-%d")
                log_file_name = f"{logger_file_path}{now}.log"
                with open(log_file_name, "w") as other_logger_file:
                    other_logger_file.write(log_content)

    def stop_all_tests(self):
        for p in self.processes:
            self.kill(p["id"])
        self.processes = []
        self.run_btn.setEnabled(True)

    def clear(self):
        self.logBrowser.clear()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
