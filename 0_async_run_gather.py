import asyncio
from time import time
from time import sleep

async def asimulate_task(task_name, duration):
    print(f"{task_name} started")
    await asyncio.sleep(duration)
    print(f"{task_name} completed after {duration} seconds")

async def simulate_task(task_name, duration):
    print(f"{task_name} started")
    sleep(duration)
    print(f"{task_name} completed after {duration} seconds")
    
async def amain():
    # Gather all tasks to run concurrently
    tasks = [
        asimulate_task("Task 1", 2),
        asimulate_task("Task 2", 1),
        asimulate_task("Task 3", 3)
    ]

    # Run tasks concurrently
    await asyncio.gather(*tasks)

async def main():
    # Gather all tasks to run concurrently
    tasks = [
        simulate_task("Task 1", 2),
        simulate_task("Task 2", 1),
        simulate_task("Task 3", 3)
    ]
    await asyncio.gather(*tasks)

# Run the event loop
start_time = time()
asyncio.run(amain())
print(f"Run async function\ntakes {time()-start_time}s")

start_time = time()
# main()
asyncio.run(main())
print(f"Run sync function\ntakes {time()-start_time}s")