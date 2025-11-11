# pages.py

import os
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTextEdit, QCheckBox, QComboBox, QPushButton, QMessageBox, QGraphicsOpacityEffect
)
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve


class BasePage(QWidget):
    def __init__(self, title):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self.title_label = QLabel(title)
        self.title_label.setStyleSheet("""
            QLabel {
                font-size: 24px;
                color: #FF5C00;
                margin: 20px 0;
                font-family: 'Poppins';
            }
        """)
        self.layout.addWidget(self.title_label)


# Profile Page
class ProfilePage(BasePage):
    def __init__(self):
        super().__init__("Profile")
        # Add profile-specific widgets here


# History Page
class HistoryPage(BasePage):
    def __init__(self):
        super().__init__("History")

        self.opacity = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.opacity)
        self.opacity.setOpacity(1)

        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        self.text_area.setStyleSheet("""
            QTextEdit {
                background-color: #FFF3E0;
                border: 1px solid #FFB97D;
                border-radius: 10px;
                padding: 12px;
                font-family: 'Poppins';
                font-size: 14px;
                color: #2C3E50;
            }
        """)
        self.layout.addWidget(self.text_area)

    def load_history(self, username):
        """Load user's history file"""
        if username == "Guest":
            self.text_area.setText("Guest mode active.\nNo saved history available.")
            return

        history_path = os.path.join(os.getcwd(), "users", username, "history.txt")
        if os.path.exists(history_path):
            with open(history_path, "r", encoding="utf-8") as file:
                self.text_area.setText(file.read())
        else:
            self.text_area.setText("No history found for this user.")

        self.fade_in()

    def fade_in(self):
        """Smooth fade-in animation"""
        self.opacity.setOpacity(0)
        self.anim = QPropertyAnimation(self.opacity, b"opacity")
        self.anim.setDuration(700)
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.anim.start()

# Settings Page
class SettingsPage(BasePage):
    def __init__(self, app_controller=None):
        super().__init__("Settings")
        # Add settings-specific widgets here
