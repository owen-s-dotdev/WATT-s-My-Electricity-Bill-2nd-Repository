# app controller

from PyQt6.QtWidgets import (
    QMainWindow, QStackedWidget, QWidget,
    QHBoxLayout, QVBoxLayout, QListWidget, QListWidgetItem,
    QLabel, QAbstractItemView
)
from PyQt6.QtCore import QSize, Qt
from getstarted import GetStartedScreen
from login_page import LoginPage
from calculator_app import MainWindow
from pages import ProfilePage, HistoryPage, SettingsPage


class AppController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Electricity Bill App")
        self.resize(QSize(1200, 800))

        # Create main widget and layout
        main_widget = QWidget()
        self.main_widget = main_widget
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Create navigation sidebar
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
                color: #ECF0F1;
                padding: 14px 18px;
                border-bottom: 1px solid #34495E;
                font-size: 14px;
            }
            QListWidget::item:selected {
                background-color: #34495E;
                color: #FFFFFF;
                border-left: 6px solid #3498DB;
                padding-left: 12px;
            }
            QListWidget::item:hover {
                background-color: #375a7f;
            }
        """)
        nav_layout.addWidget(self.nav_list)

        # Navigation items
        nav_items = ["Profile", "Calculator", "History", "Settings"]
        for item in nav_items:
            list_item = QListWidgetItem(item)
            list_item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            self.nav_list.addItem(list_item)

        # Connect navigation selection
        self.nav_list.currentRowChanged.connect(self.handle_navigation)

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
        nav_layout.insertWidget(0, nav_title)

        # Create stacked widget
        self.stack = QStackedWidget()

        # Screens
        self.get_started_screen = GetStartedScreen(self.stack)  # index 0
        self.login_screen = LoginPage(self.stack)               # index 1
        self.profile_screen = ProfilePage()                     # index 2
        self.main_screen = MainWindow()                         # index 3 (Calculator)
        self.history_screen = HistoryPage()                     # index 4
        self.settings_screen = SettingsPage()                   # index 5

        # Add screens to stack
        self.stack.addWidget(self.get_started_screen)  # 0
        self.stack.addWidget(self.login_screen)        # 1
        self.stack.addWidget(self.profile_screen)      # 2
        self.stack.addWidget(self.main_screen)         # 3
        self.stack.addWidget(self.history_screen)      # 4
        self.stack.addWidget(self.settings_screen)     # 5

        # Store containers
        self.nav_container = nav_container
        self.main_layout = main_layout

        # Layout: sidebar + stacked widget
        main_layout.addWidget(nav_container)
        main_layout.addWidget(self.stack)

        # Initial state
        self.nav_container.hide()          # hide nav until after login
        self.stack.setCurrentIndex(0)      # show Get Started first
        self.stack.currentChanged.connect(self.on_stack_changed)

        # Set central widget
        self.setCentralWidget(main_widget)

        # Debug
        print("AppController initialized. Nav container exists:", hasattr(self, 'nav_container'))

    def show_navigation(self):
        """Show navigation sidebar"""
        if hasattr(self, 'nav_container'):
            self.nav_container.show()
            self.nav_container.raise_()

    def on_stack_changed(self, stack_index: int):
        """Sync nav with stacked widget"""
        # Hide nav for Get Started & Login screens
        if stack_index in [0, 1]:
            if hasattr(self, 'nav_container'):
                self.nav_container.hide()
            self.nav_list.setCurrentRow(-1)
            return

        # Show nav
        if hasattr(self, 'nav_container') and not self.nav_container.isVisible():
            self.nav_container.show()

        # Map stack index -> nav index (subtract 2)
        nav_index = stack_index - 2
        if 0 <= nav_index < self.nav_list.count():
            try:
                self.nav_list.blockSignals(True)
                self.nav_list.setCurrentRow(nav_index)
            finally:
                self.nav_list.blockSignals(False)

    def handle_navigation(self, index):
        """Change stacked widget when nav item clicked"""
        if index < 0:
            return
        # Map nav index -> stack index (add 2 to skip Get Started + Login)
        stack_index = index + 2
        self.stack.setCurrentIndex(stack_index)

        # Fade in Calculator if selected
        if index == 1 and hasattr(self.main_screen, 'fade_in'):
            self.main_screen.fade_in()
