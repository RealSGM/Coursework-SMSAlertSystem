# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'custom_alert.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(375, 142)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(9)
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.custom_alert_message = QTextEdit(self.centralwidget)
        self.custom_alert_message.setObjectName(u"custom_alert_message")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(9)
        self.custom_alert_message.setFont(font1)
        self.custom_alert_message.setStyleSheet(u"border: 2px solid black;")

        self.verticalLayout_3.addWidget(self.custom_alert_message)

        self.send_custom_alert_button = QPushButton(self.centralwidget)
        self.send_custom_alert_button.setObjectName(u"send_custom_alert_button")
        self.send_custom_alert_button.setMinimumSize(QSize(0, 20))
        self.send_custom_alert_button.setMaximumSize(QSize(16777215, 20))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setBold(True)
        self.send_custom_alert_button.setFont(font2)
        self.send_custom_alert_button.setStyleSheet(u"QPushButton {\n"
"	border: 0px;\n"
"	border-radius: 10px;\n"
"	font-weight: bold;\n"
"	background-color: #256faf;\n"
"	color: rgb(233, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #1d55aa;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #17468a;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #d3d3d3;\n"
"	color: #a9a9a9;\n"
"	border: 1px solid #256faf;\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.send_custom_alert_button)

        self.custom_to_main_button = QPushButton(self.centralwidget)
        self.custom_to_main_button.setObjectName(u"custom_to_main_button")
        self.custom_to_main_button.setMinimumSize(QSize(100, 20))
        self.custom_to_main_button.setMaximumSize(QSize(16777215, 20))
        self.custom_to_main_button.setFont(font2)
        self.custom_to_main_button.setStyleSheet(u"QPushButton {\n"
"	border: 0px;\n"
"	border-radius: 10px;\n"
"	font-weight: bold;\n"
"	background-color: #a2c9e7;\n"
"	color: #f7ffff;\n"
"}\n"
"QPushButton:Hover {\n"
"	background-color: #8faae4;\n"
"}")

        self.verticalLayout_3.addWidget(self.custom_to_main_button)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.custom_alert_message.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Custom text message", None))
        self.send_custom_alert_button.setText(QCoreApplication.translate("MainWindow", u"Send Custom Alert", None))
        self.custom_to_main_button.setText(QCoreApplication.translate("MainWindow", u"Back to Main", None))
    # retranslateUi

