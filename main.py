# Import PySide6 classes
import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QAction, QLabel, QMenuBar, QMenu
import version

print(f'Version: {version.version}')
print(f'Autor: {version.author}')
print(f'AppName: {version.app_name}')

# Create a Qt application
app = QApplication(sys.argv)


# Create a Window
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setGeometry(50, 50, 1920, 1080)
        self.setWindowTitle(f"{version.app_name} {version.version}")

        # Create menu bar
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)

        # Create a File menu
        self.file_menu = QMenu('File', self)
        self.menu_bar.addMenu(self.file_menu)

        # Add actions to File menu
        self.exit_action = QAction('Exit', self)
        self.file_menu.addAction(self.exit_action)
        self.exit_action.triggered.connect(self.exit_app)

        # Create a label
        self.mylabel = QLabel(self)
        self.mylabel.setText('Hello, World!')
        self.mylabel.setGeometry(QtCore.QRect(200, 200, 200, 200))

    def exit_app(self):
        sys.exit()


mywindow = MainWindow()
mywindow.show()

# Enter Qt application main loop
sys.exit(app.exec())