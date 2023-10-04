
from fastapi import APIRouter,Depends,status
from db import db_user
from routers.schemas import UserCreate,UserDisplay
from sqlalchemy.orm.session import Session
from db.database import get_db
from typing import List,Optional
from auth.aouth2 import get_current_user

router = APIRouter()

router = APIRouter(
    prefix='/user',
    tags=['user']
)

@router.get('/all', response_model=List[UserDisplay], status_code=status.HTTP_200_OK)
def get_user(db: Session=Depends(get_db),current_user: int = Depends(get_current_user)):
    return db_user.get_all(db=db)
@router.post('', response_model= UserDisplay, status_code=status.HTTP_201_CREATED)
def create(request: UserCreate, db:Session=Depends(get_db)):
    return db_user.create(db=db,request=request)
@router.get('/{id}',response_model=UserDisplay, status_code=status.HTTP_200_OK)
def get_user(id:int,db:Session=Depends(get_db)):
    return db_user.get_user(db=db,id=id)
