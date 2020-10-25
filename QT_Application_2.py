import sys
from PyQt5.QtWidgets import QApplication, QWidget


def main():
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(450, 450)
    w.move(600, 600)
    w.setWindowTitle('Simple window')
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
