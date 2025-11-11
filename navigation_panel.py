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
        self.setStyleSheet("""
            QWidget {
                background-color: #2C3E50;
                border-right: 2px solid #34495E;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Navigation title
        nav_title = QLabel("Menu")
        nav_title.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 18px;
                padding: 14px;
                background-color: #1a2634;
                border-bottom: 2px solid #34495E;
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
                color: #34495E;
                padding: 14px 18px;
                border-bottom: 1px solid #34495E;
                font-size: 14px;
            }
            QListWidget::item:selected {
                background-color: #34495E;
                color: #FFFFFF;
                border-left: 6px solid #3498DB;
                padding-left: 12px; /* account for left border */
            }
            QListWidget::item:hover {
                background-color: #375a7f;
            }
        """)
        layout.addWidget(self.nav_list)

        # Add navigation items
        nav_items = ["Profile", "Calculator", "History", "Settings"]
        for item in nav_items:
            list_item = QListWidgetItem(item)
            list_item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            self.nav_list.addItem(list_item)

        # Connect navigation callback
        self.nav_list.currentRowChanged.connect(on_navigation_changed)
