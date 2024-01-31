import asyncio
import requests

from time import time

async def call_sleep(task_name, duration):
    pload = {
        "task_name": task_name,
        "duration": duration
    }
    print(task_name)
    # async with requests.post("http://0.0.0.0:9527/asynsleep", data=pload, timeout=300) as response:
    #     # You can handle the response if needed
    #     print(await response.json())
    response = requests.post("http://0.0.0.0:9527/asynsleep", params=pload, timeout=300)
    print(response.json())


async def sync_main():
    # Gather all tasks to run concurrently
    tasks = [
        call_sleep("Task 1", 3),
        call_sleep("Task 2", 1),
        call_sleep("Task 3", 2)
    ]

    # Run tasks concurrentl
    await asyncio.gather(*tasks)



# Run the event loop
start_time = time()
asyncio.run(sync_main())
print(f"Takes {time()-start_time}s")