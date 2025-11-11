# login_page.py

import os
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QGraphicsOpacityEffect
)
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QPixmap, QFont


class LoginPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(25)

        # Logo
        logo = QLabel()
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_dir, "assets", "ECB OOP_logo.png")

        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            print(f"⚠️ Could not load logo image at: {image_path}")

        logo.setPixmap(
            pixmap.scaled(225, 225, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        )

        # Title
        title_label = QLabel("Log In or Sign Up")


        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))

        # Username Input
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter username")
        self.username_input.setFixedWidth(250)
        self.username_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Buttons
        signup_btn = QPushButton("Sign Up")
        signup_btn.setStyleSheet("""
            padding: 10px 20px;
            font-size: 16px;
            background-color: #6A1B9A;
            color: white;
            border-radius: 8px;
        """)
        signup_btn.clicked.connect(self.sign_up)

        login_btn = QPushButton("Log In")
        login_btn.setStyleSheet("""
            padding: 10px 20px;
            font-size: 16px;
            background-color: #6A1B9A;
            color: white;
            border-radius: 8px;
        """)
        login_btn.clicked.connect(self.log_in)

        # Layout
        layout.addWidget(logo)
        layout.addWidget(title_label)
        layout.addWidget(self.username_input)
        layout.addWidget(login_btn)
        layout.addWidget(signup_btn)

        # Fade In Effect
        self.opacity = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.opacity)
        self.opacity.setOpacity(0)
        self.fade_in()

    # Fade In Animation
    def fade_in(self):
        self.anim = QPropertyAnimation(self.opacity, b"opacity")
        self.anim.setDuration(1500)
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.anim.start()

    # Sign Up
    def sign_up(self):
        username = self.username_input.text().strip()
        if not username:
            QMessageBox.warning(self, "Error", "Please enter a username.")
            return

        user_dir = os.path.join(os.getcwd(), "users", username)
        if os.path.exists(user_dir):
            QMessageBox.information(self, "Info", "Username already exists. Please log in.")
            return

        os.makedirs(user_dir, exist_ok=True)
        history_path = os.path.join(user_dir, "history.txt")
        with open(history_path, "w") as f:
            f.write("=== Electricity Bill Calculation History ===\n")

        QMessageBox.information(self, "Success", f"Account created for {username}!")
        self.go_to_main(username)

    # Log In
    def log_in(self):
        username = self.username_input.text().strip()
        if not username:
            QMessageBox.warning(self, "Error", "Please enter a username.")
            return

        user_dir = os.path.join(os.getcwd(), "users", username)
        if not os.path.exists(user_dir):
            QMessageBox.warning(self, "Error", "User not found. Please sign up first.")
            return

        QMessageBox.information(self, "Welcome", f"Welcome back, {username}!")
        self.go_to_main(username)

    # Transition to Calculator with fade-out
    def go_to_main(self, username):
        self.current_user = username
        self.fade_out_to_calculator()

    def fade_out_to_calculator(self):
        self.anim = QPropertyAnimation(self.opacity, b"opacity")
        self.anim.setDuration(500)
        self.anim.setStartValue(1)
        self.anim.setEndValue(0)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.anim.finished.connect(self.switch_to_calculator)
        self.anim.start()

    def switch_to_calculator(self):
        calculator_screen = self.stacked_widget.widget(2)  # index 2 = Calculator
        calculator_screen.current_user = self.current_user
        self.stacked_widget.setCurrentIndex(2)
        if hasattr(calculator_screen, 'fade_in'):
            calculator_screen.fade_in()
