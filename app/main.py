from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from app.routers import predict
from app.exceptions import general_exception_handler
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(predict.router)
app.add_exception_handler(Exception, general_exception_handler)

@app.get("/", response_class=HTMLResponse)
def serve_homepage():
    index_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "index.html")
    with open(index_path, "r") as f:
        return f.read()
