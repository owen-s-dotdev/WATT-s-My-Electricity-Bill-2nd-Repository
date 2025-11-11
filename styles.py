# styles.py
"""
Contains the centralized QSS (Qt StyleSheet) strings
for the Light and Dark themes.
"""

# --- Light Theme (Your original MODERN_STYLESHEET + extracted styles) ---
LIGHT_STYLESHEET = """
/* ---- Global ---- */
QWidget {
    font-family: 'Poppins', 'Arial', sans-serif;
    font-size: 14px;
    background-color: #F8F9FA; /* Light gray background */
    color: #2C3E50; /* Dark text */
}
QMainWindow {
    background-color: #FFFFFF;
}

/* --- Gradient background for calculator page --- */
#centralWidget {
    background: qlineargradient(
        x1:0, y1:0, x2:1, y2:0,
        stop:0 #ff914d,
        stop:1 #ffd27f
    );
}

/* --- GroupBox Styling (Light Gray) --- */
QGroupBox {
    background-color: #f9f9f9;
    color: #333333;
    border: 1px solid #eeeeee;
    border-radius: 8px;
    margin-top: 10px;
    padding: 10px;
}
QGroupBox:title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 0 5px;
    color: #333333;
    font-weight: bold;
    font-size: 16px;
    left: 10px;
    top: 3px;
}

/* --- Button Styling --- */
QPushButton {
    background-color: #f8f8f8;
    color: #cc6600;
    border: 1px solid #cc6600;
    border-radius: 8px;
    padding: 8px 12px;
    font-weight: bold;
}
QPushButton:hover {
    background-color: #fbeadb;
}
QPushButton:pressed {
    background-color: #e3e6e4;
}

/* --- ComboBox Styling (Pure White) --- */
QComboBox {
    background-color: #ffffff;
    border: 1px solid #dddddd;
    border-radius: 6px;
    padding: 6px;
    color: #333333;
}
QComboBox QAbstractItemView {
    background-color: #ffffff;
    border: 1px solid #dddddd;
    selection-background-color: #ffd27f;
    selection-color: #333333;
    outline: 0px;
}
QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 20px;
    border-left-width: 1px;
    border-left-color: #dddddd;
    border-left-style: solid;
    border-top-right-radius: 6px;
    border-bottom-right-radius: 6px;
    /* REMOVED: image, background-repeat, background-position */
}

/* --- NEW SELECTOR for the arrow --- */
QComboBox::down-arrow {
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 5px solid #333333; /* Black arrow */
    width: 0px;
    height: 0px;
    /* margin: 4px 4px 0px 0px; */ /* <-- REMOVED THIS */
    margin-top: 10px;  /* Push down from top */
    margin-left: 5px;  /* Center horizontally */
    margin-right: 5px; /* Center horizontally */
}


/* --- Label Styling (Transparent) --- */
QLabel {
    color: #333333;
    background-color: transparent; 
    padding: 4px;
}

/* --- QDateEdit Styling --- */
QDateEdit {
    background-color: #ffffff;
    border: 1px solid #dddddd;
    border-radius: 6px;
    padding: 6px;
    color: #333333;
}
QDateEdit::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 20px;
    border-left-width: 1px;
    border-left-color: #dddddd;
    border-left-style: solid;
    border-top-right-radius: 6px;
    border-bottom-right-radius: 6px;
    /* REMOVED image properties */
}

/* --- NEW SELECTOR for DateEdit arrow --- */
QDateEdit::down-arrow {
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 5px solid #333333; /* Black arrow */
    width: 0px;
    height: 0px;
    /* margin: 4px 4px 0px 0px; */ /* <-- REMOVED THIS */
    margin-top: 10px;  /* Push down from top */
    margin-left: 5px;  /* Center horizontally */
    margin-right: 5px; /* Center horizontally */
}


/* --- CALENDAR STYLE --- */
QCalendarWidget {
    background-color: #ffffff;
    border: 1px solid #eeeeee;
    border-radius: 8px;
}
QCalendarWidget QWidget#qt_calendar_navigationbar {
    background-color: #fbeadb;
    border-bottom: 1px solid #eeeeee;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
}
QCalendarWidget QToolButton {
    color: #cc6600;
    font-weight: bold;
    background-color: transparent;
    border: none;
    margin: 5px;
    padding: 5px;
    border-radius: 4px;
}
QCalendarWidget QToolButton:hover {
    background-color: #ffd27f;
}
QCalendarWidget QToolButton:pressed {
    background-color: #ff914d;
    color: #ffffff;
}
QCalendarWidget QHeaderView::section {
    background-color: #ffffff;
    border: none;
    padding: 6px;
    font-weight: 500;
    color: #333333;
}
QCalendarWidget QTableView {
    background-color: #ffffff;
    border: 1px solid #eeeeee; 
    gridline-color: #eeeeee;
}
QCalendarWidget QTableView::item {
    background-color: transparent;
    color: #333333;
    border-radius: 4px;
}
QCalendarWidget QTableView::item:disabled {
    color: #cccccc;
    background-color: #f9f9f9;
}
QCalendarWidget QTableView::item:today {
    background-color: #fbeadb;
    color: #cc6600;
    font-weight: bold;
}
QCalendarWidget QTableView::item:selected {
    background-color: #ff914d;
    color: #ffffff;
}
/* --- END OF ORIGINAL MODERN_STYLESHEET --- */


/* --- STYLES EXTRACTED FROM UI FILES --- */

/* ---- GetStartedScreen ---- */
GetStartedScreen {
    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FF8C00, stop:1 #FF4500);
}
GetStartedScreen QLabel {
    background: transparent;
}
QLabel#getStartedWelcome {
    font-size: 24px;
    font-weight: bold;
    color: #FF5C00;
}
GetStartedScreen QProgressBar {
    border: none;
    border-radius: 12px;
    background-color: #555555;
    padding: 2px;
}
GetStartedScreen QProgressBar::chunk {
    border-radius: 10px;
    background-color: #F4A261;
    margin: 0px;
}


/* ---- LoginPage ---- */
LoginPage {
    background-color: white;
    color: #FF5C00;
}
LoginPage QLabel {
    background: transparent;
    font-family: 'Poppins';
}
LoginPage QLineEdit {
    background-color: #FFB97D;
    border: none;
    border-radius: 4px;
    padding: 10px;
    color: white;
    font-size: 14px;
    font-family: 'Poppins';
}
LoginPage QLineEdit::placeholder { color: white; }
LoginPage QPushButton#orangeButton {
    background-color: #FF5C00;
    color: white;
    font-size: 16px;
    font-weight: bold;
    padding: 10px 25px;
    border-radius: 25px;
    border: none;
    font-family: 'Poppins';
}
LoginPage QPushButton#orangeButton:hover { background-color: #FF7B1A; }
LoginPage QPushButton#guestButton {
    background-color: transparent;
    color: #FF5C00;
    font-size: 14px;
    border: none;
    font-family: 'Poppins';
}
LoginPage QPushButton#guestButton:hover { text-decoration: underline; }

/* ---- NavigationPanel ---- */
NavigationPanel {
    background-color: #FFFFFF;
    border-right: 20px solid #FF4B2B;
}
NavigationPanel > QLabel { /* Use > to target only the "Menu" title */
    color: #FF3C00;
    font-family: 'Poppins';
    font-size: 20px;
    font-weight: bold;
    padding-left: 16px;
}
NavigationPanel QListWidget {
    background-color: transparent;
    border: none;
    outline: none;
}
NavigationPanel QListWidget::item {
    color: #FF3C00;
    padding: 18px 16px;
    font-family: 'Poppins';
    font-size: 20px;
    font-weight: bold;
}
NavigationPanel QListWidget::item:selected {
    background-color: #FFC04C;
    color: #FF3C00;
}
NavigationPanel QListWidget::item:hover { background-color: #FFD580; }

/* ---- Pages (Profile, History, Settings) ---- */
QLabel#pageTitle {
    font-size: 24px;
    color: #FF5C00;
    margin: 20px 0;
    font-family: 'Poppins';
}
HistoryPage QTextEdit {
    background-color: #FFF3E0;
    border: 1px solid #FFB97D;
    border-radius: 10px;
    padding: 12px;
    font-family: 'Poppins';
    font-size: 14px;
    color: #2C3E50;
}
"""


