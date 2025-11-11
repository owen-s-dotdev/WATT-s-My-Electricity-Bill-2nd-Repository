# getstarted.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGraphicsOpacityEffect, QProgressBar, QSizePolicy, QSpacerItem
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QTimer
from PyQt6.QtGui import QPixmap

class GetStartedScreen(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(15)
        layout.setContentsMargins(0, 0, 0, 0)  # ensure dynamic centering

        # Logo
        logo = QLabel()
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_dir, "assets", "ECB OOP_logo.png")

        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            print(f"⚠️ Could not load logo image at: {image_path}")

        logo.setPixmap(
            pixmap.scaled(225, 225, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        )
        logo.setStyleSheet("background: transparent;")

        # Welcome text
        welcome_label = QLabel("Welcome to Watt's my Electricity Bill?")
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_label.setStyleSheet("""
            background: transparent;
            font-family: 'Poppins';
            font-size: 24px;
            font-weight: bold;
            color: #FF5C00;
            margin: 0;
            padding: 0;
        """)
        

        # Replaced button with progress bar
        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.progress.setValue(0)
        self.progress.setFixedWidth(750)
        self.progress.setFixedHeight(24)
        self.progress.setTextVisible(False)
        self.progress.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progress.setStyleSheet("""
        QProgressBar {
            border: none;
            border-radius: 12px;
            background-color: #555555;
            padding: 2px;  
        }
        QProgressBar::chunk {
            border-radius: 10px; 
            background-color: #F4A261;
            margin: 0px;
        }
        """)


        # Animation setup
        from PyQt6.QtCore import QPropertyAnimation, QEasingCurve
        self.progress_anim = QPropertyAnimation(self.progress, b"value")
        self.progress_anim.setDuration(2000)  # total duration (ms)
        self.progress_anim.setStartValue(0)
        self.progress_anim.setEndValue(100)
        self.progress_anim.setEasingCurve(QEasingCurve.Type.InOutCubic)
        self.progress_anim.finished.connect(self.fade_out)


        # Layout
        layout.addStretch()
        layout.addWidget(logo)
        layout.addSpacing(5)
        layout.addWidget(welcome_label)
        layout.addSpacing(20)
        layout.addWidget(self.progress)
        layout.addStretch()

        # Set background gradient (match login style)
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:0, y2:1,
                    stop:0 #FF8C00, stop:1 #FF4500
                );
            }
        """)

        # Fade effect
        self.opacity = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.opacity)
        self.opacity.setOpacity(0)
        self.fade_in()

        # timer for progress
        self._timer = QTimer(self)
        self._timer.setInterval(30)  # adjust speed as desired
        self._timer.timeout.connect(self._advance_progress)

        # make layout responsive
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

    # Fade in animation
    def fade_in(self):
        self.anim = QPropertyAnimation(self.opacity, b"opacity")
        self.anim.setDuration(1500)
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        # start filling progress after fade in
        self.anim.finished.connect(self.start_loading)
        self.anim.start()

    # start filling the progress bar
    def start_loading(self):
        self.progress.setValue(0)
        self.progress_anim.start()


    # advance the progress bar, then transition when done
    def _advance_progress(self):
        val = self.progress.value() + 2
        if val >= 100:
            self.progress.setValue(100)
            self._timer.stop()
            self.fade_out()   # proceed to fade out and switch screen
            return
        self.progress.setValue(val)

    def fade_out(self):
        self.anim = QPropertyAnimation(self.opacity, b"opacity")
        self.anim.setDuration(1000)
        self.anim.setStartValue(1)
        self.anim.setEndValue(0)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.anim.finished.connect(self.go_to_login)
        self.anim.start()

    def go_to_login(self):
        """Switch to the login page"""
        self.stacked_widget.setCurrentIndex(1)  # Login page at index 1
        login_screen = self.stacked_widget.widget(1)
        if hasattr(login_screen, 'fade_in'):
            login_screen.fade_in()
