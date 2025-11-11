"""
Defines encapsulated QGroupBox widgets for the application UI.
"""
from PyQt6.QtWidgets import (
    QWidget, QGridLayout, QLabel, QComboBox,
    QPushButton, QHBoxLayout, QGroupBox
)
from PyQt6.QtCore import pyqtSignal

class InputGroup(QGroupBox):
    """
    A QGroupBox that contains all the input fields and the appliance list.
    """
    def __init__(self, appliance_presets, parent=None):
        super().__init__(parent)
        self.appliance_presets = appliance_presets
        
        self.init_ui()

    def init_ui(self):
        """Initialize the UI components for this group."""
        layout = QGridLayout(self)

        # Appliance Type
        input_type_txt = QLabel("Select Appliance Type")
        self.input_type_combo = QComboBox()
        self.input_type_combo.addItem("Select Appliance...")
        self.input_type_combo.model().item(0).setEnabled(False)
        self.input_type_combo.addItems(sorted(self.appliance_presets.keys()))
        self.input_type_combo.setCurrentIndex(0)
        self.input_type_combo.setEditable(False)
        self.input_type_combo.currentIndexChanged.connect(self.on_appliance_selected)

        # Power
        power_label = QLabel("Power Consumption")
        power_label_unit = QLabel("Watts (W)")
        self.power_input = QComboBox()
        self.power_input.setEditable(True)
        self.power_input.addItems(["10W","75W","100W", "150W","200W", "300W", "500W", "750W", "1000W", "1200W", "1500W"])
        self.power_input.setPlaceholderText("Select or enter power consumption")

        # Usage
        usage_label = QLabel("Use per day")
        usage_label_unit = QLabel("Hours")
        self.usage_input = QComboBox()
        self.usage_input.setEditable(True)
        self.usage_input.addItems(["0.5", "1", "2", "3", "4", "5", "6", "8", "10", "12", "16", "24"])
        self.usage_input.setPlaceholderText("Select or enter hours")

        # Rate
        rate_label = QLabel("Electricity Rate")
        rate_label_unit = QLabel("₱/kWh")
        self.rate_input = QComboBox()
        self.rate_input.setEditable(True)
        self.rate_input.addItems(["10", "12", "15", "18", "20"])
        self.rate_input.setPlaceholderText("Select or enter rate")

        # Added Appliances List
        appliances_label = QLabel("Appliances Added")
        self.appliances_added_combo = QComboBox()
        self.appliances_added_combo.setEditable(False)
        self.appliances_added_combo.setPlaceholderText("Selected appliances will appear here")

        # Add to layout
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
        layout.addWidget(appliances_label, 4, 0)
        layout.addWidget(self.appliances_added_combo, 4, 1, 1, 2)
        
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 0)

    def on_appliance_selected(self, index):
        """Internal slot to fill defaults when an appliance is selected."""
        if index <= 0:
            self.reset_input_fields()
            return
            
        appliance_name = self.input_type_combo.itemText(index)
        preset = self.appliance_presets.get(appliance_name)
        if preset:
            self.power_input.setEditText(str(preset["watts"]))
            self.usage_input.setEditText(str(preset["usage"]))
            self.rate_input.setEditText(str(preset["rate"]))

    def get_input_values(self):
        """Returns the current values from the input fields."""
        return {
            "appliance": self.input_type_combo.currentText(),
            "power": self.power_input.currentText(),
            "usage": self.usage_input.currentText(),
            "rate": self.rate_input.currentText()
        }
        
    def get_added_appliances(self):
        """Returns a list of all appliances added to the combo box."""
        return [self.appliances_added_combo.itemText(i) for i in range(self.appliances_added_combo.count())]

    def add_appliance_to_list(self, entry_text):
        """Adds a new text entry to the appliances list."""
        self.appliances_added_combo.addItem(entry_text)

    def remove_selected_appliance(self):
        """Removes the currently selected appliance from the list. Returns False if none selected."""
        index = self.appliances_added_combo.currentIndex()
        if index >= 0:
            self.appliances_added_combo.removeItem(index)
            return True
        return False

    def reset_input_fields(self):
        """Resets only the top input fields, not the appliance list."""
        self.input_type_combo.setCurrentIndex(0)
        self.power_input.setEditText("")
        self.usage_input.setEditText("")
        self.rate_input.setEditText("")

    def reset_all(self):
        """Resets all fields in this group, including the appliance list."""
        self.reset_input_fields()
        self.appliances_added_combo.clear()


class ButtonGroups(QGroupBox):
    """
    A QGroupBox that contains the main action buttons and emits signals.
    """
    # Define signals that will be emitted when buttons are clicked
    add_clicked = pyqtSignal()
    remove_clicked = pyqtSignal()
    calculate_clicked = pyqtSignal()
    reset_clicked = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        """Initialize the UI components for this group."""
        layout = QHBoxLayout(self)

        add_btn = QPushButton("Add Appliance")
        del_btn = QPushButton("Remove Appliance")
        calc_btn = QPushButton("Calculate")
        reset_btn = QPushButton("Reset")

        # Connect internal button clicks to the class signals
        add_btn.clicked.connect(self.add_clicked)
        del_btn.clicked.connect(self.remove_clicked)
        calc_btn.clicked.connect(self.calculate_clicked)
        reset_btn.clicked.connect(self.reset_clicked)

        layout.addWidget(add_btn)
        layout.addWidget(del_btn)
        layout.addWidget(calc_btn)
        layout.addWidget(reset_btn)


class OutputGroup(QGroupBox):
    """
    A QGroupBox that displays the calculation results.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        """Initialize the UI components for this group."""
        layout = QGridLayout(self)

        self.daily_cost_label = QLabel("Daily Cost: ₱0.00")
        self.monthly_cost_label = QLabel("Monthly Estimate: ₱0.00")
        
        # Use objectName to allow styling from the main stylesheet
        self.daily_cost_label.setObjectName("outputLabel")
        self.monthly_cost_label.setObjectName("outputLabel")

        layout.addWidget(self.daily_cost_label, 0, 0)
        layout.addWidget(self.monthly_cost_label, 1, 0)

    def update_costs(self, daily_cost, monthly_cost):
        """Updates the cost labels with formatted strings."""
        self.daily_cost_label.setText(f"Daily Cost: ₱{daily_cost:.2f}")
        self.monthly_cost_label.setText(f"Monthly Estimate: ₱{monthly_cost:.2f}")

    def reset(self):
        """Resets the cost labels to zero."""
        self.daily_cost_label.setText("Daily Cost: ₱0.00")
        self.monthly_cost_label.setText("Monthly Estimate: ₱0.00")