# ui_widgets.py

"""
Contains custom QWidget classes that encapsulate UI sections.
"""
from PyQt6.QtWidgets import (
    QWidget, QGridLayout, QLabel, QComboBox,
    QPushButton, QHBoxLayout, QGroupBox, QDateEdit
)
from PyQt6.QtCore import QDate

class InputWidget(QGroupBox):
    """
    A QGroupBox that contains all the input fields for the calculator.
    """
    def __init__(self, appliance_presets, parent=None):
        super().__init__(parent)
        
        layout = QGridLayout(self)

        # --- Appliance Type ---
        input_type_txt = QLabel("Select Appliance Type")
        self.input_type_combo = QComboBox()
        # Add presets first
        self.input_type_combo.addItems(sorted(appliance_presets.keys()))
        
        # Make it editable and add placeholder text
        self.input_type_combo.setEditable(True)
        self.input_type_combo.setPlaceholderText("Select preset or enter new appliance...")
        self.input_type_combo.setCurrentIndex(-1) # Show placeholder

        # --- Power Input ---
        power_label = QLabel("Power Consumption")
        power_label_unit = QLabel("Watts (W)")
        self.power_input = QComboBox()
        self.power_input.setEditable(True)
        self.power_input.addItems(["10W","75W","100W", "150W","200W", "300W", "500W", "750W", "1000W", "1200W", "1500W"])
        self.power_input.setPlaceholderText("Select or enter power consumption")

        # --- Usage Input ---
        usage_label = QLabel("Use per day")
        usage_label_unit = QLabel("Hours")
        self.usage_input = QComboBox()
        self.usage_input.setEditable(True)
        self.usage_input.addItems(["0.5", "1", "2", "3", "4", "5", "6", "8", "10", "12", "16", "24"])
        self.usage_input.setPlaceholderText("Select or enter hours")

        # --- Rate Input ---
        rate_label = QLabel("Electricity Rate")
        rate_label_unit = QLabel("₱/kWh")
        self.rate_input = QComboBox()
        self.rate_input.setEditable(True)
        self.rate_input.addItems(["10", "12", "15", "18", "20"])
        self.rate_input.setPlaceholderText("Select or enter rate")

        # --- Date Input ---
        date_label = QLabel("Calculation Date")
        self.date_input = QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QDate.currentDate())
        self.date_input.setDisplayFormat("yyyy-MM-dd")

        # --- Appliances Added ---
        appliances_label = QLabel("Appliances Added")
        self.appliances_added_combo = QComboBox()
        self.appliances_added_combo.setEditable(False)
        self.appliances_added_combo.setPlaceholderText("Selected appliances will appear here")

        # --- Add to Layout ---
        layout.addWidget(input_type_txt, 0, 0)
        layout.addWidget(self.input_type_combo, 0, 1, 1, 2)

        layout.addWidget(power_label, 1, 0)
        layout.addWidget(self.power_input, 1, 1)
        layout.addWidget(power_label_unit, 1, 2) 

        layout.addWidget(usage_label, 2, 0)
        layout.addWidget(self.usage_input, 2, 1)
        layout.addWidget(usage_label_unit, 2, 2)

        layout.addWidget(rate_label, 3, 0)
        layout.addWidget(self.rate_input, 3, 1)
        layout.addWidget(rate_label_unit, 3, 2)

        layout.addWidget(date_label, 4, 0)
        layout.addWidget(self.date_input, 4, 1, 1, 2)

        layout.addWidget(appliances_label, 5, 0)
        layout.addWidget(self.appliances_added_combo, 5, 1, 1, 2)
        
        layout.setColumnStretch(1, 1) 
        layout.setColumnStretch(2, 0)

    def reset(self):
        """Resets all input fields to their default state."""
        self.input_type_combo.setCurrentIndex(-1)
        self.input_type_combo.setEditText("")
        self.power_input.setCurrentIndex(-1)
        self.usage_input.setCurrentIndex(-1)
        self.rate_input.setCurrentIndex(-1)
        self.power_input.setEditText("")
        self.usage_input.setEditText("")
        self.rate_input.setEditText("")
        self.date_input.setDate(QDate.currentDate())
        self.appliances_added_combo.clear()


class ButtonWidget(QGroupBox):
    """
    A QGroupBox that contains all the action buttons.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        
        layout = QHBoxLayout(self)

        self.add_btn = QPushButton("Add Appliance")
        self.del_btn = QPushButton("Remove Appliance")
        self.calc_btn = QPushButton("Calculate")
        self.reset_btn = QPushButton("Reset")

        layout.addWidget(self.add_btn)
        layout.addWidget(self.del_btn)
        layout.addWidget(self.calc_btn)
        layout.addWidget(self.reset_btn)


class OutputWidget(QGroupBox):
    """
    A QGroupBox that displays the calculation results.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        
        layout = QGridLayout(self)

        self.daily_cost_label = QLabel("Daily Cost: ₱0.00")
        self.monthly_cost_label = QLabel("Monthly Estimate: ₱0.00")
        
        output_label_style = "background-color: transparent; font-size: 16px; font-weight: 500;"
        self.daily_cost_label.setStyleSheet(output_label_style)
        self.monthly_cost_label.setStyleSheet(output_label_style)

        layout.addWidget(self.daily_cost_label, 0, 0)
        layout.addWidget(self.monthly_cost_label, 1, 0)

    def set_costs(self, daily_cost, monthly_cost):
        """Updates the cost labels with formatted values."""
        self.daily_cost_label.setText(f"Daily Cost: ₱{daily_cost:.2f}")
        self.monthly_cost_label.setText(f"Monthly Estimate: ₱{monthly_cost:.2f}")
    
    def reset(self):
        """Resets the cost labels to zero."""
        self.daily_cost_label.setText("Daily Cost: ₱0.00")
        self.monthly_cost_label.setText("Monthly Estimate: ₱0.00")