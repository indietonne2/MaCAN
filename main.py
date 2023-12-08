from PySide6.QtCore import QRect
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QMenuBar, QMenu
from PySide6.QtGui import QAction
import sys
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

        # Setup Menu Bar
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)

        # Setup File Menu
        self.file_menu = QMenu('File', self)
        self.menu_bar.addMenu(self.file_menu)

        # Setup Edit Menu
        self.edit_menu = QMenu('Edit', self)
        self.menu_bar.addMenu(self.edit_menu)

        # Setup Help Menu
        self.help_menu = QMenu('Help', self)
        self.menu_bar.addMenu(self.help_menu)

        # File Menu Actions
        self.exit_action = QAction('Exit', self)
        self.file_menu.addAction(self.exit_action)
        self.exit_action.triggered.connect(self.exit_app)

        # Edit Menu Actions
        self.cut_action = QAction('Cut', self)
        self.edit_menu.addAction(self.cut_action)

        self.copy_action = QAction('Copy', self)
        self.edit_menu.addAction(self.copy_action)

        # Help Menu Actions
        self.about_action = QAction('About', self)
        self.help_menu.addAction(self.about_action)

        self.mylabel = QLabel(self)
        self.mylabel.setText('Hello, World!')
        self.mylabel.setGeometry(QRect(200, 200, 200, 200))

    def exit_app(self):
        sys.exit()


mywindow = MainWindow()
mywindow.show()

sys.exit(app.exec())