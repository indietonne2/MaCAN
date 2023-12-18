# main.py
# Main application entry point for MaCAN
# References version information from version.py

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from menu import MenuBar
from pages.start_screen import StartScreen
from version import app_name, version, author


class MaCAN(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set the menu bar
        self.menu_bar = MenuBar(self)
        self.setMenuBar(self.menu_bar)

        # Set the central widget to the start screen
        self.start_screen = StartScreen()
        self.setCentralWidget(self.start_screen)

        self.setWindowTitle(app_name)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MaCAN()
    sys.exit(app.exec())
