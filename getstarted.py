#getstarted.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGraphicsOpacityEffect
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
        welcome_label.setStyleSheet("font-size: 24px; color: #2C3E50; margin-bottom: 20px;")

        # Button
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
    def start_transition(self):
        """Initiate the transition from welcome screen to main app"""
        self.fade_out()

    def fade_out(self):
        """Fade out animation for the welcome screen"""
        self.anim = QPropertyAnimation(self.opacity, b"opacity")
        self.anim.setDuration(1000)
        self.anim.setStartValue(1)
        self.anim.setEndValue(0)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.anim.finished.connect(self.go_to_main)
        self.anim.start()

    def go_to_main(self):
        """Transition to the main calculator screen"""
        # Get the main window (AppController)
        parent_window = self.stacked_widget.window()
        
        # Show the navigation sidebar first
        if hasattr(parent_window, 'show_navigation'):
            parent_window.show_navigation()
            
        # Set Calculator tab as active and switch to calculator screen
        if hasattr(parent_window, 'nav_list'):
            parent_window.nav_list.setCurrentRow(1)  # Select Calculator
            
        # Switch to calculator screen
        self.stacked_widget.setCurrentIndex(2)  # Index 2 is calculator
        calculator_screen = self.stacked_widget.widget(2)
        if hasattr(calculator_screen, 'fade_in'):
            calculator_screen.fade_in()
            
        # Debug print to verify navigation
        print("Navigation shown:", parent_window.nav_container.isVisible() if hasattr(parent_window, 'nav_container') else "No nav_container")
