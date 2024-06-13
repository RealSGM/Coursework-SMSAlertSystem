import handler, time, pytest

@pytest.mark.parametrize("ui_button, expected_index", [
    ("weather_button", 3),
    ("console_button", 4),  
    ("premade_alert_button", 2),  
    ("custom_alert_button", 1)
])

def test_ui_button(ui_button, expected_index):
    handler.connect()
    time.sleep(0.5)
    button = getattr(handler.main.server_window.ui, ui_button)
    button.click()
    time.sleep(0.5)
    assert handler.main.stack.currentIndex() == expected_index  