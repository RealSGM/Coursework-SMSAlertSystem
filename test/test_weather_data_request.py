import handler, time

def test_weather_data_request():
    def callback_func(data):
        assert data["success"]
        assert data["location"]["country"] == "Cambodia"
        assert data["location"]["name"] == "Phumi Tanglang"
    
    handler.connect()
    time.sleep(0.5)
    handler.main.server_window.ui.weather_button.click()
    time.sleep(0.5)
    
    ## Simulate the user clicking the get weather button
    handler.main.request_server_command("get_weather all", callback_func)
    time.sleep(0.1)
    