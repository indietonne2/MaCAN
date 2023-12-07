# Import PySide6 classes
import sys
from PySide6 import QtCore, QtWidgets
import version

print(f'Version: {version.version}')
print(f'Autor: {version.author}')
print(f'AppName: {version.app_name}')

# Create a Qt application
app = QtWidgets.QApplication(sys.argv)

# Create a Window
mywindow = QtWidgets.QWidget()
mywindow.resize(600, 800)
mywindow.setWindowTitle(f"{version.app_name} {version.version}")

# Create a label and display it all together
mylabel = QtWidgets.QLabel(mywindow)
mylabel.setText('Hello, World!')
mylabel.setGeometry(QtCore.QRect(200, 200, 200, 200))

mywindow.show()

# Enter Qt application main loop
sys.exit(app.exec())