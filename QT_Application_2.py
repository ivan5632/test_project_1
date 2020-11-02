import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QToolTip, QPushButton, QMessageBox, QDesktopWidget, QMenu, QTextEdit
from PyQt5.QtGui import QIcon, QFont


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.unitUI()

    def unitUI(self):

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAct = QAction(QIcon('bug.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application...')
        exitAct.triggered.connect(qApp.quit)

        self.addToolBar("Exit").addAction(exitAct)

        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready...')

        menubar = self.menuBar()

        fileMenu = menubar.addMenu('&File')

        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impAct.setStatusTip('Import mail...')
        impMenu.addAction(impAct)

        newAct = QAction('New action', self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        fileMenu.addAction(exitAct)

        viewMenu = menubar.addMenu('&View')
        viewStatAct = QAction('View Statusbar', self)
        viewStatAct.setStatusTip('View Statusbar...')
        viewStatAct.setCheckable(True)
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)
        viewMenu.addAction(viewStatAct)



        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b><i>QPushButton</i></b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(150, 150)


        self.setGeometry(200, 200, 600, 600)
        self.center()
        self.setWindowTitle('Tooltips')
        self.setWindowIcon(QIcon('bug.png'))

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Confirm Quit Message', 'Are you sure?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def toggleMenu(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        openAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
