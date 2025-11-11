# calculator_app.py

# importing necessary modules
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, 
    QMessageBox, QSpacerItem, QSizePolicy
)
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, Qt

# Import modular components (encapsulated in their own files)
from constants import APPLIANCE_PRESETS
from styles import MODERN_STYLESHEET
from ui_widgets import InputGroup, ButtonGroups, OutputGroup
import utils

class MainWindow(QMainWindow):
    """
    The main application window.
    It orchestrates the input, button, and output widgets.
    """
    def __init__(self):
        super().__init__()

        self.current_user = "default_user"  # Example user
        self.setWindowTitle("Watt's my Electricity Bill?")
        self.setWindowOpacity(0)
        
        self.init_ui()
        
    def init_ui(self):
        # Initialize the main UI layout and components.
        
        # Central widget and layout
        central = QWidget()
        central.setObjectName("centralWidget")  # For stylesheet targeting
        self.main_layout = QVBoxLayout(central)
        self.setCentralWidget(central)
        
        # Apply the imported stylesheet
        self.setStyleSheet(MODERN_STYLESHEET)
        
        # Create widget groups from our custom classes
        self.input_group = InputGroup(APPLIANCE_PRESETS)
        self.button_group = ButtonGroups()
        self.output_group = OutputGroup()

        # Add widgets to the main layout
        self.main_layout.addWidget(self.input_group)
        self.main_layout.addWidget(self.button_group)
        self.main_layout.addWidget(self.output_group)

        # Spacer to push all widgets to the top
        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.main_layout.addSpacerItem(spacer)

        # Connect signals from button group to handler methods
        self.button_group.add_clicked.connect(self.handle_add_appliance)
        self.button_group.remove_clicked.connect(self.handle_remove_appliance)
        self.button_group.calculate_clicked.connect(self.handle_calculate)
        self.button_group.reset_clicked.connect(self.handle_reset)

    def showEvent(self, event):
        """Override showEvent to trigger the fade-in animation."""
        super().showEvent(event)
        self.fade_in()

    def fade_in(self):
        """Animates the window opacity from 0 to 1."""
        try:
            self.anim = QPropertyAnimation(self, b"windowOpacity")
            self.anim.setDuration(1000)
            self.anim.setStartValue(0)
            self.anim.setEndValue(1)
            self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
            self.anim.start()
        except Exception as e:
            # Fallback for environments where opacity animation fails
            print(f"Animation failed: {e}. Setting opacity to 1.")
            self.setWindowOpacity(1)

    # --- Signal Handlers ---

    def handle_add_appliance(self):
        """Handles the 'Add Appliance' button click."""
        values = self.input_group.get_input_values()
        
        if values["appliance"] == "Select Appliance..." or not (values["power"] and values["usage"] and values["rate"]):
            QMessageBox.warning(self, "Missing Input", "Please select an appliance and fill in all fields.")
            return

        try:
            # Validate numeric inputs before adding
            float(values["power"].replace("W", "").strip())
            float(values["usage"].strip())
            float(values["rate"].strip())
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter valid numeric values for power, usage, and rate.")
            return

        # Format the entry string
        entry = f"{values['appliance']} - {values['power']} x {values['usage']}hr @ {values['rate']}₱/kWh"
        self.input_group.add_appliance_to_list(entry)
        
        # Reset the input fields for the next entry
        self.input_group.reset_input_fields()

    def handle_remove_appliance(self):
        """Handles the 'Remove Appliance' button click."""
        if not self.input_group.remove_selected_appliance():
            QMessageBox.information(self, "No Selection", "Please select an appliance to remove from the list.")

    def handle_calculate(self):
        """
        Handles the 'Calculate' button click.
        Fetches data, calls utility function, and updates the output.
        """
        appliance_list = self.input_group.get_added_appliances()
        
        if not appliance_list:
            QMessageBox.information(self, "No Appliances", "Please add at least one appliance to calculate.")
            return

        try:
            total_cost = utils.calculate_total_cost(appliance_list)
        except ValueError as e:
            QMessageBox.warning(self, "Calculation Error", str(e))
            return
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")
            return

        monthly_cost = total_cost * 30
        
        # Display results in a message box
        QMessageBox.information(self, "Estimated Cost",
            f"Your estimated daily electricity cost is ₱{total_cost:.2f}\n"
            f"Monthly estimate: ₱{monthly_cost:.2f}"
        )
        
        # Update the output labels
        self.output_group.update_costs(total_cost, monthly_cost)

        # Save to history
        if self.current_user:
            utils.save_calculation_history(
                self.current_user, 
                appliance_list, 
                total_cost, 
                monthly_cost
            )

    def handle_reset(self):
        """Handles the 'Reset' button click."""
        self.input_group.reset_all()
        self.output_group.reset()
