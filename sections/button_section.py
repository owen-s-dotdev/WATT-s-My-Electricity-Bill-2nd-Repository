# sections/button_section.py
from PyQt6.QtWidgets import QGroupBox, QHBoxLayout, QPushButton

class ButtonSection(QGroupBox):
    def __init__(self, actions: dict):
        super().__init__("Actions")
        self.setStyleSheet(self.groupbox_style())
        layout = QHBoxLayout()
        self.setLayout(layout)
        self.buttons = {}

        for name, callback in actions.items():
            btn = QPushButton(name)
            btn.clicked.connect(callback)
            btn.setStyleSheet(self.button_style())
            layout.addWidget(btn)
            self.buttons[name] = btn

    @staticmethod
    def groupbox_style():
        return """
            QGroupBox {
                background-color: #ffffff;
                color: #333333;
                font-weight: bold;
                border: 2px solid #cc6600;
                border-radius: 8px;
                margin-top: 10px;
            }
            QGroupBox:title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 0 3px;
            }
        """

    @staticmethod
    def button_style():
        return """
            QPushButton {
                background-color: #ffffff;
                color: #333333;
                border: 2px solid #cc6600;
                border-radius: 6px;
                padding: 6px 12px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #f0f0f0; }
            QPushButton:pressed { background-color: #e0e0e0; }
        """
