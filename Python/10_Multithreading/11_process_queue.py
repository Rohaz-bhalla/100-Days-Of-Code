from multiprocessing import Queue, Process

def start_process(queue):
    queue.put("Your process is in execution")

if __name__ == "__main__":
    queue = Queue()

    p = Process(target=start_process, args=(queue,))
    p.start()
    p.join()
    print(queue.get())