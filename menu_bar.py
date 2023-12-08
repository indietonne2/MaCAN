
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QToolButton, QMenu, QApplication, QMessageBox, QWidget, QSizePolicy
from custom_toolbar import CustomToolBar

import version

class MenuBar:
    def __init__(self, main_window):
        self.tool_bar = CustomToolBar('Main Tools', main_window)

        # Erstellen der "File" und "Edit" Menüs zuerst
        self.create_file_menu(main_window)
        self.create_edit_menu(main_window)

        # Spacer hinzufügen, um die "Hilfe"-Schaltfläche rechtsbündig zu machen
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.tool_bar.addWidget(spacer)

        # "Hilfe"-Menü zuletzt hinzufügen
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
        cut_action.triggered.connect(self.cut_text)
        edit_menu.addAction(cut_action)

        copy_action = QAction('Copy', self.tool_bar)
        copy_action.triggered.connect(self.copy_text)
        edit_menu.addAction(copy_action)

        # Überprüfen Sie beim Öffnen des Menüs, ob die Aktionen aktiviert sein sollten
        edit_menu.aboutToShow.connect(self.update_edit_actions)

    def cut_text(self):
        focused_widget = QApplication.focusWidget()
        if isinstance(focused_widget, (QLineEdit, QTextEdit)):
            focused_widget.cut()

    def copy_text(self):
        focused_widget = QApplication.focusWidget()
        if isinstance(focused_widget, (QLineEdit, QTextEdit)):
            focused_widget.copy()

    def update_edit_actions(self):
        focused_widget = QApplication.focusWidget()
        is_editable = isinstance(focused_widget, (QLineEdit, QTextEdit))

        for action in self.tool_bar.actions():
            if action.text() in ["Cut", "Copy"]:
                action.setEnabled(is_editable)

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
