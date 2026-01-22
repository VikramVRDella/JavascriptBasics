from datetime import datetime, timedelta,timezone
from typing import Annotated
from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from schemas import CreateUserRequest,Token
from starlette import status
from database import get_db
from models import UserModel
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from jose import jwt,JWTError

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


SECRET_KEY = "7d6bd15ba4687538cf051309d1b86e0a5ba0ec8bb72adc8c957254f2d19cd0e6"
ALGORITHM = "HS256"

bcrypt_content = CryptContext(schemes=["argon2"],deprecated='auto')
oauth_bearer = OAuth2PasswordBearer(tokenUrl="/auth/token")

db_dedpendency = Annotated[Session,Depends(get_db)]

@router.post("/",status_code=status.HTTP_201_CREATED)
async def create_user(create_user_request:CreateUserRequest,db:db_dedpendency,):
    create_user_model = UserModel(
        username = create_user_request.username,
        hashed_password = bcrypt_content.hash(create_user_request.password)
    )

    db.add(create_user_model)
    db.commit()

@router.post("/token",response_model=Token)
async def login_for_access_token(form_data:Annotated[OAuth2PasswordRequestForm,Depends()],db:db_dedpendency):
    user = authenticate_user(form_data.username,form_data.password,db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate user")
    token = create_access_token(user.username,user.id,expires_delta=timedelta(minutes=20))
    return{'access_token':token,'token_type':'barrer'}

def authenticate_user(username:str,password:str,db:db_dedpendency):
    user = db.query(UserModel).filter(UserModel.username == username).first()
    if not user:
        return False
    if not bcrypt_content.verify(password,user.hashed_password):
        return False
    return user

def create_access_token(username:str,user_id:int,expires_delta:timedelta):
    encode = {'sub':username,'id':user_id}
    expires=datetime.now(timezone.utc) + expires_delta
    encode.update({'exp':expires})
    return jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)