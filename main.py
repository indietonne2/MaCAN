from PySide6.QtCore import QRect
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMenu
from PySide6.QtGui import QAction
import sys
import version

print(f'Version: {version.version}')
print(f'Autor: {version.author}')
print(f'AppName: {version.app_name}')

app = QApplication(sys.argv)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 800, 600)
        self.setWindowTitle(f"{version.app_name} {version.version}")

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.menu_button = QPushButton('Menu')
        self.layout.addWidget(self.menu_button)

        self.menu = QMenu(self)

        # File Menu Actions
        self.exit_action = QAction('Exit', self)
        self.menu.addAction(self.exit_action)
        self.exit_action.triggered.connect(self.exit_app)

        # Additional actions as needed...
        self.menu_button.setMenu(self.menu)

        self.mylabel = QLabel(self)
        self.mylabel.setText('Hello, World!')
        self.mylabel.setGeometry(QRect(200, 200, 200, 200))

    def exit_app(self):
        sys.exit()


mywindow = MainWindow()
mywindow.show()

sys.exit(app.exec())