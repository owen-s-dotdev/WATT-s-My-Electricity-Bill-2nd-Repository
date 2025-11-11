"""
Main application window (the "Controller").

This file assembles the UI widgets, connects signals to logic,
and manages the application's state.
"""
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QMessageBox, QSpacerItem, QSizePolicy
)
from PyQt6.QtCore import QSize, QPropertyAnimation, QEasingCurve, Qt, QDate

# --- Local Module Imports ---
# --- REMOVED: from styles import MODERN_STYLESHEET ---
from app_data import APPLIANCE_PRESETS
from ui_widgets import InputWidget, ButtonWidget, OutputWidget
from logic import calculate_total_cost, save_history

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.current_user = None # Can be set by your login/main driver
        self.setWindowTitle("Watt's my Electricity Bill?")
        self.setWindowOpacity(0)

        # --- Main Layout Setup ---
        central = QWidget()
        central.setObjectName("centralWidget") 
        self.main_layout = QVBoxLayout(central)
        self.setCentralWidget(central)
        
        # --- REMOVED STYLESHEET LOGIC ---
        # app_instance = QApplication.instance()
        # if app_instance:
        #     app_instance.setStyleSheet(MODERN_STYLESHEET)
        
        # --- Instantiate UI Widgets ---
        self.input_widget = InputWidget(APPLIANCE_PRESETS)
        self.button_widget = ButtonWidget()
        self.output_widget = OutputWidget()

        # --- Add Widgets to Main Layout ---
        self.main_layout.addWidget(self.input_widget)
        self.main_layout.addWidget(self.button_widget)
        self.main_layout.addWidget(self.output_widget)

        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.main_layout.addSpacerItem(spacer)

        # --- Connect Signals ---
        self.input_widget.input_type_combo.currentIndexChanged.connect(self.on_appliance_selected)
        
        self.button_widget.add_btn.clicked.connect(self.handle_add_appliance)
        self.button_widget.del_btn.clicked.connect(self.handle_remove_appliance)
        self.button_widget.calc_btn.clicked.connect(self.handle_calculate)
        self.button_widget.reset_btn.clicked.connect(self.handle_reset)

    def fade_in(self):
        """Fades the window in on show."""
        self.anim = QPropertyAnimation(self, b"windowOpacity")
        self.anim.setDuration(1000)
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.anim.start()

    # --- Signal Handlers (Slots) ---

    def handle_add_appliance(self):
        """
        Validates input and adds the configured appliance to the list.
        """
        appliance = self.input_widget.input_type_combo.currentText()
        power = self.input_widget.power_input.currentText()
        usage = self.input_widget.usage_input.currentText()
        rate = self.input_widget.rate_input.currentText()

        if appliance == "Select Appliance..." or not (power and usage and rate):
            QMessageBox.warning(self, "Missing Input", "Please select an appliance and fill in all fields.")
            return

        # --- Validation ---
        try:
            float(power.replace("W", "").strip())
            float(usage.strip())
            float(rate.strip())
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter valid numeric values for power, usage, and rate.")
            return

        # --- Add to List and Reset Inputs ---
        entry = f"{appliance} - {power} x {usage}hr @ {rate}₱/kWh"
        self.input_widget.appliances_added_combo.addItem(entry)
        
        # Reset only the input fields, not the whole widget
        self.input_widget.input_type_combo.setCurrentIndex(0)
        self.input_widget.power_input.setEditText("")
        self.input_widget.usage_input.setEditText("")
        self.input_widget.rate_input.setEditText("")

    def handle_remove_appliance(self):
        """
        Removes the currently selected appliance from the list.
        """
        index = self.input_widget.appliances_added_combo.currentIndex()
        if index >= 0:
            self.input_widget.appliances_added_combo.removeItem(index)
        else:
            QMessageBox.information(self, "No Selection", "Please select an appliance to remove.")

    def handle_calculate(self):
        """
        Calculates the total cost by calling the external logic function
        and updates the UI.
        """
        combo = self.input_widget.appliances_added_combo
        if combo.count() == 0:
            QMessageBox.information(self, "No Appliances", "Please add at least one appliance to calculate.")
            return

        items = [combo.itemText(i) for i in range(combo.count())]
        
        # --- Call Calculation Logic ---
        total_cost, monthly_cost, error = calculate_total_cost(items)
        
        if error:
            QMessageBox.warning(self, "Calculation Error", error)
            return

        # --- Update UI ---
        QMessageBox.information(self, "Estimated Cost",
            f"Your estimated daily electricity cost is ₱{total_cost:.2f}\n"
            f"Monthly estimate: ₱{monthly_cost:.2f}"
        )
        self.output_widget.set_costs(total_cost, monthly_cost)

        # --- Save to History ---
        if self.current_user:
            calculation_date = self.input_widget.date_input.date().toString("yyyy-MM-dd") 
            save_history(self.current_user, calculation_date, items, total_cost, monthly_cost)

    def fill_appliance_defaults(self, appliance_name):
        """
        Populates input fields based on the selected appliance preset.
        """
        preset = APPLIANCE_PRESETS.get(appliance_name)
        if preset:
            self.input_widget.power_input.setEditText(str(preset["watts"]))
            self.input_widget.usage_input.setEditText(str(preset["usage"]))
            self.input_widget.rate_input.setEditText(str(preset["rate"]))
    
    def on_appliance_selected(self, index):
        """
        Triggered when the user selects a different appliance.
        """
        if index <= 0:
            # "Select Appliance..." was chosen, clear fields
            self.input_widget.power_input.setEditText("")
            self.input_widget.usage_input.setEditText("")
            self.input_widget.rate_input.setEditText("")
            return
            
        appliance_name = self.input_widget.input_type_combo.itemText(index)
        self.fill_appliance_defaults(appliance_name)
    
    def handle_reset(self):
        """
        Resets all UI widgets to their default state.
        """
        self.input_widget.reset()
        self.output_widget.reset()