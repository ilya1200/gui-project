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
        self.start_btn.clicked.connect(self.run_checked_tests)
        self.stop_btn.clicked.connect(self.stop_all_tests)
        self.clear_btn.clicked.connect(self.clear)

    def browse_folder(self):
        self.current_dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Select a folder")
        if self.current_dir:
            self.treeWidget.clear()
            for file_name in os.listdir(self.current_dir):  # для каждого файла в директории
                # if file_name ends with '.js': FILTERING
                item = QtWidgets.QTreeWidgetItem(self.treeWidget, [file_name])
                item.setCheckState(0, QtCore.Qt.Unchecked)

    def find_checked(self):
        checked_items = list()
        root = self.treeWidget.invisibleRootItem()
        child_count = root.childCount()

        for i in range(child_count):
            i_child = root.child(i)
            if i_child.checkState(0) == QtCore.Qt.Checked:
                checked_items.append(i_child.text(0))
        return checked_items

    def run_checked_tests(self):
        checked_files = self.find_checked()
        subprocess.call('start', shell=True, cwd=self.current_dir)
        for file_name in checked_files:
            print(f"Run file: {file_name}")
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
