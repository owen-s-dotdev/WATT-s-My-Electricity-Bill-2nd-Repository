# styles.py

"""
Stores the QSS stylesheet for the application.
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
        top: 3px; /* <-- ADDED: Pushes the title text down 3px */
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
    
    /* --- Output Label Specifics --- */
    #outputLabel {
        background-color: transparent; 
        font-size: 16px; 
        font-weight: 500;
    }
"""