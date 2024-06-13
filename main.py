# Imports
import sys, socket, json, threading

import os
os.environ['QT_PLUGIN_PATH'] = 'C:/Users/Ryan/anaconda3/Lib/site-packages/PySide6/plugins'

# Import the PySide6 modules
from PySide6.QtCore import QObject, QThread, Signal, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QLabel, QMessageBox

# Import the GUI classes from the widgets
from gui.widgets.server_gui import Ui_MainWindow as ServerGUI
from gui.widgets.custom_alert import Ui_MainWindow as CustomAlertGUI
from gui.widgets.premade_alert import Ui_MainWindow as PreMadeAlertGUI
from gui.widgets.weather_monitor import Ui_MainWindow as WeatherGUI
from gui.widgets.console import Ui_MainWindow as ConsoleGUI

## Global Variables
server_host = '127.0.0.1'
server_port = 12345
connected = False
server = None

## Windows
server_window = None
console_window = None
weather_window = None
custom_alert_window = None
premade_alert_window = None
stack = None

## Worker class to handle server connection
class ServerConnectionWorker(QObject):
    connection_result = Signal(bool)

    def run(self):
        global server, connected
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.connect((server_host, server_port))
            connected = True
        except Exception:
            connected = False
        self.connection_result.emit(connected)

class ServerWindow(QMainWindow):
    def __init__(self):
        super(ServerWindow, self).__init__()
        global ping_counter
        ping_counter = 0 
        
        self.ui = ServerGUI()
        self.ui.setupUi(self)
        self.ui.reconnect_button.setText("Connect")
        self.ui.lineEdit.setText("127.0.0.1:12345") #change the name of this in qdesigner 
        self.ui.reconnect_button.clicked.connect(self.start_server_connection)
        self.ui.custom_alert_button.clicked.connect(lambda: stack.setCurrentIndex(1))
        self.ui.premade_alert_button.clicked.connect(lambda: stack.setCurrentIndex(2))
        self.ui.weather_button.clicked.connect(lambda: stack.setCurrentIndex(3))
        self.ui.console_button.clicked.connect(lambda: stack.setCurrentIndex(4))
        self.ui.custom_alert_button.setEnabled(False)
        self.ui.premade_alert_button.setEnabled(False)
        self.ui.weather_button.setEnabled(False)

    def start_server_connection(self):
        global bar_value, server_host, server_port
        bar_value = 0
        server_host, server_port = self.split_ip_port(self.ui.lineEdit.text())
        self.progress_timer = QTimer() 
        self.progress_timer.setInterval(100)
        self.progress_timer.timeout.connect(self.update_progress_bar)
        self.progress_timer.start()
        self.ui.connection_bar.setVisible(True)
        self.ui.reconnect_button.setText("Reconnect")

        self.ui.reconnect_button.setEnabled(False)
        self.thread = QThread()
        self.worker = ServerConnectionWorker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.connection_result.connect(self.on_connection_result)
        self.thread.start()

    def split_ip_port(self,text):
        try:
            ip, port = text.split(':')
            return ip, int(port)
        except ValueError:
            raise ValueError("Input should be in the format 'ip:port'")
        
    def on_connection_result(self, result):
        global bar_value
        
        self.thread.quit()
        self.thread.wait()
        self.ui.reconnect_button.setEnabled(True) 
        self.set_status_text()
        self.progress_timer.stop()
        self.ui.connection_bar.setVisible(False)
        bar_value = 0

        if connected:
            self.timer = QTimer()
            self.timer.setInterval(2000)
            self.timer.timeout.connect(self.send_ping)
            self.timer.start()
            
        ## Set stack index to 0
        stack.setCurrentIndex(0)

    def set_status_text(self):
        if connected:
            self.ui.status_label.setText("Connected")
            self.ui.status_label.setStyleSheet("color: green;")
            request_server_command("get_weather all", receive_weather_data)
        else:
            self.ui.status_label.setText("Disconnected")
            self.ui.status_label.setStyleSheet("color: red;")

        self.ui.reconnect_button.setEnabled(not connected)
        self.ui.custom_alert_button.setEnabled(connected)
        self.ui.premade_alert_button.setEnabled(connected)
        self.ui.weather_button.setEnabled(connected)

    def send_ping(self):
        global connected
        try:
            request_server_command("ping one", self.on_ping_response)
        except:
            connected = False
            self.on_connection_result(False)
    
    def on_ping_response(self, data):
       pass

    def update_progress_bar(self):
        global bar_value
        bar_value += 10
        self.ui.connection_bar.setValue(bar_value)
        if bar_value == 100:
            bar_value = 0

