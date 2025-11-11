# theme_manager.py

import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QSettings
from styles import LIGHT_STYLESHEET, DARK_STYLESHEET

class ThemeManager:
    def __init__(self):
        # Use QSettings to store the user's theme preference
        self.settings = QSettings("YourAppName", "YourApp")
        self.themes = {
            "light": LIGHT_STYLESHEET,
            "dark": DARK_STYLESHEET
        }
        # Load the saved theme, defaulting to "light"
        self.current_theme = self.settings.value("theme", "light")

    def apply_theme(self, app, theme_name):
        """Applies a specific theme to the QApplication."""
        if theme_name not in self.themes:
            print(f"Theme '{theme_name}' not found. Defaulting to light.")
            theme_name = "light"
            
        self.current_theme = theme_name
        app.setStyleSheet(self.themes[theme_name])
        
        # Save the choice
        self.settings.setValue("theme", theme_name)
        print(f"Theme changed to: {theme_name}")

    def load_and_apply_theme(self, app):
        """Loads the saved theme and applies it."""
        self.apply_theme(app, self.current_theme)

    def set_theme(self, theme_name):
        """Public method to change the theme."""
        app = QApplication.instance()
        if app:
            self.apply_theme(app, theme_name)
        else:
            print("Error: No QApplication instance found.")

# Create a single, global instance of the manager
# This ensures all parts of the app access the same theme state.
theme_manager = ThemeManager()