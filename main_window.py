import configparser
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication, QVBoxLayout, QWidget, QComboBox
from PySide6.QtGui import QColor, QPixmap, QPainter, QPaintEvent
from PySide6.QtCore import Qt
import sys
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.parameter_config = configparser.ConfigParser()
        self.mode_config = configparser.ConfigParser()
        self.read_parameter_config()
        self.initUI()
        self.read_mode_config()  # Liest den initialen Modus aus mode.cfg

    def read_parameter_config(self):
        self.parameter_config.read('parameter.cfg')
        return self.parameter_config['Modus']

    def read_mode_config(self):
        self.mode_config.read('mode.cfg')
        selected_mode = self.mode_config.get('selected mode', 'mode', fallback=None)
        if selected_mode and selected_mode in self.parameter_config:
            self.combo_box.setCurrentText(selected_mode)
            self.update_color_bar_and_text(selected_mode)
        else:
            first_mode = next(iter(self.parameter_config['Modus']))
            self.combo_box.setCurrentText(first_mode)
            self.update_color_bar_and_text(first_mode)

    def write_mode_config(self, mode):
        self.mode_config['selected mode'] = {'mode': mode}
        with open('mode.cfg', 'w') as configfile:
            self.mode_config.write(configfile)

    def initUI(self):
        self.setWindowTitle("Modus Auswahl")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # Farbbalken
        self.color_bar = QLabel(self)
        self.color_bar.setFixedHeight(20)
        self.color_bar.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.color_bar)

        # Auswahlfeld
        self.combo_box = QComboBox(self)
        self.fill_combo_box()
        self.combo_box.currentTextChanged.connect(self.on_mode_selected)
        layout.addWidget(self.combo_box, 0, Qt.AlignTop)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.update_background_image()

    def fill_combo_box(self):
        for key in self.parameter_config['Modus']:
            self.combo_box.addItem(key)

    def on_mode_selected(self, text):
        self.update_color_bar_and_text(text)
        self.write_mode_config(text)

    def update_color_bar_and_text(self, text):
        color_name = self.parameter_config['Modus'].get(text, "Rot")
        color_map = {
            "Rot": QColor(255, 0, 0),
            "Grün": QColor(0, 255, 0),
            "Blau": QColor(0, 0, 255),
            "Orange": QColor(255, 165, 0)
        }
        color = color_map.get(color_name, QColor(255, 0, 0))
        text_color = "white" if self.is_color_dark(color) else "black"
        self.color_bar.setStyleSheet(f"background-color: {color.name()}; color: {text_color};")
        self.color_bar.setText(text)

    def is_color_dark(self, color: QColor):
        luminance = (0.299 * color.red() + 0.587 * color.green() + 0.114 * color.blue()) / 255
        return luminance < 0.5

    def update_background_image(self):
        pixmap = QPixmap(os.path.join('resources', 'background.png'))
        painter = QPainter(pixmap)
        painter.setOpacity(0.5)
        painter.drawPixmap(pixmap.rect(), pixmap)
        painter.end()
        self.background_image = QLabel(self)
        self.background_image.setPixmap(pixmap)
        self.background_image.setGeometry(0, self.color_bar.height(), self.width(), self.height() - self.color_bar.height())

    def resizeEvent(self, event: QPaintEvent):
        self.update_background_image()
        super().resizeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