class CustomAlertWindow(QMainWindow):
    
    message_updated = Signal(str)
    
    def __init__(self):
        super(CustomAlertWindow, self).__init__()
        self.ui = CustomAlertGUI()
        self.ui.setupUi(self)

        self.ui.send_custom_alert_button.clicked.connect(self.on_send_custom_alert_button_clicked)
        self.ui.custom_to_main_button.clicked.connect(self.on_custom_alert_to_main_button_clicked)
        self.message_updated.connect(self.set_text)
    
    def on_send_custom_alert_button_clicked(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Confirm send")
        msgBox.setText("Are you sure you want to send this message?")
        msgBox.setInformativeText("This will send to all users who have signed up")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.Yes)
        msgBox.setIcon(QMessageBox.Question)
        ret = msgBox.exec()
        if ret == QMessageBox.Yes:
            self.on_confirm()

    def on_confirm(self):
        message = self.format_message()
        request_server_command(f"send_message {message}", lambda x: console_window.log_to_console(x))
        
    def format_message(self):
        message = self.ui.custom_alert_message.toPlainText()
        message = message.replace("\n", "~~~")
        return message
        
    def on_custom_alert_to_main_button_clicked(self):
        stack.setCurrentIndex(0)
        
    def set_text(self, message):
        self.ui.custom_alert_message.setText(message)

class PreMadeAlertWindow(QMainWindow):
    
    ## Signals
    message_updated = Signal(str)
    area_type_updated = Signal(int)
    weather_type_updated = Signal(int)
    duration_updated = Signal(int)
    time_updated = Signal(str)
    severity_updated = Signal(int)
    
    def __init__(self):
        super(PreMadeAlertWindow, self).__init__()
        self.ui = PreMadeAlertGUI()
        self.ui.setupUi(self)

        self.ui.send_premade_alert.clicked.connect(self.on_send_pre_made_alert_button_clicked)
        self.ui.premade_to_main_button.clicked.connect(self.on_pre_made_alert_to_main_button_clicked)
        ## Signals
        self.message_updated.connect(self.set_text)
        self.area_type_updated.connect(self.set_area_type)
        self.weather_type_updated.connect(self.set_weather_type)
        self.duration_updated.connect(self.set_duration)
        self.time_updated.connect(self.set_time)
        self.severity_updated.connect(self.set_severity)


    def on_send_pre_made_alert_button_clicked(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Confirm send")
        msgBox.setText("Are you sure you want to send this message?")
        msgBox.setInformativeText("This will send to all users who have signed up")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.Yes)
        msgBox.setIcon(QMessageBox.Question)
        ret = msgBox.exec()
        if ret == QMessageBox.Yes:
            self.on_confirm()

    def on_confirm(self):
        request_server_command(self.get_command(), lambda x: console_window.log_to_console(x))

    def on_pre_made_alert_to_main_button_clicked(self):
        stack.setCurrentIndex(0)

    def set_text(self, message):
        self.ui.message.setPlainText(message)
        
    def set_area_type(self, area):
        self.ui.area_type.setCurrentIndex(area)
        
    def set_weather_type(self, weather):
        self.ui.weather_type.setCurrentIndex(weather)
    
    def set_duration(self, duration):
        self.ui.duration.setCurrentIndex(duration)
        
    def set_time(self, time):
        self.ui.time.setTime(time)
    
    def set_severity(self, severity):
        self.ui.severity.setCurrentIndex(severity)
        
    def get_command(self):
        area_txt = self.ui.area_type.currentText()
        time_txt = self.ui.time.time().toString()
        weather_txt = self.ui.weather_type.currentText()
        severity_txt = self.ui.severity.currentText()
        duration_txt = self.ui.duration.currentText()
        message = self.ui.message.toPlainText()
        
        formattedMessage = "send_message "
        formattedMessage += f"Area: {area_txt}~~~"
        formattedMessage += f"Time: {time_txt}~~~"
        formattedMessage += f"Weather: {weather_txt}~~~"
        formattedMessage += f"Severity: {severity_txt}~~~"
        formattedMessage += f"Duration: {duration_txt}~~~"
        
        if message != "":
            formattedMessage += f"Message: {message}~~~"
        
        return formattedMessage

