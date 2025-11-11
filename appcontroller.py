# appcontroller.py
from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QWidget, QHBoxLayout, QApplication
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import QSize
from getstarted import GetStartedScreen
from login_page import LoginPage
from calculator_app import MainWindow
from pages import HistoryPage, SettingsPage 
from navigation_panel import NavigationPanel  # imported modular nav


class AppController(QMainWindow):
    def __init__(self, theme_manager): 
        super().__init__()
        self.theme_manager = theme_manager 
        self.setWindowTitle("Electricity Bill App")
        self.resize(QSize(1200, 800))

        # Main layout setup
        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Navigation panel (modularized)
        self.nav_container = NavigationPanel(self.handle_navigation)

        # Stacked widget (pages)
        self.stack = QStackedWidget()
        self.get_started_screen = GetStartedScreen(self.stack)
        self.login_screen = LoginPage(self.stack)
        self.main_screen = MainWindow()
        self.history_screen = HistoryPage()
        
        self.settings_screen = SettingsPage(theme_manager) 

        # Add pages to stack
        self.stack.addWidget(self.get_started_screen)
        self.stack.addWidget(self.login_screen)
        self.stack.addWidget(self.main_screen)
        self.stack.addWidget(self.history_screen)
        self.stack.addWidget(self.settings_screen)

        # Add to main layout
        main_layout.addWidget(self.nav_container)
        main_layout.addWidget(self.stack)

        # Hide nav initially
        self.nav_container.hide()
        self.stack.setCurrentIndex(0)
        self.stack.currentChanged.connect(self.on_stack_changed)

        self.setCentralWidget(main_widget)

    def show_navigation(self):
        if hasattr(self, 'nav_container'):
            self.nav_container.show()
            self.nav_container.raise_()

    def on_stack_changed(self, stack_index: int):
        if stack_index in [0, 1]:
            self.nav_container.hide()
            self.nav_container.nav_list.setCurrentRow(-1)
            return

        if not self.nav_container.isVisible():
            self.nav_container.show()
        
        nav_index = stack_index - 2
        if 0 <= nav_index < self.nav_container.nav_list.count():
            try:
                self.nav_container.nav_list.blockSignals(True)
                self.nav_container.nav_list.setCurrentRow(nav_index)
            finally:
                self.nav_container.nav_list.blockSignals(False)

    def handle_navigation(self, index):
        if index < 0:
            return
        stack_index = index + 2
        self.stack.setCurrentIndex(stack_index)

        # If user clicks "History", load their file
        
        if index == 1:  
            current_user = getattr(self.login_screen, "current_user", "Guest")
            self.history_screen.load_history(current_user)

        # Fade in main screen when navigated to it
        if index == 0 and hasattr(self.main_screen, 'fade_in'): # Calculate is now 1st item (index 0)
            self.main_screen.fade_in()