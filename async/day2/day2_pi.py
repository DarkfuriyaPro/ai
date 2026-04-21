import aiohttp
import asyncio

async def fetch_post1(session):
    async with session.get("https://jsonplaceholder.typicode.com/posts/1") as response:
        data = await response.json()
        return data


async def fetch_post2(session):
    async with session.get("https://jsonplaceholder.typicode.com/posts/2") as response:
        data = await response.json()
        return data

async def fetch_post3(session):
    async with session.get("https://jsonplaceholder.typicode.com/posts/3") as response:
        data = await response.json()
        return data

async def main():
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(fetch_post1(session), fetch_post2(session), fetch_post3(session))



asyncio.run(main())