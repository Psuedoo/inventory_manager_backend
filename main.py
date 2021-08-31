from typing import Optional
from datetime import datetime 

from database.db_handler import DatabaseHandler
from utils.util import generate_data
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from schemas import *


handler = DatabaseHandler()
app = FastAPI()

generate_data(handler, 50)

origins = [
    'http://localhost',
    'http://localhost:8000',
    'http://localhost:8080'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {'response': 'OK'}

@app.get("/inventory/")
async def get_inventory(commons: dict = Depends(computer_common_parameters)):
    return handler.search('Computer', search_props=commons)

@app.post("/inventory/add/", response_model=PostComputer)
async def post_inventory(computer: PostComputer):
    print(computer)
    try:
        handler.add_computer(computer)
    except Exception as e:
        return {"error": f"{e}"}

@app.put("/inventory/update/{computer_id}", response_model=PostComputer)
async def update_inventory(computer_id: str, computer: PostComputer):
    try:
        handler.update_computer(computer_id, computer)
    except Exception as e:
        return {"error": f"{e}"}

@app.delete("/inventory/delete/{computer_id}", response_model=PostComputer)
async def delete_computer(computer_id):
    try:
        handler.remove_computer(computer_id)
    except Exception as e:
        return {"error": f"{e}"}

@app.get("/users/")
async def get_user(commons: dict = Depends(user_common_parameters)):
    return handler.search('User', search_props=commons)

@app.get("/user/{user_id}/computers/")
async def get_user_by_id(user_id):
    return handler.search('User', {'id': user_id})[0].computers