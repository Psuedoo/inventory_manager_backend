from typing import Optional
from database.db_handler import DatabaseHandler
from database.models import Computer
from utils.util import generate_computer
from fastapi import FastAPI


handler = DatabaseHandler()
app = FastAPI()

# for i in range(30):
#    generate_computer(handler, i)

@app.get("/")
async def root():
    return {'computers': handler.search()}

@app.get("/inventory/")
async def get_inventory():
    return {'computers': handler.search()}

@app.get("/asset_tag/{asset_tag}")
async def get_asset_tag(asset_tag: int):
    return {'computers': handler.search(asset_tag=asset_tag)}

@app.get("/model/{model}")
async def get_model(model: str):
    model = model.lower().capitalize()
    return {'computers': handler.search(model=model)}

@app.get("/issued/{is_issued}")
async def get_issued(is_issued: Optional[bool] = True):
    return {'computers': handler.search(issued=is_issued)}

@app.get("/issuee/{url_issuee}")
async def get_issuee(url_issuee: str):
    return {'computers': handler.search(issuee=url_issuee)}

@app.get("/on_location/{is_on_location}")
async def get_on_location(is_on_location: Optional[bool] = True):
    return {'computers': handler.search(on_location=is_on_location)}

@app.get("/on_location/location/{location}")
async def get_location(location: str):
    location = location.lower().capitalize()
    return {'computers': handler.search(location=location)}

@app.get("/on_location/class_location/{class_location}")
async def get_class_location(class_location: str):
    return {'computers': handler.search(class_location=class_location)}

@app.get("/service_tag/{service_tag}")
async def get_service_tag(service_tag: str):
    service_tag = service_tag.upper()
    return {'computers': handler.search(service_tag=service_tag)}

@app.get("/make/{make}")
async def get_make(make: str):
    make = make.lower().capitalize()
    return {'computers': handler.search(make=make)}

@app.get("/checker/{checker_name}")
async def get_checker(checker_name: str):
    checker_name = checker_name.lower().capitalize()
    return {'computers': handler.search(checker=checker_name)}

@app.get("/on_hand/{is_on_hand}")
async def get_on_hand(is_on_hand: Optional[bool] = True):
    return {'computers': handler.search(on_hand=is_on_hand)}


# print(handler.search(one='one', two='two', make='Dell', service_tag="10"))

# computer = handler.search(service_tag="10")
# if len(computer) == 1:
#     handler.remove_computer(computer[0])
# else:
#     print("Can't delete multiple computers!")



