#getstarted.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt

class GetStartedScreen(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        layout = QVBoxLayout(self)

        welcome_label = QLabel("Welcome to Watt's my Electricity Bill?")
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        start_button = QPushButton("Get Started")
        start_button.clicked.connect(self.go_to_main)

        layout.addWidget(welcome_label)
        layout.addWidget(start_button)

    def go_to_main(self):
        self.stacked_widget.setCurrentIndex(1)