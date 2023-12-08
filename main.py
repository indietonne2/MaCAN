import sys
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QMenuBar, QMenu, QWidget, QVBoxLayout, QToolBar
from PySide6.QtGui import QAction
import version

print(f'Version: {version.version}')
print(f'Autor: {version.author}')
print(f'AppName: {version.app_name}')

app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setGeometry(50, 50, 800, 600)
        self.setWindowTitle(f"{version.app_name} {version.version}")

        # Setup Main Area (central widget)
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout()
        self.main_widget.setLayout(self.layout)

        # Setup Tool Bar
        self.tool_bar = self.addToolBar('Main Tools')

        # Setup File Menu on tool bar
        self.file_menu = QMenu('File', self)
        self.file_action = self.tool_bar.addAction('File')
        self.file_action.setMenu(self.file_menu)

        # Setup Edit Menu on tool bar
        self.edit_menu = QMenu('Edit', self)
        self.edit_action = self.tool_bar.addAction('Edit')
        self.edit_action.setMenu(self.edit_menu)

        # Setup Help Menu on tool bar
        self.help_menu = QMenu('Help', self)
        self.help_action = self.tool_bar.addAction('Help')
        self.help_action.setMenu(self.help_menu)

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

        self.mylabel = QLabel(self.main_widget)
        self.mylabel.setText('Hello, World!')

    def exit_app(self):
        sys.exit()


mywindow = MainWindow()
mywindow.show()

sys.exit(app.exec())