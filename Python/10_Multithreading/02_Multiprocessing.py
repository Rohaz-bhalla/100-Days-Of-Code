from multiprocessing import Process
import time

def process_start(name):
    print(f"Initializing {name}")
    time.sleep(3)
    print(f"Completed {name} process")

if __name__ == "__main__":
    orders = [
        Process(target = process_start, args = (f"Process logger {i+1}",))
        for i in range(3)
    ]

    #start all the process 
    for p in orders:
        p.start()

    #wait for all to complete
    for p in orders:
        p.join()

        print("All orders completed")