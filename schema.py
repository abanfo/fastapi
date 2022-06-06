from pydantic import BaseModel


class UserDBase(BaseModel):
    username: str
    email:str
    password: str