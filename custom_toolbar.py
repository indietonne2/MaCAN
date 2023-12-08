from PySide6.QtWidgets import QToolBar, QWidget, QSizePolicy

class CustomToolBar(QToolBar):
    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        # Spacer, der am Ende der Toolbar hinzugefügt wird, um die Buttons linksbündig zu machen
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.addWidget(spacer)
