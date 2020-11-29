import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog
from PyQt5.QtGui import QIcon
from pathlib import Path

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('bug.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open New File')
        openFile.triggered.connect(self.showDialog)

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('File Dialog')
        self.show()

    def showDialog(self):
        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'Open File', home_dir)
        if fname[0]:
            print(fname)
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)



def main():
    app = QApplication(sys.argv)
    ex = Example()
    print(vars(ex))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
