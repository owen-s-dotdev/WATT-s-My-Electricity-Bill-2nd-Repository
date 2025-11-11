# navigation_panel.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QLabel, QAbstractItemView
)
from PyQt6.QtCore import Qt


class NavigationPanel(QWidget):
    def __init__(self, on_navigation_changed):
        super().__init__()
        self.setMaximumWidth(250)
        self.setMinimumWidth(250)
        # Sidebar background and right border (orange strip)
        self.setStyleSheet("""
            QWidget {
                background-color: #FFFFFF;
                border-right: 20px solid #FF4B2B;
            }
        """)

        # Main layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 20, 0, 20)
        layout.setSpacing(20)

        # Optional "Menu" label at top (you can remove if not needed)
        nav_title = QLabel("Menu")
        nav_title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        nav_title.setStyleSheet("""
            QLabel {
                color: #FF3C00;
                font-family: 'Poppins';
                font-size: 20px;
                font-weight: bold;
                padding-left: 16px;
            }
        """)
        layout.addWidget(nav_title)

        # Navigation list
        self.nav_list = QListWidget()
        self.nav_list.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.nav_list.setStyleSheet("""
            QListWidget {
                background-color: transparent;
                border: none;
                outline: none;
            }
            QListWidget::item {
                color: #FF3C00;
                padding: 18px 16px;
                font-family: 'Poppins';
                font-size: 20px;
                font-weight: bold;
            }
            QListWidget::item:selected {
                background-color: #FFC04C;
                color: #FF3C00;
                font-weight: 700;
            }
            QListWidget::item:hover {
                background-color: #FFD580;
            }
        """)
        layout.addWidget(self.nav_list)

        # Add navigation items (same as your other pages)
        nav_items = ["Profile", "Calculate", "History", "Settings"]
        for item in nav_items:
            list_item = QListWidgetItem(item)
            list_item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            self.nav_list.addItem(list_item)

        # Connect navigation change callback
        self.nav_list.currentRowChanged.connect(on_navigation_changed)
