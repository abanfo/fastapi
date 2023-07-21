
from fastapi import APIRouter,Depends,status
from db import db_vote
from sqlalchemy.orm.session import Session
from db.database import get_db
from typing import List,Optional
from auth.aouth2 import get_current_user
from routers.schemas import VoteBase
from db.model import Vote

router = APIRouter(
    prefix='/vote',
    tags=['vote']
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def vote(vote: VoteBase, db:Session = Depends(get_db), current_user : int= Depends(get_current_user)):
    return db_vote.create(vote=vote,db=db,current_user_id=current_user.id)
