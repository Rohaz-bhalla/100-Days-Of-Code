import asyncio
import threading
import time

def bgworker():
    while True:
        time.sleep
        print(f"Logging the system health")

async def fetch_orders():
    await asyncio.sleep(3)
    print("Order Returned")

threading.Thread(target=bgworker, daemon=True).start()

if __name__ == "__main__":
    asyncio.run(fetch_orders())