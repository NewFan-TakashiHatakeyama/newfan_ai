from fastapi import FastAPI
from api.create_model import calc_indicator
app = FastAPI()
app.include_router(calc_indicator.router)

@app.get("/hello")
async def hello():
    return {"message": "hello world!"}