import sys
import os
from subprocess import Popen, PIPE
import psutil
from builtins import super
import datetime
from PyQt5 import QtWidgets, QtCore
import pygui


class ExampleApp(QtWidgets.QMainWindow, pygui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.file_types = {
            ".js": "node"
        }
        self.processes = []
        self.default_dir = "C:/Users/ilya1/OneDrive/Desktop/Automation Selenium Project/Tests"
        self.current_dir = self.default_dir
        self.logger_output_file_full_path = ""

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
        for file in self.get_tree_children():
            file.setCheckState(0, QtCore.Qt.Checked)

    def unselect_all(self):
        for file in self.get_tree_children():
            file.setCheckState(0, QtCore.Qt.Unchecked)

    def browse_folder(self):
        self.current_dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Select a folder",
                                                                      directory=self.default_dir)
        if not self.current_dir:
            return

        self.treeWidget.clear()
        allowed_files = filter(lambda file_name: self.is_allowed_file(file_name), os.listdir(self.current_dir))
        for allowed_file in allowed_files:
            QtWidgets.QTreeWidgetItem(self.treeWidget, [allowed_file]).setCheckState(0, QtCore.Qt.Unchecked)

    def is_allowed_file(self, file_name):
        return not self.file_types or len(list(filter(lambda eof: file_name.endswith(eof), self.file_types))) > 0

    def get_tree_children(self):
        root = self.treeWidget.invisibleRootItem()
        child_count = root.childCount()
        return list(map(lambda i: root.child(i), range(child_count)))

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
        self.logger_output_file_full_path = f"{self.current_dir}/log/{datetime.datetime.now().strftime('%H-%M-%S %Y-%m-%d')}.log "

        with open(self.logger_output_file_full_path, "w") as logger_output_file:
            process = Popen(run_command, stdout=logger_output_file, stderr=logger_output_file, stdin=PIPE,
                            shell=True, cwd=self.current_dir, universal_newlines=True, start_new_session=True)

            self.processes.append({"id": process.pid, "process": process})
            self.run_btn.setEnabled(False)

    def print_logs(self):
        if not self.logger_output_file_full_path:
            return
        logger_output_file = open(self.logger_output_file_full_path, "r")
        log_content = " ".join(logger_output_file.read().split("\n"))
        self.logBrowser.setText("")  # log to screen
        self.logBrowser.setText(log_content)  # log to screen

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
