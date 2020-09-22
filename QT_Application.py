import sys
import typing

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Application Title")
        label = QLabel("Label text")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

# class Rectangle:
#     def __init__(self, x_size, y_size):
#         self.x_size = x_size
#         self.y_size = y_size
#
#     def area(self):
#         return self.x_size * self.y_size


# class Square(Rectangle):
#     def __init__(self, x_size):
#         super().__init__(x_size, x_size)
#
#
# r = Rectangle(3, 5)
# print(r.area())
# print('------------------------------')
# s = Square(6)
# print(s.area())

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
