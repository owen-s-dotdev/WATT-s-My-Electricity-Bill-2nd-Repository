#main_driver.py
#comment
#comment again

import sys
from PyQt6.QtWidgets import QApplication
from appcontroller import AppController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppController()
    window.show()
    sys.exit(app.exec())
