# start_screen.py
# Start screen module for MaCAN application
# References version information from version.py

from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
from version import app_name, version, author

class StartScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Label for welcome message
        self.welcome_label = QLabel(f"Willkommen bei {app_name}.\n{app_name} ist eine CAN-Bus Software zur Simulation oder Emulation von CAN-Bus-Signalen.")
        layout.addWidget(self.welcome_label)

        # Buttons to navigate to different pages
        self.simulation_button = QPushButton("Simulation")
        self.emulation_button = QPushButton("Emulation")
        self.flash_button = QPushButton("Flash")

        layout.addWidget(self.simulation_button)
        layout.addWidget(self.emulation_button)
        layout.addWidget(self.flash_button)

        self.setLayout(layout)

        # Connect buttons to their functionalities
        self.simulation_button.clicked.connect(self.open_simulation)

    def open_simulation(self):
        # Logic to open the Simulation page
        pass
