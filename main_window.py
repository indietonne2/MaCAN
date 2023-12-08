from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit
from menu_bar import MenuBar
import version

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
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

        self.showMaximized()
