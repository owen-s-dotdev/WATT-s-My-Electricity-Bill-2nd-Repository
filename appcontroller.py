# appcontroller.py

from PyQt6.QtWidgets import (
    QMainWindow, QStackedWidget, QWidget,
    QHBoxLayout, QVBoxLayout, QListWidget, QListWidgetItem,
    QLabel, QAbstractItemView
)
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon
from getstarted import GetStartedScreen
from calculator_app import MainWindow
from pages import ProfilePage, HistoryPage, SettingsPage


class AppController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Electricity Bill App")
        self.resize(QSize(1200, 800))

        # Create main widget and layout
        main_widget = QWidget()
        self.main_widget = main_widget  # Store reference to main widget
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Create navigation sidebar container
        nav_container = QWidget()
        nav_container.setMaximumWidth(250)
        nav_container.setMinimumWidth(250)
        nav_container.setStyleSheet("""
            QWidget {
                background-color: #2C3E50;
                border-right: 2px solid #34495E;
            }
        """)
        nav_layout = QVBoxLayout(nav_container)
        nav_layout.setContentsMargins(0, 0, 0, 0)
        nav_layout.setSpacing(0)

        # Create navigation list
        self.nav_list = QListWidget()
        # single selection and keyboard navigation
        # use QAbstractItemView.SelectionMode.SingleSelection for PyQt6
        self.nav_list.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.nav_list.setStyleSheet("""
            QListWidget {
                background-color: transparent;
                border: none;
                outline: none;
            }
            QListWidget::item {
                color: #ECF0F1;
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
        nav_layout.addWidget(self.nav_list)

        # Add navigation items
        nav_items = ["Profile", "Calculator", "History", "Settings"]
        for item in nav_items:
            list_item = QListWidgetItem(item)
            list_item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            self.nav_list.addItem(list_item)

        # Connect navigation signal
        self.nav_list.currentRowChanged.connect(self.handle_navigation)

        # Create stacked widget for different pages
        self.stack = QStackedWidget()
        self.get_started_screen = GetStartedScreen(self.stack)
        self.profile_screen = ProfilePage()
        self.main_screen = MainWindow()
        self.history_screen = HistoryPage()
        self.settings_screen = SettingsPage()

        self.stack.addWidget(self.get_started_screen)  # index 0
        self.stack.addWidget(self.profile_screen)      # index 1
        self.stack.addWidget(self.main_screen)         # index 2
        self.stack.addWidget(self.history_screen)      # index 3
        self.stack.addWidget(self.settings_screen)     # index 4

        # Add title to navigation
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
        nav_layout.insertWidget(0, nav_title)

        # Store references to containers
        self.nav_container = nav_container
        self.main_layout = main_layout

        # Add widgets to main layout
        main_layout.addWidget(nav_container)
        main_layout.addWidget(self.stack)

        # Set up initial state
        self.nav_container.hide()  # Initially hide navigation
        self.stack.setCurrentIndex(0)  # Show welcome screen first
        # keep stack and nav in sync: when the stack changes, update nav selection
        self.stack.currentChanged.connect(self.on_stack_changed)

        # Set the central widget
        self.setCentralWidget(main_widget)

        # Debug print
        print("Initial setup complete. Nav container exists:", hasattr(self, 'nav_container'))

    def show_navigation(self):
        """Show the navigation sidebar with a fade effect"""
        # Keep simple: show the container and bring to front
        if hasattr(self, 'nav_container'):
            self.nav_container.show()
            self.nav_container.raise_()  # Bring to front

    def on_stack_changed(self, stack_index: int):
        """Keep the side navigation selection in sync with the stacked widget.

        Mapping:
        - stack 0 -> welcome (no selection / hide nav)
        - stack 1 -> Profile (nav index 0)
        - stack 2 -> Calculator (nav index 1)
        - stack 3 -> History (nav index 2)
        - stack 4 -> Settings (nav index 3)
        """
        # Hide nav for welcome screen, show otherwise
        if stack_index == 0:
            if hasattr(self, 'nav_container'):
                self.nav_container.hide()
            # clear selection
            self.nav_list.setCurrentRow(-1)
            return

        # ensure nav is visible
        if hasattr(self, 'nav_container') and not self.nav_container.isVisible():
            self.nav_container.show()

        nav_index = stack_index - 1
        # bounds check
        if nav_index < 0 or nav_index >= self.nav_list.count():
            self.nav_list.setCurrentRow(-1)
            return

        # set current row without re-triggering stack change loop
        try:
            self.nav_list.blockSignals(True)
            self.nav_list.setCurrentRow(nav_index)
        finally:
            self.nav_list.blockSignals(False)

    def handle_navigation(self, index):
        # Map navigation index to stack index (skip welcome screen)
        if index < 0:
            return
        stack_index = index + 1  # Add 1 to skip welcome screen
        self.stack.setCurrentIndex(stack_index)

        # Handle fade in for calculator
        if index == 1:  # Calculator
            if hasattr(self.main_screen, 'fade_in'):
                self.main_screen.fade_in()