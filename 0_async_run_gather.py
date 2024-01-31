import asyncio
from time import time

async def simulate_task(task_name, duration):
    print(f"{task_name} started")
    await asyncio.sleep(duration)
    print(f"{task_name} completed after {duration} seconds")
    
async def main():
    # Gather all tasks to run concurrently
    tasks = [
        simulate_task("Task 1", 2),
        simulate_task("Task 2", 1),
        simulate_task("Task 3", 3)
    ]

    # Run tasks concurrently
    await asyncio.gather(*tasks)

# Run the event loop
start_time = time()
asyncio.run(main())
print(f"takes{time()-start_time}s")