import asyncio
from concurrent.futures import ProcessPoolExecutor

def encrypt(data):
    return f"🔒{data[::-1]}"

async def main():
    loop = asyncio.get_event_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool,
            encrypt,
            "Credit card XXXX1234"
        )
        print(result)

if __name__ == "__main__":
    asyncio.run(main())