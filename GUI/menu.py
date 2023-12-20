# menu.py
# Menu bar for MaCAN application
# References version information from version.py
# Adds "Hilfe" action to open Hilfe.html

import PySide6.QtWidgets
import QUrl
import os
from version import app_name, version, author

class MenuBar(PySide6.QtWidgets.QMenuBar):
    def __init__(self, parent=None):
        super(MenuBar, self).__init__(parent)
        self.initUI()

    def initUI(self):
        # File menu actions
        file_menu = self.addMenu("File")

        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_configuration)
        file_menu.addAction(open_action)

        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_configuration)
        file_menu.addAction(save_action)

        # Help menu actions
        help_menu = self.addMenu("Help")

        help_action = QAction("Help", self)
        help_action.triggered.connect(self.open_help)
        help_menu.addAction(help_action)

        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

        hilfe_action = QAction("Hilfe", self)
        hilfe_action.triggered.connect(self.show_hilfe)
        help_menu.addAction(hilfe_action)

    def open_configuration(self):
        # Logic to open and load configuration
        pass

    def save_configuration(self):
        # Logic to save current configuration
        pass

    def open_help(self):
        # Logic to open help documentation
        pass

    def show_about(self):
        about_message = f"{app_name}\nVersion: {version}\nAuthor: {author}"
        PySide6.QtWidgets.QMessageBox.information(self, f"About {app_name}", about_message, PySide6.QtWidgets.QMessageBox.Ok)

    def show_hilfe(self):
        # Assuming the 'Doc' folder is in the current working directory of the application
        hilfe_path = os.path.join(os.getcwd(), 'Doc', 'Hilfe.html')
        QDesktopServices.openUrl(QUrl.fromLocalFile(hilfe_path))
