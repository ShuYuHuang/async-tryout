from fastapi import FastAPI, Form
import asyncio
from time import sleep

app = FastAPI()


@app.post("/asynsleep")
async def asynsleep(
    task_name: str = Form(...),
    duration: int = Form(...)):
    print(f"{task_name} started")
    await asyncio.sleep(duration)
    print(f"{task_name} completed after {duration} seconds")
    return {"respond": task_name+"over"}


@app.post("/synsleep")
def synsleep(
    task_name: str = Form(...),
    duration: int = Form(...)):
    print(f"{task_name} started")
    sleep(duration)
    print(f"{task_name} completed after {duration} seconds")
    return {"respond": task_name+"over"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', reload_dirs='.', port=9527)