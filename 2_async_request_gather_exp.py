import asyncio
import aiohttp
import requests

from time import time

async def call_asleep(session, task_name, duration):
    pload = {
        "task_name": task_name,
        "duration": duration
    }

    async with session.post("http://0.0.0.0:9527/synsleep", data=pload) as response:
        # You can handle the response if needed
        print(await response.text())

async def main():
    async with aiohttp.ClientSession() as session:
        # Gather all tasks to run concurrently
        tasks = [
            call_asleep(session, "Task 1", 3),
            call_asleep(session, "Task 2", 1),
            call_asleep(session, "Task 3", 2)
        ]

        # Run tasks concurrentl
        await asyncio.gather(*tasks)



# Run the event loop
start_time = time()
asyncio.run(main())
print(f"Takes {time()-start_time}s")