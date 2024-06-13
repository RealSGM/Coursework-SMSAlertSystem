import handler, time, pytest

@pytest.mark.parametrize("msg", [
    ("This is an acceptable message"),                         # T2.1.1
    ("This is an acceptable message with a number 123"),       # T2.1.2
    ("Short msg"),                                             # T2.1.3
    ("Message with special characters !@#$%^&*()"),            # T2.1.4
    ("Message with a newline\ncharacter"),                     # T2.1.5
    (r"Message with multiple\nnewlines\n\ncharacters"),         # T2.1.6
    ("A"*2000),                                                # T2.1.7
    ("Message with unicode characters 😔😎"),                # T2.1.8
    (r"Message with tabs\tand spaces"),                         # T2.1.9
])
def test_send_custom_alert(msg):
    def callback_func(data):
        assert data.startswith("+ Alert Sent!")
    
    handler.connect()
    time.sleep(0.5)
    handler.main.server_window.ui.custom_alert_button.click()
    time.sleep(0.5)    
    handler.main.custom_alert_window.message_updated.emit(msg)
    time.sleep(0.5)
    new_msg = handler.main.custom_alert_window.format_message()
    time.sleep(0.5)
    ## Simulate the user clicking the send button and confirming the alert
    handler.main.request_server_command("send_message " + new_msg, callback_func)
    time.sleep(0.5)