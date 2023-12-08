import configparser
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.modus_config = self.read_config()
        self.initUI()

    def read_config(self):
        config = configparser.ConfigParser()
        config.read('parameter.cfg')
        return config['Modus']

    def initUI(self):
        modus = "Live"  # Beispiel: Hier könnten Sie den Modus dynamisch bestimmen
        farbe = self.modus_config.get(modus, "Rot")  # Standardfarbe ist Rot

        self.setWindowTitle(f"{modus} Modus")
        self.setGeometry(100, 100, 800, 600)

        color_map = {
            "Rot": QColor(255, 0, 0),
            "Grün": QColor(0, 255, 0),
            "Blau": QColor(0, 0, 255),
            "Orange": QColor(255, 165, 0)
        }

        modus_label = QLabel(modus, self)
        modus_label.setAlignment(Qt.AlignCenter)  # Zentriert den Text im Label
        modus_label.setStyleSheet(f"background-color: {color_map[farbe].name()};")
        modus_label.setGeometry(0, 0, self.width(), 30)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
