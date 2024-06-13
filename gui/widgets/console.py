# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'console.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(517, 178)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scroll_layout = QWidget()
        self.scroll_layout.setObjectName(u"scroll_layout")
        self.scroll_layout.setGeometry(QRect(0, 0, 491, 118))
        self.verticalLayout_4 = QVBoxLayout(self.scroll_layout)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea.setWidget(self.scroll_layout)

        self.verticalLayout.addWidget(self.scrollArea)

        self.console_to_main_button = QPushButton(self.centralwidget)
        self.console_to_main_button.setObjectName(u"console_to_main_button")
        self.console_to_main_button.setMinimumSize(QSize(0, 20))
        self.console_to_main_button.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setBold(True)
        self.console_to_main_button.setFont(font)
        self.console_to_main_button.setStyleSheet(u"QPushButton {\n"
"	border: 0px;\n"
"	border-radius: 10px;\n"
"	font-weight: bold;\n"
"	background-color: #a2c9e7;\n"
"	color: #f7ffff;\n"
"}\n"
"QPushButton:Hover {\n"
"	background-color: #8faae4;\n"
"}")

        self.verticalLayout.addWidget(self.console_to_main_button)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.console_to_main_button.setText(QCoreApplication.translate("MainWindow", u"Back to Main", None))
    # retranslateUi

