# main_driver.py
import sys
from PyQt6.QtWidgets import QApplication
from appcontroller import AppController
from theme_manager import theme_manager  # Theme manager is applied before any windows show

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Load and apply the saved theme BEFORE showing any windows
    theme_manager.load_and_apply_theme(app)
  
    window = AppController(theme_manager) # Create main app controller window and pass theme manager
    window.show()
    sys.exit(app.exec())