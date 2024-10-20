import requests
import json
from fastapi import APIRouter
from api.create_model.function import *
router = APIRouter()


@router.post("/create_model_pytorch")
async def create_model_pytorch(uid):
    result = func_create_user_database(uid)
    return result

