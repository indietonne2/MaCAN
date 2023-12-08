import logging
mport sys
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QMenu, QToolButton, QWidget, QToolBar, QLineEdit, QMessageBox
from PySide6.QtGui import QAction, QTextDocument, QTextCursor, QTextOption
from PySide6.QtCore import Qt  # We need QtCore.Qt for the alignment
import version
import logging



class MenuBar:
    def __init__(self, main_window):
        self.tool_bar = QToolBar('Main Tools', main_window)

        self.create_file_menu(main_window)
        self.create_edit_menu(main_window)
        self.create_help_menu(main_window)

    def create_file_menu(self, window):
        file_button = QToolButton(self.tool_bar)
        file_button.setText('File')
        file_menu = QMenu(file_button)
        file_button.setMenu(file_menu)
        file_button.setPopupMode(QToolButton.InstantPopup)
        self.tool_bar.addWidget(file_button)

        exit_action = QAction('Exit', self.tool_bar)
        exit_action.triggered.connect(QApplication.instance().quit)
        file_menu.addAction(exit_action)

    def create_edit_menu(self, window):
        edit_button = QToolButton(self.tool_bar)
        edit_button.setText('Edit')
        edit_menu = QMenu(edit_button)
        edit_button.setMenu(edit_menu)
        edit_button.setPopupMode(QToolButton.InstantPopup)
        self.tool_bar.addWidget(edit_button)

        cut_action = QAction('Cut', self.tool_bar)
        cut_action.triggered.connect(window.text_edit.cut)
        edit_menu.addAction(cut_action)

        copy_action = QAction('Copy', self.tool_bar)
        copy_action.triggered.connect(window.text_edit.copy)
        edit_menu.addAction(copy_action)

    def create_help_menu(self, window):
        help_button = QToolButton(self.tool_bar)
        help_button.setText('Help')
        help_menu = QMenu(help_button)
        help_button.setMenu(help_menu)
        help_button.setPopupMode(QToolButton.InstantPopup)
        self.tool_bar.addWidget(help_button)

        about_action = QAction('About', window)
        about_action.triggered.connect(self.showMessage)
        help_menu.addAction(about_action)

    def showMessage(self):
        message_box = QMessageBox()
        message_box.setWindowTitle("About")
        text_document = QTextDocument()
        text_cursor = QTextCursor(text_document)
        text_cursor.insertText(f"{version.app_name}\n{version.version}\n\n{version.author}")
        text_document.setDefaultTextOption(QTextOption(Qt.AlignCenter))
        message_box.setText(text_document.toPlainText())
        message_box.show()
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