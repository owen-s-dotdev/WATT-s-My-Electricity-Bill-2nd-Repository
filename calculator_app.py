#calculator_app.py

import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QLabel, QComboBox,
    QPushButton, QMessageBox, QHBoxLayout, QGroupBox, QGraphicsOpacityEffect
)
from PyQt6.QtCore import QSize, QPropertyAnimation, QEasingCurve

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.current_user = None  # logged in user
        self.setWindowTitle("Watt's my Electricity Bill?")
        central = QWidget()
        central.setAutoFillBackground(True)
        central.setStyleSheet("""
            background: qlineargradient(
                x1:0, y1:0, x2:1, y2:0,  /* left to right */
                stop:0 #ff914d,           /* darker orange on the left */
                stop:1 #ffd27f            /* lighter orange on the right */
            );
        """)
        self.main_layout = QVBoxLayout(central)
        self.setCentralWidget(central)
        

        # ADDED FADE IN EFFECT
        self.opacity = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.opacity)
        self.opacity.setOpacity(0)

        # button style for each group
        button_style = """
            QPushButton {
                background-color: #ffffff;      /* white background */
                color: #333333;                 /* dark text */
                border: 2px solid #cc6600;      /* darker orange border to match QGroupBoxes */
                border-radius: 6px;
                padding: 6px 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #f0f0f0;      /* light gray on hover */
            }
            QPushButton:pressed {
                background-color: #e0e0e0;      /* slightly darker gray when pressed */
            }
        """

        groupbox_style = """
            QGroupBox {
                background-color: #ffffff;       /* solid white */
                color: #333333;                  /* dark text */
                font-weight: bold;
                border: 2px solid #cc6600;       /* darker orange border */
                border-radius: 8px;
                margin-top: 10px;
            }
            QGroupBox:title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 0 3px;
            }
        """
        #  Input Section
        input_grid_layout = QGridLayout()
        input_group = QGroupBox("Appliance Input")
        # Input Section
        input_group.setStyleSheet(groupbox_style)

        input_group.setLayout(input_grid_layout)

        # Default preset appliance ratings
        self.appliance_presets = {
        "Refrigerator": {"watts": "150W", "usage": "24", "rate": "12"},
        "Television": {"watts": "100W", "usage": "4", "rate": "12"},
        "Air Conditioner": {"watts": "1200W", "usage": "8", "rate": "12"},
        "Electric Fan": {"watts": "75W", "usage": "6", "rate": "12"},
        "Light Bulb": {"watts": "10W", "usage": "5", "rate": "12"},
        "Washing Machine": {"watts": "500W", "usage": "1", "rate": "12"},
        "Microwave Oven": {"watts": "1000W", "usage": "0.5", "rate": "12"},
        "Electric Kettle": {"watts": "1500W", "usage": "0.3", "rate": "12"},
        "Rice Cooker": {"watts": "700W", "usage": "1", "rate": "12"},
        "Hair Dryer": {"watts": "1200W", "usage": "0.2", "rate": "12"},
        "Desktop Computer": {"watts": "250W", "usage": "6", "rate": "12"},
        "Laptop": {"watts": "60W", "usage": "6", "rate": "12"},
        "Wi-Fi Router": {"watts": "10W", "usage": "24", "rate": "12"},
        "Electric Iron": {"watts": "1000W", "usage": "0.5", "rate": "12"},
        "Blender": {"watts": "300W", "usage": "0.2", "rate": "12"},
        "Toaster": {"watts": "800W", "usage": "0.2", "rate": "12"},
        "Water Dispenser": {"watts": "100W", "usage": "8", "rate": "12"},
        "Printer": {"watts": "50W", "usage": "0.5", "rate": "12"},
        }

        input_type_txt = QLabel("Select Appliance Type")
        self.input_type_combo = QComboBox()
        self.input_type_combo.addItem("Select Appliance...")
        self.input_type_combo.model().item(0).setEnabled(False) 
        self.input_type_combo.addItems(sorted(self.appliance_presets.keys()))
        self.input_type_combo.setCurrentIndex(0)  
        self.input_type_combo.setEditable(False)
        
        self.input_type_combo.currentIndexChanged.connect(self.on_appliance_selected)

        power_label = QLabel("Power Consumption")
        power_label_unit = QLabel("Watts (W)")
        self.power_input = QComboBox()
        self.power_input.setEditable(True)
        self.power_input.addItems(["10W","75W","100W", "150W","200W", "300W", "500W", "750W", "1000W", "1200W", "1500W"])
        self.power_input.setPlaceholderText("Select or enter power consumption")

        usage_label = QLabel("Use per day")
        usage_label_unit = QLabel("Hours")
        self.usage_input = QComboBox()
        self.usage_input.setEditable(True)
        self.usage_input.addItems(["0.5", "1", "2", "3", "4", "5", "6", "8", "10", "12", "16", "24"])
        self.usage_input.setPlaceholderText("Select or enter hours")

        rate_label = QLabel("Electricity Rate")
        rate_label_unit = QLabel("₱/kWh")
        self.rate_input = QComboBox()
        self.rate_input.setEditable(True)
        self.rate_input.addItems(["10", "12", "15", "18", "20"])
        self.rate_input.setPlaceholderText("Select or enter rate")

        appliances_label = QLabel("Appliances Added")
        self.appliances_added_combo = QComboBox()
        self.appliances_added_combo.setEditable(False)
        self.appliances_added_combo.setPlaceholderText("Selected appliances will appear here")

        input_grid_layout.addWidget(input_type_txt, 0, 0)
        input_grid_layout.addWidget(self.input_type_combo, 0, 1)

        input_grid_layout.addWidget(power_label, 1, 0)
        input_grid_layout.addWidget(self.power_input, 1, 1)
        input_grid_layout.addWidget(power_label_unit, 1, 3)

        input_grid_layout.addWidget(usage_label, 2, 0)
        input_grid_layout.addWidget(self.usage_input, 2, 1)
        input_grid_layout.addWidget(usage_label_unit, 2, 3)

        input_grid_layout.addWidget(rate_label, 3, 0)
        input_grid_layout.addWidget(self.rate_input, 3, 1)
        input_grid_layout.addWidget(rate_label_unit, 3, 3)

        input_grid_layout.addWidget(appliances_label, 4, 0)
        input_grid_layout.addWidget(self.appliances_added_combo, 4, 1)

        #  Button Section
        btn_layout = QHBoxLayout()
        btn_group = QGroupBox("Actions")
        # Button Section
        btn_group.setStyleSheet(groupbox_style)
        btn_group.setLayout(btn_layout)

        add_btn = QPushButton("Add Appliance")
        add_btn.clicked.connect(self.handle_add_appliance)

        del_btn = QPushButton("Remove Appliance")
        del_btn.clicked.connect(self.handle_remove_appliance)

        calc_btn = QPushButton("Calculate")
        calc_btn.clicked.connect(self.handle_calculate)

        reset_btn = QPushButton("Reset")
        reset_btn.clicked.connect(self.handle_reset)

        btn_layout.addWidget(add_btn)
        btn_layout.addWidget(del_btn)
        btn_layout.addWidget(calc_btn)
        btn_layout.addWidget(reset_btn)

        #  Output Section
        output_grid_layout = QGridLayout()
        output_group = QGroupBox("Estimated Cost")
        # Output Section
        output_group.setStyleSheet(groupbox_style)
        output_group.setLayout(output_grid_layout)

        self.daily_cost_label = QLabel("Daily Cost: ₱0.00")
        self.monthly_cost_label = QLabel("Monthly Estimate: ₱0.00")
        output_grid_layout.addWidget(self.daily_cost_label, 0, 0)
        output_grid_layout.addWidget(self.monthly_cost_label, 1, 0)

        #  Add to Main Layout
        self.main_layout.addWidget(input_group)
        self.main_layout.addWidget(btn_group)
        self.main_layout.addWidget(output_group)

    # ADDED FADE IN ANIMATION
    def fade_in(self):
        self.anim = QPropertyAnimation(self.opacity, b"opacity")
        self.anim.setDuration(1500)
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.anim.start()

    def handle_add_appliance(self):
        appliance = self.input_type_combo.currentText()
        power = self.power_input.currentText()
        usage = self.usage_input.currentText()
        rate = self.rate_input.currentText()

        if not (appliance and power and usage and rate):
            QMessageBox.warning(self, "Missing Input", "Please fill in all fields before adding.")
            return

        try:
            float(power.replace("W", "").strip())
            float(usage.strip())
            float(rate.strip())
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter valid numeric values for power, usage, and rate.")
            return

        entry = f"{appliance} - {power} x {usage}hr @ {rate}₱/kWh"
        self.appliances_added_combo.addItem(entry)

    def handle_remove_appliance(self):
        index = self.appliances_added_combo.currentIndex()
        if index >= 0:
            self.appliances_added_combo.removeItem(index)
        else:
            QMessageBox.information(self, "No Selection", "Please select an appliance to remove.")

    def handle_calculate(self):
        total_cost = 0.0

        for i in range(self.appliances_added_combo.count()):
            item_text = self.appliances_added_combo.itemText(i)
            try:
                parts = item_text.split(" - ")[1].split(" x ")
                watts = float(parts[0].replace("W", "").strip())
                usage_hr = float(parts[1].split("hr")[0])
                rate = float(parts[1].split("@ ")[1].replace("₱/kWh", ""))
                kwh = (watts / 1000) * usage_hr
                cost = kwh * rate
                total_cost += cost
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to parse item: {item_text}\n{e}")
                return

        monthly_cost = total_cost * 30
        QMessageBox.information(self, "Estimated Cost",
            f"Your estimated daily electricity cost is ₱{total_cost:.2f}\n"
            f"Monthly estimate: ₱{monthly_cost:.2f}"
        )
        self.daily_cost_label.setText(f"Daily Cost: ₱{total_cost:.2f}")
        self.monthly_cost_label.setText(f"Monthly Estimate: ₱{monthly_cost:.2f}")

        if self.current_user:
            user_dir = os.path.join(os.getcwd(), "users", self.current_user)
            os.makedirs(user_dir, exist_ok=True)
            history_path = os.path.join(user_dir, "history.txt")
            with open(history_path, "a", encoding="utf-8") as f:
                f.write("---- New Calculation ----\n")
                for i in range(self.appliances_added_combo.count()):
                    f.write(self.appliances_added_combo.itemText(i) + "\n")
                f.write(f"Total Daily: ₱{total_cost:.2f}, Monthly: ₱{monthly_cost:.2f}\n\n")

        # preset filling method
    def fill_appliance_defaults(self, appliance_name):
        preset = self.appliance_presets.get(appliance_name)
        if preset:
            self.power_input.setEditText(str(preset["watts"]))
            self.usage_input.setEditText(str(preset["usage"]))
            self.rate_input.setEditText(str(preset["rate"]))

    
    def on_appliance_selected(self, index):
        if index <= 0:
            return
        appliance_name = self.input_type_combo.itemText(index)
        self.fill_appliance_defaults(appliance_name)
    
    def handle_reset(self):
        self.input_type_combo.setCurrentIndex(0)
        self.input_type_combo.setEditText("") 
        self.power_input.setCurrentIndex(-1)
        self.usage_input.setCurrentIndex(-1)
        self.rate_input.setCurrentIndex(-1)
        self.power_input.setEditText("")
        self.usage_input.setEditText("")
        self.rate_input.setEditText("")
        self.appliances_added_combo.clear()
        self.daily_cost_label.setText("Daily Cost: ₱0.00")
        self.monthly_cost_label.setText("Monthly Estimate: ₱0.00")
