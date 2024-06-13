# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'server_gui.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 348)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        font = QFont()
        font.setFamilies([u"Roboto"])
        self.frame_3.setFont(font)
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.server_label = QLabel(self.frame_3)
        self.server_label.setObjectName(u"server_label")
        self.server_label.setMaximumSize(QSize(100, 40))
        self.server_label.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.server_label)

        self.status_label = QLabel(self.frame_3)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setMaximumSize(QSize(100, 40))
        self.status_label.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.status_label)

        self.connection_bar = QProgressBar(self.frame_3)
        self.connection_bar.setObjectName(u"connection_bar")
        self.connection_bar.setValue(24)
        self.connection_bar.setTextVisible(False)

        self.horizontalLayout_2.addWidget(self.connection_bar)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"border-bottom: 2px solid black;")

        self.verticalLayout_3.addWidget(self.lineEdit)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.reconnect_button = QPushButton(self.frame_3)
        self.reconnect_button.setObjectName(u"reconnect_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reconnect_button.sizePolicy().hasHeightForWidth())
        self.reconnect_button.setSizePolicy(sizePolicy)
        self.reconnect_button.setMinimumSize(QSize(200, 20))
        self.reconnect_button.setMaximumSize(QSize(16777215, 16777215))
        self.reconnect_button.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.reconnect_button)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.premade_alert_button = QPushButton(self.frame_3)
        self.premade_alert_button.setObjectName(u"premade_alert_button")
        self.premade_alert_button.setMinimumSize(QSize(200, 20))
        self.premade_alert_button.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setBold(True)
        self.premade_alert_button.setFont(font1)
        self.premade_alert_button.setStyleSheet(u"QPushButton {\n"
"	border: 0px;\n"
"	border-radius: 10px;\n"
"	font-weight: bold;\n"
"	background-color: #a2c9e7;\n"
"	color: #f7ffff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #8faae4;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #6b93d6;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #d3d3d3;\n"
"	color: #a9a9a9;\n"
"	border: 1px solid #a2c9e7;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.premade_alert_button, 0, 0, 1, 1)

        self.custom_alert_button = QPushButton(self.frame_3)
        self.custom_alert_button.setObjectName(u"custom_alert_button")
        self.custom_alert_button.setMinimumSize(QSize(200, 20))
        self.custom_alert_button.setMaximumSize(QSize(16777215, 20))
        self.custom_alert_button.setFont(font1)
        self.custom_alert_button.setStyleSheet(u"QPushButton {\n"
"	border: 0px;\n"
"	border-radius: 10px;\n"
"	font-weight: bold;\n"
"	background-color: #a2c9e7;\n"
"	color: #f7ffff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #8faae4;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #6b93d6;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #d3d3d3;\n"
"	color: #a9a9a9;\n"
"	border: 1px solid #a2c9e7;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.custom_alert_button, 0, 1, 1, 1)

        self.console_button = QPushButton(self.frame_3)
        self.console_button.setObjectName(u"console_button")
        self.console_button.setMinimumSize(QSize(200, 20))
        self.console_button.setMaximumSize(QSize(16777215, 20))
        self.console_button.setFont(font1)
        self.console_button.setStyleSheet(u"QPushButton {\n"
"	border: 0px;\n"
"	border-radius: 10px;\n"
"	font-weight: bold;\n"
"	background-color: #a2c9e7;\n"
"	color: #f7ffff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #8faae4;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #6b93d6;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #d3d3d3;\n"
"	color: #a9a9a9;\n"
"	border: 1px solid #a2c9e7;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.console_button, 1, 0, 1, 1)

        self.weather_button = QPushButton(self.frame_3)
        self.weather_button.setObjectName(u"weather_button")
        self.weather_button.setMinimumSize(QSize(200, 20))
        self.weather_button.setMaximumSize(QSize(16777215, 20))
        self.weather_button.setFont(font1)
        self.weather_button.setStyleSheet(u"QPushButton {\n"
"	border: 0px;\n"
"	border-radius: 10px;\n"
"	font-weight: bold;\n"
"	background-color: #a2c9e7;\n"
"	color: #f7ffff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #8faae4;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #6b93d6;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #d3d3d3;\n"
"	color: #a9a9a9;\n"
"	border: 1px solid #a2c9e7;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.weather_button, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.server_label.setText(QCoreApplication.translate("MainWindow", u"Server Status:", None))
        self.status_label.setText(QCoreApplication.translate("MainWindow", u"Disconnected", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter IP:Port", None))
        self.reconnect_button.setText(QCoreApplication.translate("MainWindow", u"Reconnect", None))
        self.premade_alert_button.setText(QCoreApplication.translate("MainWindow", u"Send Pre-Made Alert", None))
        self.custom_alert_button.setText(QCoreApplication.translate("MainWindow", u"Send Custom Alert", None))
        self.console_button.setText(QCoreApplication.translate("MainWindow", u"View Console", None))
        self.weather_button.setText(QCoreApplication.translate("MainWindow", u"View Weather Monitor", None))
    # retranslateUi

