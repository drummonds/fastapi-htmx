from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("test04.html", {"request": request})

@app.post("/mouse_hello", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("test04_hello.html", {"request": request})

@app.post("/restore", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("test04_restore.html", {"request": request})
