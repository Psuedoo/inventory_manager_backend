from typing import Optional
from datetime import datetime 

from database.db_handler import DatabaseHandler
from database.models import Computer, Role, User
from utils.util import generate_data
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


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


async def common_parameters(
    make: Optional[str] = None,
    model: Optional[str] = None,
    service_tag: Optional[str] = None,
    asset_tag: Optional[str] = None,
    issued: Optional[bool] = None,
    assigned_to: Optional[str] = None,
    on_hand: Optional[bool] = None,
    on_location: Optional[bool] = None,
    computer_location: Optional[str] = None,
    class_location: Optional[str] = None,
    checker: Optional[str] = None,
    time_checked: Optional[datetime] = None,
    notes: Optional[str] = None

):
    return {
        "make": make,
        "model": model,
        "service_tag": service_tag,
        "asset_tag": asset_tag,
        "issued": issued,
        "assigned_to": assigned_to,
        "on_hand": on_hand,
        "on_location": on_location,
        "computer_location": computer_location,
        "class_location": class_location,
        "checker": checker,
        "time_checked": time_checked,
        "notes": notes,
    }

class PostComputer(BaseModel):
    make: str
    model: str 
    service_tag: str 
    asset_tag: str 
    issued: bool 
    assigned_to: str 
    on_hand: bool 
    on_location: bool 
    computer_location: str 
    class_location: str
    checker: str
    time_checked: Optional[datetime] = None
    notes: str

    class Config:
        orm_mode = True

@app.get("/")
async def root():
    return {'response': 'OK'}

@app.get("/inventory/")
async def get_inventory(commons: dict = Depends(common_parameters)):
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
