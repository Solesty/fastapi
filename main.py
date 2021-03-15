from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"data": {"name": "Adeleke"}}


@app.get("/about")
def about():
    return {"data": {"about page"}}
