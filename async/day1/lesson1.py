import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(2)
    print("Hello after 2 seconds")

async def say_bye():
    print("Bye")
    await asyncio.sleep(1)
    print("Bye after 1 second")

async def main():
    await say_hello()
    await say_bye()

asyncio.run(main())