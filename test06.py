import asyncio
from jinja2 import Environment, FileSystemLoader

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("test06.html", {"request": request})

# Queue of HTML response which can be concatenated.
queue = asyncio.Queue()
run = False

@app.post("/start", response_class=HTMLResponse)
async def read_item(request: Request):
    global run
    run = True
    asyncio.create_task(worker( queue))
    return templates.TemplateResponse("test05_start.html", {"request": request})

async def worker(queue):
    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("test05_print.html")
    i = 0
    while i < 20 and run:
        i += 1
        content = template.render({"output": f"Output {i}"})
        queue.put_nowait(content)
        await asyncio.sleep(2)

@app.post("/stop", response_class=HTMLResponse)
async def read_item(request: Request):
    global run
    run = False
    return templates.TemplateResponse("test05_stop.html", {"request": request})

@app.get("/terminal", response_class=HTMLResponse)
async def read_item(request: Request):
    if queue.empty():
        return ("")
    response = ""
    while not queue.empty():
        # Get a "work item" out of the queue.
        response += queue.get_nowait()
        queue.task_done()
    return response
