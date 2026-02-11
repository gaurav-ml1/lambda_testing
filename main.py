from fastapi import FastAPI
from mangum import Mangum
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    arg1: str
    arg2: str

@app.get("/")
def root():
    return {"message": "Updated: FastAPI running on Lambda via Docker latest"}

@app.post("/post-data")
def print_args(item: Item):
    print(f"arg1: {item.arg1}, arg2: {item.arg2}")
    return {"arg1": item.arg1, "arg2": item.arg2}

handler = Mangum(app)
