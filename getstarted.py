# get started

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGraphicsOpacityEffect
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QPixmap

class GetStartedScreen(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(25)

        # Logo
        logo = QLabel()
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap("C:/Users/JAMES/PYTHON FILES/PROJECT OOP/assets/ECB OOP.png")
        if pixmap.isNull():
            print("⚠️ Could not load logo image. Check path.")
        logo.setPixmap(
            pixmap.scaled(225, 225, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        )

        # Welcome text
        welcome_label = QLabel("Welcome to Watt's my Electricity Bill?")
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_label.setStyleSheet("font-size: 24px; color: #2C3E50; margin-bottom: 20px;")

        # Get Started button
        start_button = QPushButton("Get Started")
        start_button.setStyleSheet("""
            QPushButton {
                padding: 10px 20px;
                font-size: 16px;
                background-color: #6A1B9A;
                color: white;
                border-radius: 8px;
                min-width: 150px;
            }
            QPushButton:hover {
                background-color: #8E24AA;
            }
        """)
        start_button.clicked.connect(self.start_transition)

        # Layout
        layout.addWidget(logo)
        layout.addWidget(welcome_label)
        layout.addWidget(start_button)

        # Fade effect
        self.opacity = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.opacity)
        self.opacity.setOpacity(0)
        self.fade_in()

    # Fade in animation
    def fade_in(self):
        self.anim = QPropertyAnimation(self.opacity, b"opacity")
        self.anim.setDuration(1500)
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.anim.start()

    # Fade out animation
    def start_transition(self):
        self.fade_out()

    def fade_out(self):
        self.anim = QPropertyAnimation(self.opacity, b"opacity")
        self.anim.setDuration(1000)
        self.anim.setStartValue(1)
        self.anim.setEndValue(0)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.anim.finished.connect(self.go_to_login)
        self.anim.start()

    def go_to_login(self):
        """Switch to the login page"""
        self.stacked_widget.setCurrentIndex(1)  # Login page at index 1
        login_screen = self.stacked_widget.widget(1)
        if hasattr(login_screen, 'fade_in'):
            login_screen.fade_in()
