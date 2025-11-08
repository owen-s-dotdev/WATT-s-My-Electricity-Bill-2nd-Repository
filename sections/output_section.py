# sections/output_section.py
from PyQt6.QtWidgets import QGroupBox, QGridLayout, QLabel

class OutputSection(QGroupBox):
    def __init__(self):
        super().__init__("Estimated Cost")
        self.setStyleSheet(self.groupbox_style())
        layout = QGridLayout()
        self.setLayout(layout)
        self.daily_label = QLabel("Daily Cost: ₱0.00")
        self.monthly_label = QLabel("Monthly Estimate: ₱0.00")
        layout.addWidget(self.daily_label, 0, 0)
        layout.addWidget(self.monthly_label, 1, 0)

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
