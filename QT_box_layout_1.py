import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.unitUI()

    def unitUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']
        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            if name:
                button_name = f'button_{name}'
                setattr(self, button_name, QPushButton(name))
                # button = QPushButton(name)
                grid.addWidget(getattr(self, button_name), *position)

        self.move(100, 200)
        self.setWindowTitle('Buttons')
        self.show()




def main():
    app = QApplication(sys.argv)
    ex = Example()
    print(vars(ex))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
