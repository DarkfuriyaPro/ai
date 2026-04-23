import aiohttp
import asyncio

urls = ["https://jsonplaceholder.typicode.com/posts/1", "https://jsonplaceholder.typicode.com/posts/2", "https://jsonplaceholder.typicode.com/posts/3"]

async def fetch(url, session):
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return data
                else:
                    return None
        except:
            print("Request failed")

def process(results):
    for r in results:
        if r is not None: 
            print(r)
        else:
            print("failed")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(fetch(url, session))
        results =  await asyncio.gather(*tasks)
        process(results)

        

asyncio.run(main())