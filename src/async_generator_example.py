# Async generators need `async for` and event loop;
# mixing with normal ones causes issues.

import asyncio


async def async_numbers():
    for i in range(3):
        await asyncio.sleep(0.1)  # Simulate async work
        yield i


# Fails if used like normal generator
# for num in async_numbers():
#     print(num)


async def main():
    async for num in async_numbers():
        print(num)


# Run the async main function
asyncio.run(main())
