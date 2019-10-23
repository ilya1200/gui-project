import subprocess
import sys
import os
from builtins import super

from PyQt5 import QtWidgets
import pygui


class ExampleApp(QtWidgets.QMainWindow, pygui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.select_folder_btn.clicked.connect(self.browse_folder)
        self.start_btn.clicked.connect(self.run_tests)
        self.stop_btn.clicked.connect(self.stop_all_tests)
        self.clear_btn.clicked.connect(self.clear)

    def browse_folder(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Select a folder")
        if directory:
            self.listWidget.clear()
            for file_name in os.listdir(directory):  # для каждого файла в директории
                self.listWidget.addItem(file_name)

    def run_tests(self):
        subprocess.call('start', shell=True)
        # directory = QtWidgets.QFileDialog.fileSelected(self, 'listWidget')
        # if directory:
        #     for file_name in directory:
        #         subprocess.call(directory, shell=True)

    def stop_all_tests(self):
        print("All tests stopped")

    def clear(self):
        self.listWidget.clear()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()