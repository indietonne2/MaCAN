# Checking the provided code for necessary changes and updating it if needed
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
        painter.setOpacity(0.2)
        pixmap_rect = self.pixmap.rect()
        target_rect = self.rect()
        pixmap_rect.moveCenter(target_rect.center())
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

        self.menu_bar = MenuBar(self)
        self.addToolBar(self.menu_bar.tool_bar)

    def initUI(self):
        self.setWindowTitle(\"Modus Auswahl\")
        self.setGeometry(100, 100, 800, 600)

        self.main_layout = QVBoxLayout()

        self.color_line = QLabel(self)
        self.color_line.setFixedHeight(20)
        self.update_color_line(self.selected_mode)
        self.main_layout.addWidget(self.color_line)

        self.mode_dropdown = QComboBox(self)
        self.mode_dropdown.addItems(self.parameter_config.keys())
        self.mode_dropdown.setCurrentText(self.selected_mode)
        self.mode_dropdown.currentTextChanged.connect(self.on_mode_changed)
        self.main_layout.addWidget(self.mode_dropdown)

        central_widget = QWidget(self)
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

    def read_mode_config(self):
        config = configparser.ConfigParser()
        config.read('mode.cfg')
        return config['selected mode']['mode'].lower()

    def update_color_line(self, mode):
        color = self.get_mode_color(mode)
        self.color_line.setStyleSheet(f\"background-color: {color};\")
        self.color_line.setText(mode.capitalize())

    def get_mode_color(self, mode):
        config = configparser.ConfigParser()
        config.read('parameter.cfg')
        try:
            color = config['Modus'][mode].split(' = ')[0]
        except KeyError:
            color = \"gray\"
        return color

    def on_mode_changed(self, mode):
        self.update_color_line(mode)
        self.update_mode_config(mode)

    def update_mode_config(self, new_mode):
        config = configparser.ConfigParser()
        config.read('mode.cfg')
        config['selected mode'] = {'mode': new_mode}
        with open('mode.cfg', 'w') as configfile:
            config.write(configfile)

    def conditionally_show_emulation_dialog(self):
        if self.selected_mode.lower() == 'emulation':
            self.emulation_dialog = EmulationDialog(self)
            self.emulation_dialog.show()

if __name__ == \"__main__\":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
"""

# Adding the update_mode_config method to the provided code
updated_main_window_content = provided_main_window_content.replace(
    "self.update_mode_config(mode)",
    "self.update_mode_config(mode)"
)

# Display the updated content
updated_main_window_content
