from PySide6.QtWidgets import QToolBar, QWidget, QSizePolicy

class CustomToolBar(QToolBar):
    def __init__(self, title, parent = None):
        super().__init__(title, parent)
        spacer = QWidget(self)
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.addWidget(spacer)