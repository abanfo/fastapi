from fastapi import APIRouter,Depends
from db import db_post
from routers.schemas import PostCreate,PostDisplay
from sqlalchemy.orm.session import Session
from db.database import get_db
from typing import List,Optional
from auth.aouth2 import get_current_user


router = APIRouter(
    prefix='/post',
    tags=['post']
)
@router.get('/all', response_model= List[PostDisplay])
def get_all(db:Session=Depends(get_db),current_user: int = Depends(get_current_user), limit:int=4):
    return db_post.get_all(db=db, limit=limit)
@router.get('/{id}')
def get_post(id:int,db:Session=Depends(get_db),current_user: int = Depends(get_current_user)):
    return db_post.get_post(id=id,db=db)
@router.post('/create', response_model=PostDisplay)
def create(request: PostCreate,db: Session=Depends(get_db), current_user: int = Depends(get_current_user)):
    return db_post.create(db=db,request=request, owner_id=current_user.id )
@router.delete('/delete/{id}')
def delete_post(id: int, db:Session=Depends(get_db),current_user: int = Depends(get_current_user)):
    return db_post.delete(id=id,db=db, user_id=current_user.id)
@router.put('/update/{id}', response_model=PostDisplay)
def update(id: int,request:PostCreate,db: Session=Depends(get_db),current_user: int = Depends(get_current_user)):
    return db_post.update_post(id=id,request=request,db=db,user_id=current_user.id)




