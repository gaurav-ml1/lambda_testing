from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Updated: FastAPI running on Lambda via Docker 🚀"}

handler = Mangum(app)
