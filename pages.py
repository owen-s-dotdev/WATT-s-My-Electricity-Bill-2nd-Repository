# pages.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

class BasePage(QWidget):
    def __init__(self, title):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Add title label
        title_label = QLabel(title)
        title_label.setStyleSheet("""
            QLabel {
                font-size: 24px;
                color: #2C3E50;
                margin-bottom: 20px;
            }
        """)
        layout.addWidget(title_label)

class ProfilePage(BasePage):
    def __init__(self):
        super().__init__("Profile")
        # Add profile-specific widgets here

class HistoryPage(BasePage):
    def __init__(self):
        super().__init__("History")
        # Add history-specific widgets here

class SettingsPage(BasePage):
    def __init__(self):
        super().__init__("Settings")
        # Add settings-specific widgets here