class WeatherWindow(QMainWindow):
    is_celsius = True
    
    def __init__(self):
        super(WeatherWindow, self).__init__()
        self.ui = WeatherGUI()
        self.ui.setupUi(self)

        self.ui.weather_to_main_button.clicked.connect(lambda: stack.setCurrentIndex(0))
        self.ui.refresh_weather_button.clicked.connect(self.on_refresh_weather_button_clicked)
        self.ui.celsius_radio.clicked.connect(self.on_celsius_radio_button_clicked)
        self.ui.fahrenheit_radio.clicked.connect(self.on_fahrenheit_radio_button_clicked)
        self.ui.celsius_radio.setChecked(True)
        self.on_celsius_radio_button_clicked()

    def on_refresh_weather_button_clicked(self):
        request_server_command("get_weather all", receive_weather_data)

    def on_celsius_radio_button_clicked(self):
        if self.is_celsius:
            return
        if self.ui.temp_data.text() == "[DATA]":
            return
        fahrenheit = float(self.ui.temp_data.text())
        celsius = round((fahrenheit - 32) * 5/9, 2)
        self.ui.temp_data.setText(str(celsius))
        
        self.is_celsius = True

    def on_fahrenheit_radio_button_clicked(self):
        if not self.is_celsius:
            return
        if self.ui.temp_data.text() == "[DATA]":
            return
        celsius = float(self.ui.temp_data.text())
        fahrenheit = round(celsius * 9/5 + 32, 2)
        self.ui.temp_data.setText(str(fahrenheit))
        
        self.is_celsius = False

    def update_weather_data(self, data):
        self.ui.location_data.setText(data['location']['country'])
        self.ui.condition_data.setText(data['current']['condition']['text'])
        self.ui.cc_data.setText(str(data['current']['condition']['code']))
        self.ui.w_dir_data.setText(data['current']['wind_dir'])
        self.ui.humidity_data.setText(str(data['current']['humidity']))
        self.ui.w_speed_data.setText(str(data['current']['wind_kph']))
        if self.is_celsius:
            self.ui.temp_data.setText(str(data['current']['temp_c']))
        else:
            self.ui.temp_data.setText(str(data['current']['temp_f']))

class ConsoleWindow(QMainWindow):
    def __init__(self):
        super(ConsoleWindow, self).__init__()
        self.ui = ConsoleGUI()
        self.ui.setupUi(self)

        self.ui.console_to_main_button.clicked.connect(self.on_console_to_main_button_clicked)

    def on_console_to_main_button_clicked(self):
        stack.setCurrentIndex(0)
        
    def log_to_console(self, message):
        label = QLabel(message)
        self.ui.scroll_layout.layout().addWidget(label)

## Helper Functions
def receive_weather_data(data):
    data = json.loads(data)
    if data['success']:
        weather_window.update_weather_data(data)
    else:
        console_window.log_to_console("Error: Could not fetch weather data")

def request_server_command(command, callback_function):
    server.sendall(command.encode('utf-8'))
    threading.Thread(target=receive_server_data, args=(callback_function,)).start()

def receive_server_data(callback_function):
    try:
        data = server.recv(1024).decode()
        callback_function(data)
    except Exception as e:
        console_window.log_to_console(f"Error: {e}")

def setup_widgets():
    global stack, server_window, console_window, weather_window, custom_alert_window, premade_alert_window
    stack = QStackedWidget()
    server_window = ServerWindow()
    console_window = ConsoleWindow()
    weather_window = WeatherWindow()
    custom_alert_window = CustomAlertWindow()
    premade_alert_window = PreMadeAlertWindow()

    stack.addWidget(server_window) # 0 
    stack.addWidget(custom_alert_window) # 1
    stack.addWidget(premade_alert_window) # 2
    stack.addWidget(weather_window) # 3
    stack.addWidget(console_window) # 4

    return stack

def run_main():
    global stack
    app = QApplication(sys.argv)
    stack = setup_widgets()
    stack.setWindowTitle("Alert System")
    stack.show()
    sys.exit(app.exec())

# Main Function --------------------------------------------------------------
if __name__ == "__main__":
    run_main()