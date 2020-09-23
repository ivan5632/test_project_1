import sys
import typing

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # SIGNAL: The connected function will be called whenever the window
        # title is changed. The new title will be passed to the function.
        self.windowTitleChanged.connect(self.onWindowTitleChange)

        # SIGNAL: The connected function will be called whenever the window
        # title is changed. The new title is discarded in the lambda and the
        # function is called without parameters.
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn('tttt',x))

        # SIGNAL: The connected function will be called whenever the window
        # title is changed. The new title is passed to the function
        # and replaces the default parameter
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x))

        # SIGNAL: The connected function will be called whenever the window
        # title is changed. The new title is passed to the function
        # and replaces the default parameter. Extra data is passed from
        # within the lambda.
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x, 25))

        self.setWindowTitle("Application Title 114")

        label = QLabel("Label text")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

    def onWindowTitleChange(self, s):
        print(s)

    # SLOT: This has default parameters and can be called without a value
    def my_custom_fn(self, a="HELLLO!", b=5):
        print(a, b)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
