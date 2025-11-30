# Demonstrates an async generator and how to properly use it with an event loop.

import asyncio


async def async_numbers():
    for i in range(3):
        await asyncio.sleep(0.1)  # Simulate async work
        yield i


async def main():
    async for num in async_numbers():
        print(num)


# Run the async main function
asyncio.run(main())
