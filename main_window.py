import configparser
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication, QVBoxLayout, QWidget, QPushButton, QInputDialog, QFileDialog
from PySide6.QtGui import QColor, QPixmap
from PySide6.QtCore import Qt, Slot
import sys
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.modus_config = self.read_config()
        self.initUI()

    def read_config(self):
        config = configparser.ConfigParser()
        config.read('parameter.cfg')
        return config['Modus']

    @Slot()
    def select_context(self):
        parameters_file = QFileDialog.getOpenFileName(self, "Open parameters file", "", "Config Files (*.cfg)")

        if parameters_file:
            self.config.read(parameters_file[0])
            options = self.config.options('parameters')

            item, ok = QInputDialog.getItem(self, "Select a context", "Select a parameter:", options, 0, False)

            if ok and item:
                print(f"Selected: {item}")

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
        modus_label.setAlignment(Qt.AlignCenter)
        modus_label.setStyleSheet(f"background-color: {color_map[farbe].name()};")
        modus_label.setGeometry(0, 0, self.width(), 30)

        # Hintergrundbild hinzufügen
        background_image = QLabel(self)
        pixmap = QPixmap(os.path.join('resources', 'background.png'))
        background_image.setPixmap(pixmap)
        background_image.setGeometry(0, 30, self.width(), self.height() - 30)  # Passt das Bild an die Größe des Fensters an


        # Stellen Sie sicher, dass das Label den gesamten Hintergrund bedeckt
        background_layout = QVBoxLayout()
        background_layout.addWidget(background_image)

        button = QPushButton("Select a Context", self)
        button.clicked.connect(self.select_context)
        background_layout.addWidget(button)

        background_widget = QWidget()
        background_widget.setLayout(background_layout)
        self.setCentralWidget(background_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())