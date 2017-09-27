import sys
import win32con
import win32gui
import win32api

from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PyQt5 import uic, QtCore


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('mainwindow.ui', self)

app = QApplication(sys.argv)
window = MyWindow()
window.show()

# Back up the reference to the exceptionhook
sys._excepthook = sys.excepthook

def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)

# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook

try:
    sys.exit(app.exec_())
except:
    print("Exiting")

