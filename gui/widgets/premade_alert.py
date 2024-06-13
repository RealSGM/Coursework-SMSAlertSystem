# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'premade_alert.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QLabel, QLayout, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QTimeEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(530, 266)
        MainWindow.setMinimumSize(QSize(0, 80))
        MainWindow.setStyleSheet(u"border-radius: 0px")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(9)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet(u"border-radius: 20px;")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(100, 20))
        self.label_2.setStyleSheet(u"color: #706C6E;\n"
"font-weight: bold;")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.weather_type = QComboBox(self.groupBox_4)
        self.weather_type.addItem("")
        self.weather_type.addItem("")
        self.weather_type.addItem("")
        self.weather_type.addItem("")
        self.weather_type.addItem("")
        self.weather_type.addItem("")
        self.weather_type.setObjectName(u"weather_type")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.weather_type.sizePolicy().hasHeightForWidth())
        self.weather_type.setSizePolicy(sizePolicy1)
        self.weather_type.setMinimumSize(QSize(100, 20))

        self.gridLayout.addWidget(self.weather_type, 1, 1, 1, 1)

        self.weather_label = QLabel(self.groupBox_4)
        self.weather_label.setObjectName(u"weather_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.weather_label.sizePolicy().hasHeightForWidth())
        self.weather_label.setSizePolicy(sizePolicy2)
        self.weather_label.setMinimumSize(QSize(100, 20))
        self.weather_label.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setBold(True)
        self.weather_label.setFont(font1)
        self.weather_label.setStyleSheet(u"color: #706C6E;\n"
"font-weight: bold;")

        self.gridLayout.addWidget(self.weather_label, 1, 0, 1, 1)

        self.time = QTimeEdit(self.groupBox_4)
        self.time.setObjectName(u"time")
        sizePolicy1.setHeightForWidth(self.time.sizePolicy().hasHeightForWidth())
        self.time.setSizePolicy(sizePolicy1)
        self.time.setMinimumSize(QSize(100, 20))

        self.gridLayout.addWidget(self.time, 0, 3, 1, 1)

        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(100, 20))
        self.label.setStyleSheet(u"color: #706C6E;\n"
"font-weight: bold;")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.area_type = QComboBox(self.groupBox_4)
        self.area_type.addItem("")
        self.area_type.addItem("")
        self.area_type.addItem("")
        self.area_type.setObjectName(u"area_type")
        sizePolicy1.setHeightForWidth(self.area_type.sizePolicy().hasHeightForWidth())
        self.area_type.setSizePolicy(sizePolicy1)
        self.area_type.setMinimumSize(QSize(100, 20))

        self.gridLayout.addWidget(self.area_type, 0, 1, 1, 1)

        self.severity = QComboBox(self.groupBox_4)
        self.severity.addItem("")
        self.severity.addItem("")
        self.severity.addItem("")
        self.severity.addItem("")
        self.severity.setObjectName(u"severity")

        self.gridLayout.addWidget(self.severity, 1, 3, 1, 1)

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: #706C6E;\n"
"font-weight: bold;")

        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: #706C6E;\n"
"font-weight: bold;")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.duration = QComboBox(self.groupBox_4)
        self.duration.addItem("")
        self.duration.addItem("")
        self.duration.addItem("")
        self.duration.addItem("")
        self.duration.setObjectName(u"duration")

        self.gridLayout.addWidget(self.duration, 2, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.message = QPlainTextEdit(self.groupBox_4)
        self.message.setObjectName(u"message")
        self.message.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_3.addWidget(self.message)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.send_premade_alert = QPushButton(self.groupBox_4)
        self.send_premade_alert.setObjectName(u"send_premade_alert")
        self.send_premade_alert.setMinimumSize(QSize(0, 20))
        self.send_premade_alert.setMaximumSize(QSize(16777215, 20))
        self.send_premade_alert.setFont(font1)
        self.send_premade_alert.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.send_premade_alert)

        self.premade_to_main_button = QPushButton(self.groupBox_4)
        self.premade_to_main_button.setObjectName(u"premade_to_main_button")
        self.premade_to_main_button.setMinimumSize(QSize(0, 20))
        self.premade_to_main_button.setFont(font1)
        self.premade_to_main_button.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.premade_to_main_button)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.verticalLayout.addWidget(self.groupBox_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_4.setTitle("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.weather_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Flood", None))
        self.weather_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Typhoon", None))
        self.weather_type.setItemText(2, QCoreApplication.translate("MainWindow", u"Drought", None))
        self.weather_type.setItemText(3, QCoreApplication.translate("MainWindow", u"Hurricane", None))
        self.weather_type.setItemText(4, QCoreApplication.translate("MainWindow", u"Tropical Storm", None))
        self.weather_type.setItemText(5, QCoreApplication.translate("MainWindow", u"Other", None))

        self.weather_label.setText(QCoreApplication.translate("MainWindow", u"Weather Type", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Area Type", None))
        self.area_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Cambodia", None))
        self.area_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Pu Ngaol", None))
        self.area_type.setItemText(2, QCoreApplication.translate("MainWindow", u"Surrounding Areas", None))

        self.severity.setItemText(0, QCoreApplication.translate("MainWindow", u"Low", None))
        self.severity.setItemText(1, QCoreApplication.translate("MainWindow", u"Medium", None))
        self.severity.setItemText(2, QCoreApplication.translate("MainWindow", u"High", None))
        self.severity.setItemText(3, QCoreApplication.translate("MainWindow", u"Extreme", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Severity", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Duration", None))
        self.duration.setItemText(0, QCoreApplication.translate("MainWindow", u"< 1 Hour", None))
        self.duration.setItemText(1, QCoreApplication.translate("MainWindow", u"1 - 2 Hours", None))
        self.duration.setItemText(2, QCoreApplication.translate("MainWindow", u"3 - 6 Hours", None))
        self.duration.setItemText(3, QCoreApplication.translate("MainWindow", u"6 - 24 Hours", None))

        self.message.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter custom message...", None))
        self.send_premade_alert.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.premade_to_main_button.setText(QCoreApplication.translate("MainWindow", u"Back to Main", None))
    # retranslateUi

