#appcontroller.py

from PyQt6.QtWidgets import QMainWindow, QStackedWidget
from PyQt6.QtCore import QSize
from getstarted import GetStartedScreen
from calculator_app import MainWindow

class AppController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Electricity Bill App")
        self.resize(QSize(1000, 800))

        self.stack = QStackedWidget()
        self.get_started_screen = GetStartedScreen(self.stack)
        self.main_screen = MainWindow()

        self.stack.addWidget(self.get_started_screen)  # index 0
        self.stack.addWidget(self.main_screen)         # index 1

        self.setCentralWidget(self.stack)