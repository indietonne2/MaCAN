import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QAction, QMenu, QToolButton, QWidget, QToolBar, QLineEdit
from PySide6.QtGui import QApplication
import version


class MenuBar:
    def __init__(self, parent):
        self.tool_bar = QToolBar('Main Tools', parent)

        self.create_file_menu()
        self.create_edit_menu()

    def create_file_menu(self):
        file_button = QToolButton(self.tool_bar)
        file_button.setText('File')
        file_menu = QMenu(file_button)
        file_button.setMenu(file_menu)
        file_button.setPopupMode(QToolButton.InstantPopup)
        self.tool_bar.addWidget(file_button)

        exit_action = QAction('Exit', self.tool_bar)
        exit_action.triggered.connect(QApplication.instance().quit)
        file_menu.addAction(exit_action)

    def create_edit_menu(self):
        edit_button = QToolButton(self.tool_bar)
        edit_button.setText('Edit')
        edit_menu = QMenu(edit_button)
        edit_button.setMenu(edit_menu)
        edit_button.setPopupMode(QToolButton.InstantPopup)
        self.tool_bar.addWidget(edit_button)

        cut_action = QAction('Cut', self.tool_bar)
        cut_action.triggered.connect(self.tool_bar.parent().parent().text_edit.cut)
        edit_menu.addAction(cut_action)

        copy_action = QAction('Copy', self.tool_bar)
        copy_action.triggered.connect(self.tool_bar.parent().parent().text_edit.copy)
        edit_menu.addAction(copy_action)


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

        self.menu_bar = MenuBar(self)
        self.addToolBar(self.menu_bar.tool_bar)

        self.mylabel = QLabel(self.main_widget)
        self.mylabel.setText('Hello, World!')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())