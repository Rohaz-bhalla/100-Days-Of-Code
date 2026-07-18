import threading
import time

def process_execution(type_, wait_time):
    print(f"{type_} process in call stack...")
    time.sleep(wait_time)
    print(f"{type_} process done...")

t1 = threading.Thread(target=process_execution, args=("node.js",2))
t2 = threading.Thread(target=process_execution, args=("Java",3))

t1.start()
t2.start()

t1.join()
t2.join()