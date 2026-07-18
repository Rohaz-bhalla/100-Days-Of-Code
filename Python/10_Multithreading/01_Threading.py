import threading
import time

def take_bookings():
    for i in range(1,4):
        print(f"Taking order for #{i}")
        time.sleep(2)

def brew_coffee():
    for i in range(1,4):
        print(f"Taking order for #{i}")
        time.sleep(3)

#Creating Threads
order_thread = threading.Thread(target = take_bookings)
brew_thread  = threading.Thread(target = brew_coffee)

order_thread.start()
brew_thread.start()

#wait for both to finish
order_thread.join
brew_thread.join

print(f"All orders Completed successfully...!")