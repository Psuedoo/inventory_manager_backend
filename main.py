from database.db_handler import DatabaseHandler
from database.models import Computer
from utils.util import generate_computer
from fastapi import FastAPI


handler = DatabaseHandler()
app = FastAPI()

for i in range(15):
   generate_computer(handler, i)

@app.get("/")
async def root():
    return {'computers': handler.search()}

@app.get("/make/{make}")
async def get_make(make: str):
    make = make.lower().capitalize()
    return {'computers': handler.search(make=make)}

@app.get("/checker/{checker_name}")
async def get_checker(checker_name: str):
    checker_name = checker_name.lower().capitalize()
    return {'computers': handler.search(checker=checker_name)}

# print(handler.search(one='one', two='two', make='Dell', service_tag="10"))

# computer = handler.search(service_tag="10")
# if len(computer) == 1:
#     handler.remove_computer(computer[0])
# else:
#     print("Can't delete multiple computers!")



