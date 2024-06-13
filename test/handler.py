import sys
import os
import threading
import time

main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, main_dir)

import main, server
threading.Thread(target=main.run_main).start()

def connect(ip="127.0.0.1:12345"):
    time.sleep(0.5)
    main.server_window.ui.lineEdit.setText(ip)
    main.server_window.ui.reconnect_button.click()
    time.sleep(0.5)