from pydantic import BaseModel

class UserOut(BaseModel):
    id: int
    firstname: str
    lastname: str
    phone_no: str
    email: str
    password:str


    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    firstname: str
    lastname: str
    phone_no: str
    email: str
    password: str
    confirm_password: str

