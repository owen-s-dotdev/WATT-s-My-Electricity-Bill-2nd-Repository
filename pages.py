# pages.py
import os
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTextEdit, QCheckBox,  
    QComboBox, QPushButton, QMessageBox, QGraphicsOpacityEffect
)
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve


class BasePage(QWidget):
    def __init__(self, title):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self.title_label = QLabel(title)
        
        self.title_label.setObjectName("pageTitle")
        
        self.layout.addWidget(self.title_label)


# History Page
class HistoryPage(BasePage):
    def __init__(self):
        super().__init__("History")
        
        # --- ADD OBJECT NAME ---
        self.setObjectName("HistoryPage")

        self.opacity = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.opacity)
        self.opacity.setOpacity(1)

        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        
        # --- REMOVE INLINE STYLE ---
        # self.text_area.setStyleSheet(""" ... """)
        
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
    def __init__(self, theme_manager): # <-- ACCEPT THEME MANAGER
        super().__init__("Settings")
        self.theme_manager = theme_manager # <-- STORE IT
        
        # Dark Mode Toggle
        self.theme_toggle_cb = QCheckBox("Enable Dark Mode")
        
        self.theme_toggle_cb.setStyleSheet("font-size: 16px; margin-top: 10px;") 
        
        # Set its initial state based on the current theme (Exiting when in dark mode will load it in dark mode next time)
        self.theme_toggle_cb.setChecked(self.theme_manager.current_theme == "dark")
        
        # Connect the toggle signal to a handler function
        self.theme_toggle_cb.toggled.connect(self.handle_theme_change)
        
        self.layout.addWidget(self.theme_toggle_cb)

    def handle_theme_change(self, is_checked):
        """Called when the checkbox is toggled."""
        if is_checked:
            self.theme_manager.set_theme("dark")
        else:
            self.theme_manager.set_theme("light")