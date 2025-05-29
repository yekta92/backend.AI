from typing_extensions import Annotated
from pydantic import BaseModel, ValidationError, validator
from INCV import CodeValidation as validate_nationalcode
import jwt

from utils import *
from fastapi import Header
from typing import Optional


class RegistrationData(BaseModel):
    first_name: str
    last_name: str
    national_code: str
    medical_number: str
    password: str

    @validator('national_code')
    def check_national_code(cls, v):
        if not validate_nationalcode(v):
            raise ValueError("invalid national code number")
        return v


class LoginData(BaseModel):
    national_code: str
    password: str
    center: str

    @validator('national_code')
    def check_national_code(cls, v):
        if not validate_nationalcode(v):
            raise ValueError("invalid national code number")
        return v
    






class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    national_code: str | None = None


class ChatData(BaseModel):
    conversation_id: str
    message:str
    authorization: Optional[str] = Header(None)

    @validator('authorization_token')
    def check_authorization_token(cls, v):
        if not validate_authorization_token(v):
            raise ValueError("Invalid authorization token")
        return v


