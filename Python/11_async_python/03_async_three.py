import asyncio
import aiohttp

async def fetch_user(session, url):
    async with session.get(url) as response:
        print(f"Fetched {url} with with status {response.status}")

async def main():
    urls = ["https://httpbin.org/delay/2"] * 3
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_user(session, url) for url in urls]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())