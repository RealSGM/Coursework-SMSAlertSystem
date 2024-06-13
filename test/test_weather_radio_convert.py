import handler, time

def f_to_c(f):
    return (f - 32) * 5/9

def c_to_f(c):
    return c * 9/5 + 32

def test_weather_radio_convert():
    handler.connect()
    time.sleep(0.5)
    handler.main.server_window.ui.weather_button.click()
    time.sleep(0.5)
    handler.main.weather_window.on_refresh_weather_button_clicked()
    time.sleep(0.1)
    
    current_value = handler.main.weather_window.ui.temp_data.text()
    expected_value = None
    
    if handler.main.weather_window.is_celsius:
        expected_value = c_to_f(float(current_value))
        handler.main.weather_window.ui.fahrenheit_radio.click()
    else:
        expected_value = f_to_c(float(current_value))
        handler.main.weather_window.ui.celsius_radio.click()
    
    time.sleep(0.1)
    new_value = handler.main.weather_window.ui.temp_data.text()
    
    assert round(float(new_value), 2) == round(expected_value, 2)