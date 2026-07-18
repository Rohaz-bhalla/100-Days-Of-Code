import asyncio
import time

async def brew(name):
    print(f"brewing your {name} coffee")
    await asyncio.sleep(3)
    time.sleep(3)
    print(f"Your {name} coffee is ready...")

async def main():
    await asyncio.gather(
        brew("Vietnamese coffee"),
        brew("Cold coffee"),
        brew("Black coffee"),
    )

asyncio.run(main())