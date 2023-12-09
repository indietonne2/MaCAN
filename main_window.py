import sys
import os
import importlib
import configparser
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication, QVBoxLayout, QWidget, QComboBox, QStackedWidget, QDialog
from PySide6.QtGui import QColor, QPixmap, QPainter
from PySide6.QtCore import Qt
from config import Config
from menu_bar import MenuBar
from gui.emulation_ui import Ui_Dialog

class BackgroundWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pixmap = QPixmap(os.path.join('resources', 'background.png'))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setOpacity(0.2)  # Set transparency
        pixmap_rect = self.pixmap.rect()
        target_rect = self.rect()
        pixmap_rect.moveCenter(target_rect.center())  # Center the background image
        painter.drawPixmap(target_rect, self.pixmap, pixmap_rect)
        painter.end()

class EmulationDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.config = Config()
        self.parameter_config = self.config.read_parameter_config()
        self.selected_mode = self.read_mode_config()
        self.initUI()
        self.conditionally_show_emulation_dialog()

        # Create an instance of MenuBar and add it to the main window
        self.menu_bar = MenuBar(self)
        self.addToolBar(self.menu_bar.tool_bar)

    def initUI(self):
        self.setWindowTitle("Modus Auswahl")
        self.setGeometry(100, 100, 800, 600)

        self.background_widget = BackgroundWidget(self)
        self.setCentralWidget(self.background_widget)

        self.main_layout = QVBoxLayout()
        self.background_widget.setLayout(self.main_layout)

        # Create the colored line
        self.color_line = QLabel(self)
        self.color_line.setFixedHeight(20)
        self.update_color_line(self.selected_mode)
        self.main_layout.addWidget(self.color_line)

        # Create the mode dropdown
        self.mode_dropdown = QComboBox(self)
        self.mode_dropdown.addItems(self.parameter_config.keys())
        self.mode_dropdown.setCurrentText(self.selected_mode)
        self.mode_dropdown.currentTextChanged.connect(self.on_mode_changed)
        self.main_layout.addWidget(self.mode_dropdown)

        # Other UI elements setup...

    def read_mode_config(self):
        config = configparser.ConfigParser()
        config.read('mode.cfg')
        # Convert mode to a consistent case, e.g., all lowercase
        return config['selected mode']['mode'].lower()

    def get_mode_color(self, mode):
        # Convert mode to the case used in parameter.cfg, e.g., capitalize the first letter
        mode_formatted = mode.capitalize()
        return self.parameter_config.get('Modus', mode_formatted, fallback="gray")

    def update_color_line(self, mode):
        color = self.get_mode_color(mode)
        self.color_line.setStyleSheet(f"background-color: {color};")
        self.color_line.setText(mode.capitalize())

    def on_mode_changed(self, mode):
        self.update_color_line(mode)
        self.update_mode_config(mode)
        # Additional logic for mode change...

    def conditionally_show_emulation_dialog(self):
        # Check if the selected mode is 'Emulation'
        if self.selected_mode.lower() == 'emulation':
            self.emulation_dialog = EmulationDialog(self)
            self.emulation_dialog.show()

    # Rest of the MainWindow class methods...

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
