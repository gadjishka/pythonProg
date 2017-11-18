import sys, random

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class OurWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Приложение")
        self.setGeometry(50, 50, 800, 600)
        self.show()
        
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = OurWindow()
	sys.exit(app.exec_())