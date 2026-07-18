import asyncio

async def async_process():
    print("Calculating the estimated time...!")
    await asyncio.sleep(2)
    print("Process is ready...!")

asyncio.run(async_process())