import configparser
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication, QVBoxLayout, QWidget, QPushButton, QSpacerItem, QSizePolicy
from PySide6.QtGui import QColor, QPixmap, QPainter, QPaintEvent
from PySide6.QtCore import Qt, Slot
import sys
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.modus_config = self.read_config()
        self.background_image = QLabel(self)  # Hintergrundbild Label
        self.initUI()

    def read_config(self):
        config = configparser.ConfigParser()
        config.read('parameter.cfg')
        return config['Modus']

    def initUI(self):
        modus = "Live"
        farbe = self.modus_config.get(modus, "Rot")

        self.setWindowTitle(f"{modus} Modus")
        self.setGeometry(100, 100, 800, 600)

        color_map = {"Rot": QColor(255, 0, 0), "Grün": QColor(0, 255, 0), "Blau": QColor(0, 0, 255), "Orange": QColor(255, 165, 0)}

        modus_label = QLabel(modus, self)
        modus_label.setAlignment(Qt.AlignCenter)
        modus_label.setStyleSheet(f"background-color: {color_map[farbe].name()};")
        modus_label.setGeometry(0, 0, self.width(), 30)

        self.update_background_image()

        layout = QVBoxLayout()
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))  # Dehnbarer Bereich oben

        button = QPushButton("Select a Context", self)
        button.clicked.connect(self.select_context)
        layout.addWidget(button, 0, Qt.AlignCenter)

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))  # Dehnbarer Bereich unten

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def update_background_image(self):
        pixmap = QPixmap(os.path.join('resources', 'background.png'))
        painter = QPainter(pixmap)
        painter.setOpacity(0.5)  # Setzt die Transparenz auf 50%
        painter.drawPixmap(pixmap.rect(), pixmap)
        painter.end()
        self.background_image.setPixmap(pixmap)
        self.background_image.setGeometry(0, 30, self.width(), self.height() - 30)

    def resizeEvent(self, event: QPaintEvent):
        self.update_background_image()
        super().resizeEvent(event)

    @Slot()
    def select_context(self):
        pass  # Ihre Implementierung hier

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
