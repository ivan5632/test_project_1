import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLCDNumber, QSlider

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.unitUI()

    def unitUI(self):

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)


        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle('Review')
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()



def main():
    app = QApplication(sys.argv)
    ex = Example()
    print(vars(ex))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
