import sys
import version
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QMenu, QWidget, QVBoxLayout, QToolBar, QLineEdit, QToolButton
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 800, 600)
        self.setWindowTitle(f"{version.app_name} {version.version}")

        self.main_widget = QWidget(self)
        self.layout = QVBoxLayout(self.main_widget)
        self.setCentralWidget(self.main_widget)

        self.text_edit = QLineEdit()
        self.layout.addWidget(self.text_edit)

        self.tool_bar = self.addToolBar('Main Tools')

        self.file_button = QToolButton(self)
        self.file_button.setText('File')
        self.file_menu = QMenu('File', self.file_button)
        self.file_button.setMenu(self.file_menu)
        self.file_button.setPopupMode(QToolButton.InstantPopup)
        self.tool_bar.addWidget(self.file_button)

        self.edit_button = QToolButton(self)
        self.edit_button.setText('Edit')
        self.edit_menu = QMenu('Edit', self.edit_button)
        self.edit_button.setMenu(self.edit_menu)
        self.edit_button.setPopupMode(QToolButton.InstantPopup)
        self.tool_bar.addWidget(self.edit_button)

        self.help_button = QToolButton(self)
        self.help_button.setText('Help')
        self.help_menu = QMenu('Help', self.help_button)
        self.help_button.setMenu(self.help_menu)
        self.help_button.setPopupMode(QToolButton.InstantPopup)
        self.tool_bar.addWidget(self.help_button)

        self.exit_action = QAction('Exit', self)
        self.exit_action.triggered.connect(self.close)
        self.file_menu.addAction(self.exit_action)

        self.cut_action = QAction('Cut', self)
        self.cut_action.triggered.connect(self.text_edit.cut)
        self.edit_menu.addAction(self.cut_action)

        self.copy_action = QAction('Copy', self)
        self.copy_action.triggered.connect(self.text_edit.copy)
        self.edit_menu.addAction(self.copy_action)

        self.mylabel = QLabel(self.main_widget)
        self.mylabel.setText('Hello, World!')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())