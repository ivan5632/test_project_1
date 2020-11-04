import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.unitUI()

    def unitUI(self):

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.move(100, 200)
        self.setWindowTitle('Review')
        self.show()




def main():
    app = QApplication(sys.argv)
    ex = Example()
    print(vars(ex))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
