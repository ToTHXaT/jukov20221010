import os

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

import uvicorn

app = FastAPI()

counter = 0


@app.get("/")
def get_counter():
    return counter


@app.get("/stat")
def get_counter():
    global counter
    counter += 1
    return counter


@app.get("/about")
def hello():
    return HTMLResponse("<h3>Hello, ainur</h3>")


if __name__ == '__main__':
    uvicorn.run(app, port=int(os.getenv("PORT", 5000)))
