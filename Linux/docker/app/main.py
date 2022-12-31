from fastapi import FastAPI
from .triton import run

app = FastAPI()


@app.get("/")
def read_root():
    return run()