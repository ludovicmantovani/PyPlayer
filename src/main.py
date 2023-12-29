import sys

from PySide2.QtWidgets import QApplication
from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.resize(550, 600)
    window.show()
    exit_code = app.exec_()
    sys.exit(exit_code)