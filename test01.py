from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    response = "Hello world"
    return response
