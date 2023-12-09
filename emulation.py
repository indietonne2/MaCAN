from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Signal





class EmulationWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)




        # "Zurück" Button
        self.backButton = QPushButton("Zurück", self)
        self.backButton.clicked.connect(self.on_back_clicked)
        layout.addWidget(self.backButton)

        # Text fields
        self.textField1 = QLineEdit(self)
        self.textField2 = QLineEdit(self)

        # Add text fields to the layout
        layout.addWidget(self.textField1)
        layout.addWidget(self.textField2)

        # Set the layout for the widget
        self.setLayout(layout)

        # Set the window title
        self.setWindowTitle("Emulation")


    def on_back_clicked(self):
        self.back_signal.emit()  # Emit the back signal when the button is clicked

# If you need to run this file independently for testing
# You can include a main function like this:
def main():
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    simWindow = EmulationWidget()
    EmuWindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
