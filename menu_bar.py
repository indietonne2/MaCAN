from PySide6.QtGui import QAction
from PySide6.QtWidgets import QToolButton, QMenu, QApplication, QMessageBox, QWidget, QSizePolicy
from custom_toolbar import CustomToolBar
import version

class MenuBar:
    def __init__(self, main_window):
        self.tool_bar = CustomToolBar('Main Tools', main_window)

        # Erstellen Sie zuerst die "File" und "Edit" Menüs
        self.create_file_menu(main_window)
        self.create_edit_menu(main_window)

        # Fügen Sie dann einen Spacer ein
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.tool_bar.addWidget(spacer)

        # Erstellen Sie zuletzt das "Hilfe"-Menü
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

        about_action = QAction('About', self.tool_bar)
        about_action.triggered.connect(self.showMessage)
        help_menu.addAction(about_action)

    def showMessage(self):
        self.message_box = QMessageBox()
        self.message_box.setWindowTitle("About")
        self.message_box.setText(f"<center>{version.app_name}<br>{version.version}<br><br>{version.author}</center>")
        self.message_box.show()
