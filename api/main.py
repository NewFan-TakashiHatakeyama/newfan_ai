from fastapi import FastAPI
from api.create_model import pytorch
app = FastAPI()
app.include_router(pytorch.router)

@app.get("/hello")
async def hello():
    return {"message": "hello world!"}