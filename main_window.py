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
        self.color_bar.setStyleSheet("background-color: red;")  # Standardfarbe
        layout.addWidget(self.color_bar)

        # Auswahlfeld
        self.combo_box = QComboBox(self)
        self.fill_combo_box()
        self.combo_box.currentTextChanged.connect(self.update_color_bar)  # Aktualisieren der Farbe bei Auswahl
        layout.addWidget(self.combo_box, 0, Qt.AlignTop)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def fill_combo_box(self):
        for key in self.modus_config.keys():
            self.combo_box.addItem(key)

    def update_color_bar(self, text):
        color = self.modus_config.get(text, "Rot")
        color_map = {"Rot": QColor(255, 0, 0), "Grün": QColor(0, 255, 0), "Blau": QColor(0, 0, 255), "Orange": QColor(255, 165, 0)}
        self.color_bar.setStyleSheet(f"background-color: {color_map[color].name()};")

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
