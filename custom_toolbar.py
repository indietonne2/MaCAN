from PySide6.QtWidgets import QToolBar

class CustomToolBar(QToolBar):
    def __init__(self, title, parent=None):
        super().__init__(title, parent)
