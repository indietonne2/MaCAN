# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'emulation.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QTextBrowser, QTextEdit,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(2560, 1462)
        self.CanReceiver = QTextBrowser(Dialog)
        self.CanReceiver.setObjectName(u"CanReceiver")
        self.CanReceiver.setGeometry(QRect(170, 510, 256, 891))
        self.CanMessage = QTextEdit(Dialog)
        self.CanMessage.setObjectName(u"CanMessage")
        self.CanMessage.setGeometry(QRect(190, 280, 231, 71))
        self.CanSender = QListWidget(Dialog)
        self.CanSender.setObjectName(u"CanSender")
        self.CanSender.setGeometry(QRect(190, 80, 231, 192))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(470, 280, 100, 32))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"SendButton", None))
    # retranslateUi

