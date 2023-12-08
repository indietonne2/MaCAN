import sys
import os
import configparser
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication, QVBoxLayout, QWidget, QComboBox, QLineEdit
from PySide6.QtGui import QColor, QPixmap, QPainter, QPaintEvent
from PySide6.QtCore import Qt

# Import MenuBar from the menu_bar.py file
from menu_bar import MenuBar

class BackgroundWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pixmap = QPixmap(os.path.join('resources', 'background.png'))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setOpacity(0.5)  # Set transparency
        pixmap_rect = self.pixmap.rect()
        target_rect = self.rect()
        pixmap_rect.moveCenter(target_rect.center())  # Center the background image
        painter.drawPixmap(target_rect, self.pixmap, pixmap_rect)
        painter.end()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.parameter_config = configparser.ConfigParser()
        self.mode_config = configparser.ConfigParser()
        self.read_parameter_config()
        self.initUI()
        self.read_mode_config()

        # Create an instance of MenuBar and add it to the main window
        self.menu_bar = MenuBar(self)
        self.addToolBar(self.menu_bar.tool_bar)

    def read_parameter_config(self):
        self.parameter_config.read('parameter.cfg')
        return self.parameter_config['Modus']

    def read_mode_config(self):
        self.mode_config.read('mode.cfg')
        selected_mode = self.mode_config.get('selected mode', 'mode', fallback=None)
        if selected_mode and selected_mode.upper() in self.parameter_config['Modus']:
            self.combo_box.setCurrentText(selected_mode.lower())
            self.update_color_bar_and_text(selected_mode.lower())
        else:
            first_mode = next(iter(self.parameter_config['Modus']))
            self.combo_box.setCurrentText(first_mode.lower())
            self.update_color_bar_and_text(first_mode.lower())

    def write_mode_config(self, mode):
        self.mode_config['selected mode'] = {'mode': mode.upper()}
        with open('mode.cfg', 'w') as configfile:
            self.mode_config.write(configfile)

    def initUI(self):
        self.setWindowTitle("Modus Auswahl")
        self.setGeometry(100, 100, 800, 600)

        # Central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Main layout
        main_layout = QVBoxLayout(central_widget)

        # Color Bar
        self.color_bar = QLabel(self)
        self.color_bar.setFixedHeight(20)
        self.color_bar.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.color_bar)

        # Combo Box
        self.combo_box = QComboBox(self)
        self.fill_combo_box()
        self.combo_box.currentTextChanged.connect(self.update_color_bar_and_text)
        main_layout.addWidget(self.combo_box)

        # Single Line Edit
        self.line_edit = QLineEdit(self)
        main_layout.addWidget(self.line_edit)

        # Background Widget
        self.background_widget = BackgroundWidget(self)
        main_layout.insertWidget(0, self.background_widget)

    def fill_combo_box(self):
        for key in self.parameter_config['Modus']:
            self.combo_box.addItem(key.lower())

    def update_color_bar_and_text(self, text):
        color_name = self.parameter_config['Modus'].get(text.upper(), "Rot")
        color_map = {
            "Rot": QColor(255, 0, 0),
            "Grün": QColor(0, 255, 0),
            "Blau": QColor(0, 0, 255),
            "Orange": QColor(255, 165, 0)
        }
        color = color_map.get(color_name, QColor(255, 0, 0))
        text_color = "white" if self.is_color_dark(color) else "black"
        self.color_bar.setStyleSheet(f"background-color: {color.name()}; color: {text_color};")
        self.color_bar.setText(text.lower())

    def is_color_dark(self, color: QColor):
        luminance = (0.299 * color.red() + 0.587 * color.green() + 0.114 * color.blue()) / 255
        return luminance < 0.5

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
