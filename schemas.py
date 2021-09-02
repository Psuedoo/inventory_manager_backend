from pydantic import BaseModel
from typing import Optional
from datetime import datetime 


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
    checker: int
    time_checked: Optional[datetime] = None
    notes: str

    class Config:
        orm_mode = True


class PostUser(BaseModel):
    name: str
    username: str
    email: str
    role: int

    class Config:
        orm_mode = True


class PostRole(BaseModel):
    name: str

    class Config:
        orm_mode = True


async def computer_common_parameters(
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

async def user_common_parameters(
    name: Optional[str] = None,
    username: Optional[str] = None,
    password: Optional[str] = None,
    email: Optional[str] = None,
    role: Optional[int] = None,
):
    return {
        "name": name,
        "username": username,
        "password": password,
        "email": email,
        "role": role
    }

async def role_common_parameters(
    name: Optional[str] = None,
):
    return {
        "name": name
    }
