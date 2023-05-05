from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("test02.html", {"request": request})

@app.post("/mouse_enter", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("test02_hello.html", {"request": request})

@app.post("/mouse_leave", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("test02_mouse.html", {"request": request})
