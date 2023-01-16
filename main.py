from library.main.python.gui import main_window as mw
from PyQt5.QtWidgets import QApplication
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = mw.MainWindow()
    sys.exit(app.exec_())