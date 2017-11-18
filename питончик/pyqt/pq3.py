import sys
from PyQt5.QtWidgets import QApplication, QToolTip, QMessageBox, QDesktopWidget, QMainWindow, QAction, qApp, QTextEdit, QLabel
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)
        QToolTip.setFont(QFont('SansSerif', 12))

        self.setToolTip('<b>Здесь нет виджетов</b>')


        exitAction = QAction(QIcon('exit.png'), 'ВЫХОД!!!!!', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Файл')
        fileMenu.addAction(exitAction)

        lbl1 = QLabel('Zetcode', self)
        lbl1.move(300, 50)

        lbl2 = QLabel('tutorials', self)
        lbl2.move(330, 80)

        lbl3 = QLabel('for programmers', self)
        lbl3.move(350, 110)

        self.resize(500, 300)
        self.center()
        self.setWindowTitle('PyQt5')
        self.show()


    # def closeEvent(self, event):

    #     reply = QMessageBox.question(self, 'Внимание, ВОПРОС!!!',
    #         "Ты уверен что хочешь свалить отсюда?", QMessageBox.Yes |
    #         QMessageBox.No, QMessageBox.No)

    #     if reply == QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()


    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())