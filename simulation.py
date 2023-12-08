from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit
import can  # Importing the CAN library

class SimulationWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Main layout
        layout = QVBoxLayout(self)

        # Text fields
        self.textField1 = QLineEdit(self)
        self.textField2 = QLineEdit(self)

        # Add text fields to the layout
        layout.addWidget(self.textField1)
        layout.addWidget(self.textField2)

        # Set the layout for the widget
        self.setLayout(layout)

# If you need to run this file independently for testing
# You can include a main function like this:
def main():
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    simWindow = SimulationWidget()
    simWindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
