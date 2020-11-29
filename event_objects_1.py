import sys
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QLabel, QPushButton

class Communicate(QObject):
    closeApp = pyqtSignal()

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.unitUI()

    def unitUI(self):

        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)
        # grid = QGridLayout()
        # x, y = 0, 0
        # self.text = f'x: {x}, y: {y}'
        # self.label = QLabel(self.text, self)
        # grid.addWidget(self.label, 0, 0, Qt.AlignTop)
        #
        # self.setMouseTracking(True)
        #
        # self.setLayout(grid)

        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle('Review')
        self.show()

    # def mouseMoveEvent(self, e):
    #     x, y = e.x(), e.y()
    #     text = f'x: {x}, y: {y}'
    #     self.label.setText(text)


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(f'{sender.text()} was pressed')

    def mousePressEvent(self, e):
        self.c.closeApp.emit()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    print(vars(ex))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
