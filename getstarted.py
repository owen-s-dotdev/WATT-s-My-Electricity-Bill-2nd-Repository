#getstarted.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QPixmap, QFont

class GetStartedScreen(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(25)

        # ADDED LOGO
        logo = QLabel()
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap("C:/Users/JAMES/PYTHON FILES/PROJECT OOP/assets/ECB OOP.png")
        if pixmap.isNull():
            print("⚠️ Could not load logo image. Check path.")
        logo.setPixmap(
            pixmap.scaled(225, 225, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        )

        # Welcome
        welcome_label = QLabel("Welcome to Watt's my Electricity Bill?")
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        start_button = QPushButton("Get Started")
        start_button.clicked.connect(self.go_to_main)

        # Button
        start_button = QPushButton("Get Started")
        start_button.setStyleSheet("padding: 10px 20px; font-size: 16px; background-color: #6A1B9A; color: white; border-radius: 8px;")
        start_button.clicked.connect(self.go_to_main)

        # Layout
        layout.addWidget(logo)
        layout.addWidget(welcome_label)
        layout.addWidget(start_button)

        # ADDED FADE IN EFFECT
        self.opacity = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.opacity)
        self.opacity.setOpacity(0)
        self.fade_in()

        # ADDED FADE IN ANIMATION
    def fade_in(self):
        self.anim = QPropertyAnimation(self.opacity, b"opacity")
        self.anim.setDuration(1500)
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.anim.start()

        # ADDED FADE OUT ANIMATION
    def fade_out(self):
        self.anim = QPropertyAnimation(self.opacity, b"opacity")
        self.anim.setDuration(1500)
        self.anim.setStartValue(1)
        self.anim.setEndValue(0)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.anim.finished.connect(self.go_to_main)
        self.anim.start()

    def go_to_main(self):
        self.stacked_widget.setCurrentIndex(1)

        # ADDED FADE IN TO CALC
        calculator_screen = self.stacked_widget.widget(1)
        calculator_screen.fade_in()
