from constant import ALGORITHM, SECRET_KEY
from database.db_handler import DatabaseHandler
from utils.util import generate_data
from schemas import *
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException


handler = DatabaseHandler()
app = FastAPI()

manager = LoginManager(SECRET_KEY, '/login')

@manager.user_loader
def query_user(username: str):
    return handler.search('User', {'username': username}).first()

generate_data(handler, 50)

origins = [
    'http://localhost',
    'http://localhost:8000',
    'http://localhost:8080',
    'http://127.0.0.1:5500',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:8080',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Returns OK."""
    return {'response': 'OK'}

@app.post("/login")
def login(data: OAuth2PasswordRequestForm = Depends()):
    username = data.username
    password = data.password

    user = query_user(username)
    if not user:
        raise InvalidCredentialsException
    elif password != user.password:
        raise InvalidCredentialsException

    access_token = manager.create_access_token(
        data=dict(sub=username)
    )
    return {'access_token': access_token, 'token_type': 'bearer'}


@app.get("/protected")
def protected_route(user=Depends(manager)):
    return {'user': user}

@app.get("/inventory/")
async def get_inventory(commons: dict = Depends(computer_common_parameters)):
    """Returns computers"""
    return handler.search('Computer', search_props=commons).all()

@app.post("/inventory/add/", response_model=PostComputer)
async def post_inventory(computer: PostComputer):
    """Adds a computer to the database"""
    print(computer)
    try:
        handler.add_computer(computer)
    except Exception as e:
        return {"error": f"{e}"}

@app.put("/inventory/update/{computer_id}", response_model=PostComputer)
async def update_inventory(computer_id: str, computer: PostComputer):
    """Updates a computer in the database"""
    try:
        handler.update_computer(computer_id, computer)
    except Exception as e:
        return {"error": f"{e}"}

@app.delete("/inventory/delete/{computer_id}", response_model=PostComputer)
async def delete_computer(computer_id):
    """Deletes a computer from the database"""
    try:
        handler.remove_computer(computer_id)
    except Exception as e:
        return {"error": f"{e}"}

@app.get("/users/")
async def get_user(commons: dict = Depends(user_common_parameters)):
    """Returns users"""
    return handler.search('User', search_props=commons).all()

@app.get("/roles/")
async def get_role(commons: dict = Depends(role_common_parameters)):
    """Returns roles"""
    return handler.search('Role', search_props=commons).all()