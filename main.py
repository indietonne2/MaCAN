import sys
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QMainWindow, QApplication, QAction, QLabel, QMenu, QWidget, QVBoxLayout, QToolBar, QLineEdit, QToolButton
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

        # Setup Central Widget (main area)
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout()
        self.main_widget.setLayout(self.layout)

        # Add a QLineEdit to illustrate 'Cut' and 'Copy'
        self.text_edit = QLineEdit()
        self.layout.addWidget(self.text_edit)

        # Setup Tool Bar
        self.tool_bar = self.addToolBar('Main Tools')

        # Setup File Menu on tool bar
        self.file_menu = QMenu('File', self)
        self.file_button = QToolButton(self)
        self.file_button.setMenu(self.file_menu)
        self.file_button.setPopupMode(QToolButton.InstantPopup)
        self.file_button.setText('File')
        self.tool_bar.addWidget(self.file_button)

        # Setup Edit Menu on tool bar
        self.edit_menu = QMenu('Edit', self)
        self.edit_button = QToolButton(self)
        self.edit_button.setMenu(self.edit_menu)
        self.edit_button.setPopupMode(QToolButton.InstantPopup)
        self.edit_button.setText('Edit')
        self.tool_bar.addWidget(self.edit_button)

        # Setup Help Menu on tool bar
        self.help_menu = QMenu('Help', self)
        self.help_button = QToolButton(self)
        self.help_button.setMenu(self.help_menu)
        self.help_button.setPopupMode(QToolButton.InstantPopup)
        self.help_button.setText('Help')
        self.tool_bar.addWidget(self.help_button)

        # File Menu Actions
        self.exit_action = QAction('Exit', self)
        self.file_menu.addAction(self.exit_action)
        self.exit_action.triggered.connect(self.exit_app)

        # Edit Menu Actions
        self.cut_action = QAction('Cut', self)
        self.edit_menu.addAction(self.cut_action)
        self.cut_action.triggered.connect(self.text_edit.cut)

        self.copy_action = QAction('Copy', self)
        self.edit_menu.addAction(self.copy_action)
        self.copy_action.triggered.connect(self.text_edit.copy)

        # Help Menu Actions
        self.about_action = QAction('About', self)
        self.help_menu.addAction(self.about_action)

        self.mylabel = QLabel(self.main_widget)
        self.mylabel.setText('Hello, World!')

    def exit_app(self):
        sys.exit()


mywindow = MainWindow()
mywindow.show()