import subprocess
import sys
import os
from builtins import super

from PyQt5 import QtWidgets, QtCore
import pygui


class ExampleApp(QtWidgets.QMainWindow, pygui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.treeWidget.setHeaderLabels(['Files'])
        self.treeWidget.setAlternatingRowColors(True)

        self.current_dir = ""
        self.select_folder_btn.clicked.connect(self.browse_folder)
        self.start_btn.clicked.connect(self.run_tests)
        self.stop_btn.clicked.connect(self.stop_all_tests)
        self.clear_btn.clicked.connect(self.clear)

    def browse_folder(self):
        self.current_dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Select a folder")
        if self.current_dir:
            self.treeWidget.clear()
            for file_name in os.listdir(self.current_dir):  # для каждого файла в директории
                item = QtWidgets.QTreeWidgetItem(self.treeWidget, [file_name])
                item.setCheckState(0, QtCore.Qt.Unchecked)
                print(item.checkState(0))
                # if item.checkState(0) == QtCore.Qt.Checked:
                #     print(file_name)
                # else:
                #     print("els")
    def run_tests(self):
        subprocess.call('start', shell=True, cwd=self.current_dir)
        if self.current_dir:
            for file_name in os.listdir(self.current_dir):
                subprocess.call(f"node {file_name}", shell=True, cwd=self.current_dir)

    def stop_all_tests(self):
        print("All tests stopped")

    def clear(self):
        self.treeWidget.clear()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
