from PySide6.QtWidgets import QMainWindow, QApplication, QStatusBar, QTextEdit, QAction, QMenu, QMenuBar, QRect
from PySide6.QtCore import Qt
from version import app_name, version, author

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


class MaCANApp(QMainWindow):
    """
    This class represents the main application window for MaCANApp.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"{app_name} - v{version}")
        self.main_content = None
        self.create_widgets()

    def create_widgets(self):
        self.create_menu_bar()
        self.create_status_bar()
        self.create_main_content()

    def create_menu_bar(self):
        menu_bar: QMenuBar = self.menuBar()
        file_menu: QMenu = menu_bar.addMenu('&File')
        file_menu.addAction(QAction('&Exit', self, triggered=self.close))

    def create_status_bar(self):
        status_bar: QStatusBar = QStatusBar()
        status_bar.showMessage(f"Developed by {author}")
        self.setStatusBar(status_bar)

    def create_main_content(self):
        self.main_content: QTextEdit = QTextEdit(self)
        self.main_content.setGeometry(QRect(10, 30, 780, 560))


if __name__ == "__main__":
    app = QApplication([])
    mainWin = MaCANApp()
    mainWin.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
    mainWin.show()
    app.exec()
