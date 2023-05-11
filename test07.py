import asyncio
from jinja2 import Environment, FileSystemLoader

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

class Controller:
    def __init__(self):
        self.state = 0
        self.run = False
        self.queue = asyncio.Queue()
        self.results = ""  # Buffer print

    def start(self):
        self.run = True
        self.results = ""

    def stop(self):
        self.run = False

    def read(self):
        self.results += read_queue()

controller = Controller()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    controller.read()
    return templates.TemplateResponse("test07.html", state_dict({"request": request}))

# Queue of HTML response which can be concatenated.
queue = asyncio.Queue()

def state_dict(d):
    if controller.run:
        d["start_class"] = "is-success is-light"
        d["cancel_class"] = "is-warning"
        d["refresh"] = '<meta http-equiv="refresh" content="1">'  # Poll while running
    else:
        d["start_class"] = "is-success"
        d["cancel_class"] = "is-warning is-light"
        d["refresh"] = ""
    d["results"] = controller.results
    return d

@app.post("/start", response_class=HTMLResponse)
async def read_item(request: Request):
    controller.start()
    asyncio.create_task(model( queue))
    return '<head>  <meta http-equiv="Refresh" content="0; URL=/" /></head>'
    # return templates.TemplateResponse("test07.html", state_dict({"request": request}))

async def model(queue):
    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("test07_print.html")
    i = 0
    while i < 20 and controller.run:
        i += 1
        content = template.render({"output": f"Output {i}"})
        queue.put_nowait(content)
        await asyncio.sleep(2)
    controller.stop()

@app.post("/stop", response_class=HTMLResponse)
async def read_item(request: Request):
    controller.stop()
    return '<head>  <meta http-equiv="Refresh" content="0; URL=/" /></head>'

def read_queue():
    if queue.empty():
        return ""
    response = ""
    while not queue.empty():
        # Get a "work item" out of the queue.
        response += queue.get_nowait()
        queue.task_done()
    return response

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)