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

        # --- ADD OBJECT NAME ---
        self.setObjectName("LoginPage")

        # --- REMOVE INLINE STYLE ---
        # self.setStyleSheet("background-color: white; color: #FF5C00;")

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(20)

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
        
        # --- REMOVE INLINE STYLE ---
        # logo.setStyleSheet("background: transparent;") 

        # Username Label and Input
        username_label = QLabel("Username")
        username_label.setFont(QFont("Arial", 12))
        username_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        # --- REMOVE INLINE STYLE ---
        # username_label.setStyleSheet("color: #FF5C00; background: transparent; font-family: 'Poppins';") 

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username")
        self.username_input.setFixedWidth(300)
        
        # --- REMOVE INLINE STYLE ---
        # self.username_input.setStyleSheet(""" ... """)

        # Buttons
        login_btn = QPushButton("Log in")
        login_btn.setObjectName("orangeButton") # <-- ADD
        # --- REMOVE INLINE STYLE ---
        # login_btn.setStyleSheet(self.orange_button_style())
        login_btn.clicked.connect(self.log_in)

        signup_btn = QPushButton("Sign up")
        signup_btn.setObjectName("orangeButton") # <-- ADD
        # --- REMOVE INLINE STYLE ---
        # signup_btn.setStyleSheet(self.orange_button_style())
        signup_btn.clicked.connect(self.sign_up)

        guest_btn = QPushButton("Continue without logging in")
        guest_btn.setObjectName("guestButton") # <-- ADD
        # --- REMOVE INLINE STYLE ---
        # guest_btn.setStyleSheet(""" ... """)
        guest_btn.clicked.connect(self.continue_as_guest)

        # Layout assembly
        layout.addWidget(logo)
        layout.addWidget(username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(login_btn)
        layout.addWidget(signup_btn)
        layout.addWidget(guest_btn)

        # Fade-in effect
        self.opacity = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.opacity)
        self.opacity.setOpacity(0)
        self.fade_in()

    # --- REMOVE THIS ENTIRE METHOD ---
    # def orange_button_style(self):
    #     return """ ... """

    # Fade animation
    def fade_in(self):
        self.anim = QPropertyAnimation(self.opacity, b"opacity")
        self.anim.setDuration(700)
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.anim.start()

    # Sign up
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
        with open(os.path.join(user_dir, "history.txt"), "w", encoding="utf-8") as f:
            f.write("=== Electricity Bill Calculation History ===\n")

        QMessageBox.information(self, "Success", f"Account created for {username}!")
        self.go_to_main(username)

    # Log in
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

    # Continue as Guest
    def continue_as_guest(self):
        QMessageBox.information(self, "Guest Mode", "Continuing without logging in.")
        self.go_to_main("Guest")

    # Switch to calculator
    def go_to_main(self, username):
        self.current_user = username
        self.fade_out_to_calculator()

    def fade_out_to_calculator(self):
        self.anim = QPropertyAnimation(self.opacity, b"opacity")
        self.anim.setDuration(700)
        self.anim.setStartValue(1)
        self.anim.setEndValue(0)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.anim.finished.connect(self.switch_to_calculator)
        self.anim.start()

    def switch_to_calculator(self):
        calculator_screen = self.stacked_widget.widget(2)
        calculator_screen.current_user = self.current_user
        self.stacked_widget.setCurrentIndex(2)
        if hasattr(calculator_screen, 'fade_in'):
            calculator_screen.fade_in()