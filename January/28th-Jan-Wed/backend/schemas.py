from pydantic import BaseModel
from typing import Optional

class AddressModel(BaseModel):
    city:str
    state:str
    zip_code:int

class AddressCreate(AddressModel):
    pass

class AddressResponse(AddressModel):
    id:int
    class config:
        orm_mode:True

class UserModel(BaseModel):
    name:str
    age:int

class UserCreate(UserModel):
    address:Optional[list[AddressCreate]]
    pass

class UserResponse(UserModel):
    id:int
    address:list[AddressResponse] = []
    class config:
        orm_mode:True
