import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton


class Form1(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Hello")
        self.setFixedSize(350, 180)

        self.labelName: QLabel = QLabel("Your Name", self)
        self.labelName.setGeometry(20, 30, 70, 20)

        self.entryName: QLineEdit = QLineEdit(self)
        self.entryName.setGeometry(100, 30, 180, 22)

        self.labelResult: QLabel = QLabel("Hello Text", self)
        self.labelResult.setGeometry(20, 70, 70, 20)

        self.entryResult: QLineEdit = QLineEdit(self)
        self.entryResult.setReadOnly(True)
        self.entryResult.setGeometry(100, 70, 180, 22)

        self.button: QPushButton = QPushButton("OK", self)
        self.button.setGeometry(110, 110, 80, 25)
        self.button.clicked.connect(self.button_click)

    def button_click(self):
        name = self.entryName.text()

        if name == "":
            self.entryResult.setText("Hello World!")
        else:
            self.entryResult.setText("Hello " + name + "!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form1()
    form.show()
    sys.exit(app.exec_())
