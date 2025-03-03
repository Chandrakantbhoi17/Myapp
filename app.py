from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()



@app.get("/")
def read_root():
    print(22222)
    return {"Hello": "World"}

