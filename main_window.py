from PySide6.QtWidgets import QMainWindow, QLabel, QApplication, QVBoxLayout, QWidget, QComboBox
from PySide6.QtGui import QColor, QPixmap, QPainter, QPaintEvent
from PySide6.QtCore import Qt
import sys
import os
import configparser

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.config = configparser.ConfigParser()
        self.modus_config = self.read_config()
        self.background_image = QLabel(self)  # Hintergrundbild Label
        self.color_bar = QLabel(self)  # Farbbalken
        self.initUI()

    def read_config(self):
        self.config.read('parameter.cfg')
        return self.config['Modus']

    def initUI(self):
        self.setWindowTitle("Modus Auswahl")
        self.setGeometry(100, 100, 800, 600)

        self.update_background_image()

        layout = QVBoxLayout()

        # Farbbalken
        self.color_bar.setFixedHeight(20)  # Setzt die Höhe des Farbbalkens auf 20 Pixel
        self.color_bar.setAlignment(Qt.AlignCenter)  # Text zentrieren
        layout.addWidget(self.color_bar)

        # Auswahlfeld
        self.combo_box = QComboBox(self)
        self.fill_combo_box()
        self.combo_box.currentTextChanged.connect(self.update_color_bar_and_text)  # Aktualisieren der Farbe und Text bei Auswahl
        layout.addWidget(self.combo_box, 0, Qt.AlignTop)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def fill_combo_box(self):
        for key in self.modus_config.keys():
            self.combo_box.addItem(key)

    def update_color_bar_and_text(self, text):
        color_name = self.modus_config.get(text, "Rot")
        color_map = {"Rot": QColor(255, 0, 0), "Grün": QColor(0, 255, 0), "Blau": QColor(0, 0, 255), "Orange": QColor(255, 165, 0)}
        color = color_map[color_name]
        text_color = "white" if self.is_color_dark(color) else "black"
        self.color_bar.setStyleSheet(f"background-color: {color.name()}; color: {text_color};")
        self.color_bar.setText(text)  # Setzt den ausgewählten Modus als Text im Farbbalken

    def is_color_dark(self, color: QColor):
        # Berechnung der Luminanz
        luminance = (0.299 * color.red() + 0.587 * color.green() + 0.114 * color.blue()) / 255
        return luminance < 0.5

    def update_background_image(self):
        pixmap = QPixmap(os.path.join('resources', 'background.png'))
        painter = QPainter(pixmap)
        painter.setOpacity(0.5)  # Setzt die Transparenz auf 50%
        painter.drawPixmap(pixmap.rect(), pixmap)
        painter.end()
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
