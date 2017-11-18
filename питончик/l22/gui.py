import sys
from PyQt5.QtWidgets import QApplication, QWidget

class OurWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Лукамана первое приложение")
        self.setGeometry(8, 30, 800, 600)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OurWindow()
    sys.exit(app.exec_())

