import threading
import time

def monitor_sys():
    while True:
        print(f"Monitoring Tea Temperature")
        time.sleep(2)

t = threading.Thread(target=monitor_sys, daemon=True)
t.start()

print("Main program done")