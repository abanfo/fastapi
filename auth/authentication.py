from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm.session import Session
from db.database import get_db
from routers.schemas import userlogin
from db.model import User
from db.hashing import Hash
from auth import aouth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from routers.schemas import Token

router = APIRouter(
    tags=['authentication']
)

@router.post('/login', response_model=Token)
def login(user_credentials: OAuth2PasswordRequestForm=Depends(), db: Session = Depends(get_db)):
    
    user = db.query(User).filter(user_credentials.username == User.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f' wrong email')
    
    if not Hash.verify_password(plain_password=user_credentials.password,hashed_password=user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= f'invalid credentials')
    #create taken
    access_token = aouth2.create_access_token(data={'user_id':user.id})
    return{
        "access_token": access_token,
        "user_id": user.id,
        "tokern_type": "bearer"
            }