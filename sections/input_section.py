from PyQt6.QtWidgets import QGroupBox, QGridLayout, QLabel, QComboBox

class InputSection(QGroupBox):
    def __init__(self, appliance_presets):
        super().__init__("Appliance Input")
        self.presets = appliance_presets
        self.inputs = {}
        self.setStyleSheet(self.groupbox_style())
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()
        self.setLayout(layout)

        fields = [
            ("Select Appliance Type", "combo", sorted(self.presets.keys()), False),
            ("Power Consumption", "combo", ["10W","75W","100W","150W","200W","300W","500W","750W","1000W","1200W","1500W"], True),
            ("Use per day", "combo", ["0.5","1","2","3","4","5","6","8","10","12","16","24"], True),
            ("Electricity Rate", "combo", ["10","12","15","18","20"], True),
            ("Appliances Added", "combo", [], False)
        ]

        for i, (label_text, widget_type, items, editable) in enumerate(fields):
            label = QLabel(label_text)
            combo = QComboBox()
            combo.setEditable(editable)
            if items: combo.addItems(items)
            self.inputs[label_text] = combo
            layout.addWidget(label, i, 0)
            layout.addWidget(combo, i, 1)

        # Disable first item for appliance type
        combo = self.inputs["Select Appliance Type"]
        combo.insertItem(0, "Select Appliance...")
        combo.setCurrentIndex(0)
        combo.model().item(0).setEnabled(False)

    @staticmethod
    def groupbox_style():
        return """
            QGroupBox {
                background-color: #ffffff;
                color: #333333;
                font-weight: bold;
                border: 2px solid #cc6600;
                border-radius: 8px;
                margin-top: 10px;
            }
            QGroupBox:title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 0 3px;
            }
        """
