import handler, time, pytest

@pytest.mark.parametrize("ip, expected", [
    ("192.168.0.1:8080", True),
    ("127.0.0.1:12345", False)
])

def test_connect(ip, expected):
    handler.connect(ip)
    time.sleep(30)
    assert handler.main.server_window.ui.reconnect_button.isEnabled() == expected