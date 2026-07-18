from multiprocessing import Process
import time

def process_manager():
    print(f"started brewing...")
    count = 0
    for _ in range(100_000_000):
        count =+ 1
    print(f"finished brewing...")

if __name__ == "__main__":
    start = time.time()

    p1 = Process(target=process_manager)
    p2= Process(target=process_manager)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time.time()

    print(f"Total time with multi-processing is {end - start:.2f} seconds")
