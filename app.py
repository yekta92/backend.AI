import uvicorn
from fastapi import FastAPI, HTTPException
from schemas import *
from utils import *
import settings
app = FastAPI(lifespan=lifespan)

@app.post("/register")
async def register(userinfo: RegistrationData):
    if user_exists(userinfo.national_code):
        raise HTTPException(status_code=400, detail="a user with this national code already exists")
    create_user(userinfo.first_name, userinfo.last_name, userinfo.national_code, userinfo.medical_number, userinfo.password)
    return { "success": True }


@app.post("/login")
async def login(userinfo: LoginData):
    user = get_user(userinfo.national_code)
    if user == None:
        raise HTTPException(status_code=400, detail="user not found")
    if not verify_password_hash(userinfo.password, user.password):
        raise HTTPException(status_code=400, detail="invalid password")
    return { "success": True, "token": get_user_token({ "national_code": userinfo.national_code, "center": userinfo.center }) }








from datetime import timedelta
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from utils import authenticate_user ,create_access_token, get_current_active_user
from db import *
ACCESS_TOKEN_EXPIRE_MINUTES = 30



@app.post("/chat")
async def chat(userinfo: ChatData):
    national_code = get_user(userinfo.national_code)
    if authenticate_user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    if not national_code.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid national_code header")
    token = national_code.split("Bearer ")[-1]
    national_code = get_current_active_user(token)
    return {"conversation_id": userinfo.conversation_id, "message": userinfo.message, "national_code": userinfo.national_code}




@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = authenticate_user(db, form_data.national_code, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.national_code}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")



@app.get("/users/me/", response_model=Doctor)
async def read_users_me(
    current_user: Annotated[Doctor, Depends(get_current_active_user)],
):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[Doctor, Depends(get_current_active_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]





if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7654)
