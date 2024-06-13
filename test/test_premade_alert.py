import handler, time, pytest
from PySide6.QtCore import QTime

@pytest.mark.parametrize("msg, area, weather, duration, time_var, severity", [
    ("Test", 1, 2, 3, QTime(12, 0), 3),
    ## Add more test cases
])

def test_premade_alert(msg, area, weather, duration, time_var, severity):
    def callback_func(data):
        assert data.startswith("+ Alert Sent!")

    handler.connect()
    time.sleep(0.5)
    handler.main.server_window.ui.premade_alert_button.click()
    time.sleep(0.5)
    
    handler.main.premade_alert_window.set_text(msg)
    handler.main.premade_alert_window.set_area_type(area)
    handler.main.premade_alert_window.set_weather_type(weather)
    handler.main.premade_alert_window.set_duration(duration)
    handler.main.premade_alert_window.set_time(time_var)
    handler.main.premade_alert_window.set_severity(severity)
    
    command = handler.main.premade_alert_window.get_command()
    handler.main.request_server_command(command, callback_func)