# --- Dark Theme (New) ---
DARK_STYLESHEET = """
/* ---- Global ---- */
QWidget {
    font-family: 'Poppins', 'Arial', sans-serif;
    font-size: 14px;
    background-color: #2E2E2E; /* Dark background */
    color: #EAEAEA; /* Light text */
}
QMainWindow {
    background-color: #2E2E2E;
}

/* --- Gradient background for calculator page --- */
#centralWidget {
    background: qlineargradient(
        x1:0, y1:0, x2:1, y2:0,
        stop:0 #ff914d,
        stop:1 #ffd27f
    );
}

/* --- GroupBox Styling (Dark) --- */
QGroupBox {
    background-color: #353535;
    color: #EAEAEA;
    border: 1px solid #444444;
    border-radius: 8px;
    margin-top: 10px;
    padding: 10px;
}
QGroupBox:title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 0 5px;
    color: #EAEAEA;
    font-weight: bold;
    font-size: 16px;
    left: 10px;
    top: 3px;
}

/* --- Button Styling (Dark) --- */
QPushButton {
    background-color: #4A4A4A;
    color: #F4A261; /* Light Orange */
    border: 1px solid #F4A261;
    border-radius: 8px;
    padding: 8px 12px;
    font-weight: bold;
}
QPushButton:hover {
    background-color: #5A5A5A;
}
QPushButton:pressed {
    background-color: #6A6A6A;
}

/* --- ComboBox Styling (Dark) --- */
QComboBox {
    background-color: #353535;
    border: 1px solid #555555;
    border-radius: 6px;
    padding: 6px;
    color: #EAEAEA;
}
QComboBox QAbstractItemView {
    background-color: #353535;
    border: 1px solid #555555;
    selection-background-color: #FF5C00;
    selection-color: #FFFFFF;
    outline: 0px;
}
QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 20px;
    border-left-width: 1px;
    border-left-color: #555555;
    border-left-style: solid;
    border-top-right-radius: 6px;
    border-bottom-right-radius: 6px;
    /* REMOVED: image, background-repeat, background-position */
}

/* --- NEW SELECTOR for the arrow (Dark) --- */
QComboBox::down-arrow {
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 5px solid #EAEAEA; /* White arrow */
    width: 0px;
    height: 0px;
    /* margin: 4px 4px 0px 0px; */ /* <-- REMOVED THIS */
    margin-top: 10px;  /* Push down from top */
    margin-left: 5px;  /* Center horizontally */
    margin-right: 5px; /* Center horizontally */
}


/* --- Label Styling (Dark) --- */
QLabel {
    color: #EAEAEA;
    background-color: transparent; 
    padding: 4px;
}

/* --- QDateEdit Styling (Dark) --- */
QDateEdit {
    background-color: #353535;
    border: 1px solid #555555;
    border-radius: 6px;
    padding: 6px;
    color: #EAEAEA;
}
QDateEdit::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 20px;
    border-left-width: 1px;
    border-left-color: #555555;
    border-left-style: solid;
    border-top-right-radius: 6px;
    border-bottom-right-radius: 6px;
    /* REMOVED image properties */
}

/* --- NEW SELECTOR for DateEdit arrow (Dark) --- */
QDateEdit::down-arrow {
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 5px solid #EAEAEA; /* White arrow */
    width: 0px;
    height: 0px;
    /* margin: 4px 4px 0px 0px; */ /* <-- REMOVED THIS */
    margin-top: 10px;  /* Push down from top */
    margin-left: 5px;  /* Center horizontally */
    margin-right: 5px; /* Center horizontally */
}


/* --- CALENDAR STYLE (Dark) --- */
QCalendarWidget {
    background-color: #353535;
    border: 1px solid #444444;
    border-radius: 8px;
}
QCalendarWidget QWidget#qt_calendar_navigationbar {
    background-color: #4A4A4A;
    border-bottom: 1px solid #444444;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
}
QCalendarWidget QToolButton {
    color: #F4A261;
    font-weight: bold;
    background-color: transparent;
    border: none;
    margin: 5px;
    padding: 5px;
    border-radius: 4px;
}
QCalendarWidget QToolButton:hover {
    background-color: #5A5A5A;
}
QCalendarWidget QToolButton:pressed {
    background-color: #FF5C00;
    color: #ffffff;
}
QCalendarWidget QHeaderView::section {
    background-color: #353535;
    border: none;
    padding: 6px;
    font-weight: 500;
    color: #AAAAAA;
}
QCalendarWidget QTableView {
    background-color: #353535;
    border: 1px solid #444444; 
    gridline-color: #444444;
}
QCalendarWidget QTableView::item {
    background-color: transparent;
    color: #EAEAEA;
    border-radius: 4px;
}
QCalendarWidget QTableView::item:disabled {
    color: #777777;
    background-color: #2E2E2E;
}
QCalendarWidget QTableView::item:today {
    background-color: #5A5A5A;
    color: #F4A261;
    font-weight: bold;
}
QCalendarWidget QTableView::item:selected {
    background-color: #FF5C00;
    color: #ffffff;
}
/* --- END OF DARK THEME --- */


/* --- STYLES EXTRACTED FROM UI FILES (Dark) --- */

/* ---- GetStartedScreen ---- */
GetStartedScreen {
    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #D45500, stop:1 #C23400);
}
GetStartedScreen QLabel {
    background: transparent;
}
QLabel#getStartedWelcome {
    font-size: 24px;
    font-weight: bold;
    color: #F4A261; /* Lighter orange */
}
GetStartedScreen QProgressBar {
    border: none;
    border-radius: 12px;
    background-color: #555555;
    padding: 2px;
}
GetStartedScreen QProgressBar::chunk {
    border-radius: 10px;
    background-color: #FF5C00; /* Brighter chunk for dark bg */
    margin: 0px;
}

/* ---- LoginPage ---- */
LoginPage {
    background-color: #2E2E2E;
    color: #F4A261;
}
LoginPage QLabel {
    background: transparent;
    font-family: 'Poppins';
}
LoginPage QLineEdit {
    background-color: #4A4A4A;
    border: 1px solid #555;
    border-radius: 4px;
    padding: 10px;
    color: #EAEAEA;
    font-size: 14px;
    font-family: 'Poppins';
}
LoginPage QLineEdit::placeholder { color: #999; }
LoginPage QPushButton#orangeButton {
    background-color: #FF5C00;
    color: white;
    font-size: 16px;
    font-weight: bold;
    padding: 10px 25px;
    border-radius: 25px;
    border: none;
    font-family: 'Poppins';
}
LoginPage QPushButton#orangeButton:hover { background-color: #FF7B1A; }
LoginPage QPushButton#guestButton {
    background-color: transparent;
    color: #F4A261;
    font-size: 14px;
    border: none;
    font-family: 'Poppins';
}
LoginPage QPushButton#guestButton:hover { text-decoration: underline; }

/* ---- NavigationPanel ---- */
NavigationPanel {
    background-color: #353535;
    border-right: 20px solid #FF4B2B;
}
NavigationPanel > QLabel {
    color: #F4A261;
    font-family: 'Poppins';
    font-size: 20px;
    font-weight: bold;
    padding-left: 16px;
}
NavigationPanel QListWidget {
    background-color: transparent;
    border: none;
    outline: none;
}
NavigationPanel QListWidget::item {
    color: #F4A261;
    padding: 18px 16px;
    font-family: 'Poppins';
    font-size: 20px;
    font-weight: bold;
}
NavigationPanel QListWidget::item:selected {
    background-color: #555555;
    color: #FF5C00;
}
NavigationPanel QListWidget::item:hover { background-color: #4A4A4A; }

/* ---- Pages (Profile, History, Settings) ---- */
QLabel#pageTitle {
    font-size: 24px;
    color: #F4A261;
    margin: 20px 0;
    font-family: 'Poppins';
}
HistoryPage QTextEdit {
    background-color: #353535;
    border: 1px solid #555;
    border-radius: 10px;
    padding: 12px;
    font-family: 'Poppins';
    font-size: 14px;
    color: #EAEAEA;
}
"""