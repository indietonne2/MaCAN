import sys
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QMainWindow, QApplication, QAction, QLabel, QMenuBar, QMenu
import version

print(f'Version: {version.version}')
print(f'Autor: {version.author}')
print(f'AppName: {version.app_name}')

app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setGeometry(50, 50, 1920, 1080)
        self.setWindowTitle(f"{version.app_name} {version.version}")
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)
        self.file_menu = QMenu('File', self)
        self.menu_bar.addMenu(self.file_menu)
        self.exit_action = QAction('Exit', self)
        self.file_menu.addAction(self.exit_action)
        self.exit_action.triggered.connect(self.exit_app)
        self.mylabel = QLabel(self)
        self.mylabel.setText('Hello, World!')
        self.mylabel.setGeometry(QRect(200, 200, 200, 200))

    def exit_app(self):
        sys.exit()


mywindow = MainWindow()
mywindow.show()

sys.exit(app.exec())