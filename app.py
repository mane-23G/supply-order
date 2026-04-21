import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow

#Subclass QMainWindow to customize your apps main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        buton = QPushButton("Press Me!")

        self.setFixedSize(QSize(400,300))

        #Set the central widget of the window
        self.setCentralWidget(buton)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

