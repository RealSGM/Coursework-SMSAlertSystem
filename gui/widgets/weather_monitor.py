# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weather_monitor.ui'
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
    QLabel, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(433, 282)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName(u"gridLayout")
        self.w_speed_data = QLabel(self.frame_2)
        self.w_speed_data.setObjectName(u"w_speed_data")
        self.w_speed_data.setStyleSheet(u"font-weight: bold;")
        self.w_speed_data.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.w_speed_data, 3, 1, 1, 1)

        self.w_speed = QLabel(self.frame_2)
        self.w_speed.setObjectName(u"w_speed")
        self.w_speed.setStyleSheet(u"font-weight: bold;")

        self.gridLayout.addWidget(self.w_speed, 3, 0, 1, 1)

        self.w_dir_data = QLabel(self.frame_2)
        self.w_dir_data.setObjectName(u"w_dir_data")
        self.w_dir_data.setStyleSheet(u"font-weight: bold;")
        self.w_dir_data.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.w_dir_data, 1, 3, 1, 1)

        self.location_data = QLabel(self.frame_2)
        self.location_data.setObjectName(u"location_data")
        self.location_data.setStyleSheet(u"font-weight: bold;")
        self.location_data.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.location_data, 0, 1, 1, 1)

        self.temp_data = QLabel(self.frame_2)
        self.temp_data.setObjectName(u"temp_data")
        self.temp_data.setStyleSheet(u"font-weight: bold;")
        self.temp_data.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.temp_data, 2, 3, 1, 1)

        self.cc_data = QLabel(self.frame_2)
        self.cc_data.setObjectName(u"cc_data")
        self.cc_data.setStyleSheet(u"font-weight: bold;")
        self.cc_data.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.cc_data, 1, 1, 1, 1)

        self.condition = QLabel(self.frame_2)
        self.condition.setObjectName(u"condition")
        self.condition.setStyleSheet(u"font-weight: bold;")

        self.gridLayout.addWidget(self.condition, 0, 2, 1, 1)

        self.condition_data = QLabel(self.frame_2)
        self.condition_data.setObjectName(u"condition_data")
        self.condition_data.setStyleSheet(u"font-weight: bold;")
        self.condition_data.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.condition_data, 0, 3, 1, 1)

        self.humidity = QLabel(self.frame_2)
        self.humidity.setObjectName(u"humidity")
        self.humidity.setStyleSheet(u"font-weight: bold;")

        self.gridLayout.addWidget(self.humidity, 2, 0, 1, 1)

        self.temp = QLabel(self.frame_2)
        self.temp.setObjectName(u"temp")
        self.temp.setStyleSheet(u"font-weight: bold;")

        self.gridLayout.addWidget(self.temp, 2, 2, 1, 1)

        self.cc = QLabel(self.frame_2)
        self.cc.setObjectName(u"cc")
        self.cc.setStyleSheet(u"font-weight: bold;")

        self.gridLayout.addWidget(self.cc, 1, 0, 1, 1)

        self.humidity_data = QLabel(self.frame_2)
        self.humidity_data.setObjectName(u"humidity_data")
        self.humidity_data.setStyleSheet(u"font-weight: bold;")
        self.humidity_data.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.humidity_data, 2, 1, 1, 1)

        self.location = QLabel(self.frame_2)
        self.location.setObjectName(u"location")
        self.location.setStyleSheet(u"font-weight: bold;")

        self.gridLayout.addWidget(self.location, 0, 0, 1, 1)

        self.w_dir = QLabel(self.frame_2)
        self.w_dir.setObjectName(u"w_dir")
        self.w_dir.setStyleSheet(u"font-weight: bold;")

        self.gridLayout.addWidget(self.w_dir, 1, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.celsius_radio = QRadioButton(self.frame_2)
        self.celsius_radio.setObjectName(u"celsius_radio")
        self.celsius_radio.setStyleSheet(u"color: #706C6E;\n"
"font-weight: bold;")

        self.horizontalLayout_4.addWidget(self.celsius_radio)

        self.fahrenheit_radio = QRadioButton(self.frame_2)
        self.fahrenheit_radio.setObjectName(u"fahrenheit_radio")
        self.fahrenheit_radio.setStyleSheet(u"color: #706C6E;\n"
"font-weight: bold;")

        self.horizontalLayout_4.addWidget(self.fahrenheit_radio)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.refresh_weather_button = QPushButton(self.frame_2)
        self.refresh_weather_button.setObjectName(u"refresh_weather_button")
        self.refresh_weather_button.setMinimumSize(QSize(100, 20))
        self.refresh_weather_button.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setBold(True)
        self.refresh_weather_button.setFont(font)
        self.refresh_weather_button.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.refresh_weather_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.weather_to_main_button = QPushButton(self.frame_2)
        self.weather_to_main_button.setObjectName(u"weather_to_main_button")
        self.weather_to_main_button.setMinimumSize(QSize(100, 20))
        self.weather_to_main_button.setMaximumSize(QSize(16777215, 20))
        self.weather_to_main_button.setFont(font)
        self.weather_to_main_button.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.weather_to_main_button)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.w_speed_data.setText(QCoreApplication.translate("MainWindow", u"[DATA]", None))
        self.w_speed.setText(QCoreApplication.translate("MainWindow", u"Wind Speed", None))
        self.w_dir_data.setText(QCoreApplication.translate("MainWindow", u"[DATA]", None))
        self.location_data.setText(QCoreApplication.translate("MainWindow", u"[DATA]", None))
        self.temp_data.setText(QCoreApplication.translate("MainWindow", u"[DATA]", None))
        self.cc_data.setText(QCoreApplication.translate("MainWindow", u"[DATA]", None))
        self.condition.setText(QCoreApplication.translate("MainWindow", u"Condition", None))
        self.condition_data.setText(QCoreApplication.translate("MainWindow", u"[DATA]", None))
        self.humidity.setText(QCoreApplication.translate("MainWindow", u"Humidity", None))
        self.temp.setText(QCoreApplication.translate("MainWindow", u"Tempurature", None))
        self.cc.setText(QCoreApplication.translate("MainWindow", u"Cloud Coverage", None))
        self.humidity_data.setText(QCoreApplication.translate("MainWindow", u"[DATA]", None))
        self.location.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.w_dir.setText(QCoreApplication.translate("MainWindow", u"Wind Direction", None))
        self.celsius_radio.setText(QCoreApplication.translate("MainWindow", u"Celsius", None))
        self.fahrenheit_radio.setText(QCoreApplication.translate("MainWindow", u"Farenheit", None))
        self.refresh_weather_button.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.weather_to_main_button.setText(QCoreApplication.translate("MainWindow", u"Back to Main", None))
    # retranslateUi

