# main_driver.py
import sys
from PyQt6.QtWidgets import QApplication
from appcontroller import AppController
from theme_manager import theme_manager  # <-- IMPORT THE MANAGER

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # --- ADD THIS ---
    # Load and apply the saved theme BEFORE showing any windows
    theme_manager.load_and_apply_theme(app)
    # --- END ADD ---

    window = AppController(theme_manager) # <-- PASS IT
    window.show()
    sys.exit(app.exec())