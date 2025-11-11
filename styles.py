# styles.py

"""
Contains the application's global QSS stylesheet.
"""

MODERN_STYLESHEET = """
    /* --- Global Font --- */
    QWidget {
        font-family: 'Poppins';
        font-size: 14px;
    }

    /* --- 4. TARGET THE GRADIENT BACKGROUND --- */
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
    }
    

    /* CALENDAR STYLE */

    /* --- Main Calendar Widget --- */
    QCalendarWidget {
        background-color: #ffffff;
        border: 1px solid #eeeeee;
        border-radius: 8px;
    }

    /* --- Navigation Bar (Month/Year) --- */
    QCalendarWidget QWidget#qt_calendar_navigationbar {
        background-color: #fbeadb; /* Light orange hover color */
        border-bottom: 1px solid #eeeeee;
        border-top-left-radius: 8px;
        border-top-right-radius: 8px;
    }
    
    /* --- Month/Year Text & Arrow Buttons --- */
    QCalendarWidget QToolButton {
        color: #cc6600; /* Dark Orange */
        font-weight: bold;
        background-color: transparent;
        border: none;
        margin: 5px;
        padding: 5px;
        border-radius: 4px;
    }
    QCalendarWidget QToolButton:hover {
        background-color: #ffd27f; /* Lighter accent orange */
    }
    QCalendarWidget QToolButton:pressed {
        background-color: #ff914d; /* Main accent orange */
        color: #ffffff;
    }

    /* --- Weekday Headers (Mon, Tue, Wed...) --- */
    QCalendarWidget QHeaderView::section {
        background-color: #ffffff;
        border: none;
        padding: 6px;
        font-weight: 500;
        color: #333333;
    }

    /* --- Main Date Grid --- */
    QCalendarWidget QTableView {
        background-color: #ffffff;
        border: 1px solid #eeeeee; 
        gridline-color: #eeeeee; /* Remove grid lines */
    }

    /* --- Individual Date Cells --- */
    QCalendarWidget QTableView::item {
        background-color: transparent;
        color: #333333;
        border-radius: 4px;
    }

    /* --- Dates from other months --- */
    QCalendarWidget QTableView::item:disabled {
        color: #cccccc;
        background-color: #f9f9f9;
    }

    /* --- Today's Date --- */
    QCalendarWidget QTableView::item:today {
        background-color: #fbeadb; /* Light orange */
        color: #cc6600; /* Dark orange text */
        font-weight: bold;
    }

    /* --- Selected Date (Clicked) --- */
    QCalendarWidget QTableView::item:selected {
        background-color: #ff914d; /* Main accent orange */
        color: #ffffff; /* White text */
    }
"""