from contextlib import asynccontextmanager
from passlib.context import CryptContext
from fastapi import Depends, FastAPI, HTTPException, status
import jwt
from db import *
from settings import *

from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
import schemas



settings = Settings()
pwd_context = CryptContext(schemes=["sha1_crypt", "scrypt"], deprecated="auto")

@asynccontextmanager
async def lifespan(app: FastAPI):
    db.bind(provider="sqlite", filename="db.sqlite", create_db=True)
    db.generate_mapping(create_tables=True)
    set_sql_debug(True)
    yield

def verify_password_hash(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def user_exists(national_code: str) -> bool:
    with db_session:
        return Doctor.get(national_code=national_code) != None

def get_user(national_code: str):
    with db_session:
        return Doctor.get(national_code=national_code)

def get_user_token(userinfo: dict) -> str:
    return jwt.encode(userinfo, settings.SECRET_KEY, algorithm="HS256")

def create_user(first_name: str, last_name: str, national_code: str, medical_number: str, password: str):
    with db_session:
        doctor = Doctor(first_name=first_name, last_name=last_name, national_code=national_code, medical_number=medical_number, password=get_password_hash(password))





def authenticate_user(db, national_code: str, password: str):
    user = get_user(national_code)
    if not user:
        return False
    if not verify_password_hash(password, user.hashed_password):
        return False
    return user  


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
        national_code: str = payload.get("sub")
        if national_code is None:
            raise credentials_exception
        token_data = schemas.TokenData(national_code=national_code)
    except JWTError:
        raise credentials_exception
    user = get_user(national_code=token_data.national_code)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[Doctor, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user




__all__ = ["lifespan", "user_exists", "create_user", "get_user", "get_user_token", "verify_password_hash" , "validate_authorization_token"]
