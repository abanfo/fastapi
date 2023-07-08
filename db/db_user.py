from db.model import User
from sqlalchemy.orm.session import Session
from routers.schemas import UserCreate,UserBase
from db.model import User
import datetime
from db.hashing import Hash
from fastapi import HTTPException, status
def create(db: Session,request: UserBase):

    new_user= User(
        email= request.email,
        password = Hash.get_password_hash(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
def get_all(db: Session):
    return db.query(User).all()

def get_user(id : str, db = Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f' user with id {id} not found')
    return user