from db.model import User
from sqlalchemy.orm.session import Session
from routers.schemas import VoteBase
from db import model
from fastapi import HTTPException, status,Depends
from db.database import get_db


def create(current_user_id :int, vote: VoteBase,db:Session=Depends(get_db)):
    post = db.query(model.Post).filter(model.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'post with id {vote.post_id} doesnt exist')
    vote_query = db.query(model.Vote).filter(model.Vote.post_id == vote.post_id, model.Vote.user_id == current_user_id)
    found_vote = vote_query.first()
    if vote.dir == 1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'User  {current_user_id} has already liked it {vote.post_id}')
        new_vote= model.Vote(post_id= vote.post_id,user_id=current_user_id)
        db.add(new_vote)
        db.commit()
        return {"message": "voted added"}
    else: 
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'vaote not found')
        vote_query.delete(synchronize_session=False)
        db.commit()
        return{"messgae": "deleted"}
        