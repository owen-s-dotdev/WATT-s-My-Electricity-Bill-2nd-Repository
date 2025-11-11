# navigation_panel.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QLabel, QAbstractItemView
)
from PyQt6.QtCore import Qt


class NavigationPanel(QWidget):
    def __init__(self, on_navigation_changed):
        super().__init__()
        
        # --- ADD OBJECT NAME ---
        self.setObjectName("NavigationPanel")
        
        self.setMaximumWidth(250)
        self.setMinimumWidth(250)
        
        # --- REMOVE INLINE STYLE ---
        # self.setStyleSheet(""" ... """)

        # Main layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 20, 0, 20)
        layout.setSpacing(20)

        # Optional "Menu" label at top (you can remove if not needed)
        nav_title = QLabel("Menu")
        nav_title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        # --- REMOVE INLINE STYLE ---
        # nav_title.setStyleSheet(""" ... """)
        
        layout.addWidget(nav_title)

        # Navigation list
        self.nav_list = QListWidget()
        self.nav_list.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        
        # --- REMOVE INLINE STYLE ---
        # self.nav_list.setStyleSheet(""" ... """)
        
        layout.addWidget(self.nav_list)

        # Add navigation items (same as your other pages)
        nav_items = ["Calculate", "History", "Settings"] # <-- REMOVED "Profile"
        for item in nav_items:
            list_item = QListWidgetItem(item)
            list_item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            self.nav_list.addItem(list_item)

        # Connect navigation change callback
        self.nav_list.currentRowChanged.connect(on_navigation_changed)