from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserDisplay(BaseModel):
    id:str
    email: str
    password: str 
    class Config:
        orm_mode = True

class PostDisplay(PostBase):
    created_at: datetime
    owner_id: int 
    owner : UserDisplay
    class Config:
        orm_mode = True
        
class UserBase(BaseModel):
    email: EmailStr
    password: str
class UserCreate(UserBase):
    pass

class userlogin(BaseModel):
    email: EmailStr
    password: str
class Token(BaseModel):
    access_token: str
    token_type = str
class TokenData(BaseModel):
    id :Optional[str] = None


