import sys
import os
import importlib
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication, QVBoxLayout, QWidget, QComboBox, QStackedWidget
from PySide6.QtGui import QColor, QPixmap, QPainter
from PySide6.QtCore import Qt
from config import Config
from menu_bar import MenuBar

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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.config = Config()
        self.parameter_config = self.config.read_parameter_config()
        self.initUI()
        selected_mode = self.config.read_mode_config()
        self.handle_mode_selection(selected_mode)

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

        self.create_persistent_widgets()

        # Bereich für modusspezifische Widgets
        self.stacked_widget = QStackedWidget(self)
        self.main_layout.addWidget(self.stacked_widget)

    def create_persistent_widgets(self):
        # Farbbalken
        self.color_bar = QLabel(self)
        self.color_bar.setFixedHeight(20)
        self.color_bar.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.color_bar)

        # ComboBox
        self.combo_box = QComboBox(self)
        self.fill_combo_box()
        self.combo_box.currentTextChanged.connect(self.update_color_bar_and_text)
        self.main_layout.addWidget(self.combo_box)

    def fill_combo_box(self):
        for key in self.parameter_config['Modus']:
            mode_name = key.split('=')[0].strip()
            self.combo_box.addItem(mode_name.lower())

    def update_color_bar_and_text(self, text):
        mode_info = self.parameter_config['Modus'].get(text.upper())
        if mode_info:
            color_name, python_file_name = [item.strip() for item in mode_info.split('=')]
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

            self.load_and_execute_python_file(python_file_name)

    def is_color_dark(self, color: QColor):
        luminance = (0.299 * color.red() + 0.587 * color.green() + 0.114 * color.blue()) / 255
        return luminance < 0.5

    def handle_mode_selection(self, selected_mode):
        if selected_mode and selected_mode.upper() in self.parameter_config['Modus']:
            self.combo_box.setCurrentText(selected_mode.lower())
            self.update_color_bar_and_text(selected_mode.lower())
        else:
            first_mode = next(iter(self.parameter_config['Modus']))
            self.combo_box.setCurrentText(first_mode.lower())
            self.update_color_bar_and_text(first_mode.lower())

    def load_and_execute_python_file(self, python_file_name):
        module_name = os.path.splitext(python_file_name)[0]
        try:
            module = importlib.import_module(module_name)
            if hasattr(module, 'SimulationWidget'):
                simulation_widget = module.SimulationWidget()
                self.stacked_widget.addWidget(simulation_widget)
                self.stacked_widget.setCurrentWidget(simulation_widget)
            self.setWindowTitle(f"Module: {module_name}")
        except ImportError:
            print(f"Failed to import module {module_name}.")


    def restore_initial_state(self):
        self.stacked_widget.setCurrentIndex(-1)
        self.setWindowTitle("Modus Auswahl")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
