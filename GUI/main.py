# Importing necessary libraries from PySide6
import sys
import PySide6


# Importing version information
from version import app_name, version, author


class MaCANApp(PySide6.QtWidgets.QMainWindow):
    """

    This class represents the main application window for MaCANApp.

    Methods:
        - __init__(self): Initializes the MaCANApp instance.
        - create_widgets(self): Creates and configures the widgets for the GUI.

    Attributes:
        - main_content: Represents the main content area of the application as a QTextEdit widget.

    Example usage:

        app = MaCANApp()
        app.show()

    """
    def __init__(self):
        super().__init__()

        # Debugging print statement
        self.main_content = None
        print("Initializing MaCANApp")

        # Setting the window title with the app name and version number
        self.setWindowTitle(f"{app_name} - v{version}")

        # Call to create widgets for the GUI
        self.create_widgets()

    def create_widgets(self):
        # Debugging print statementpip install PySide6
        print("Creating widgets")

        # Creating a menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')

        # Creating a file menu with an exit option
        exit_action = QAction('&Exit', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Creating a status bar to display the author information
        status_bar = PySide6.QtWidgets.QStatusBar()
        status_bar.showMessage(f"Developed by {author}")
        self.setStatusBar(status_bar)

        # Creating the main content area as a text widget
        self.main_content = PySide6.QtWidgets.QTextEdit(self)
        self.main_content.setGeometry(QRect(10, 30, 780, 560))


if __name__ == "__main__":
    # Debugging print statement
    print("Starting MaCANApp")

    app = PySide6.QtWidgets.QApplication(sys.argv)
    mainWin = MaCANApp()
    mainWin.resize(800, 600)
    mainWin.show()

    sys.exit(app.exec())
