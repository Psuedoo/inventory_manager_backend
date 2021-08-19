from typing import Optional
import datetime 

from database.db_handler import DatabaseHandler
from database.models import Computer
from utils.util import generate_computer
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware


handler = DatabaseHandler()
app = FastAPI()


for i in range(50):
    generate_computer(handler, i)

origins = [
    'http://localhost',
    'http://localhost:8000'
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
    time_checked: Optional[datetime.datetime] = None,
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

@app.get("/")
async def root():
    return {'response': 'OK'}

@app.get("/inventory/")
async def get_inventory(commons: dict = Depends(common_parameters)):
    return handler.search(search_props=commons)

@app.post("/inventory/")
async def post_inventory(commons: dict = Depends(common_parameters)):
    try:
        handler.add_computer(commons)
    except Exception as e:
        return {"error": f"{e}"}

# print(handler.search(one='one', two='two', make='Dell', service_tag="10"))

# computer = handler.search(service_tag="10")
# if len(computer) == 1:
#     handler.remove_computer(computer[0])
# else:
#     print("Can't delete multiple computers!")



