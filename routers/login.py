import sys
import uuid

sys.path.append("..")

from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
import models.users
from models.login import LoginModel
from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return bcrypt_context.hash(password)


def verify_password(plain_password, hashed_password):
    return bcrypt_context.verify(plain_password, hashed_password)


router = APIRouter(
    prefix="/Login",
    tags=["Login"],
    responses={404: {"description": "Not Found"}}
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


def token_auth_not_admin(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    tk = db.query(models.login.LoginModel).filter(models.login.LoginModel.token == token).first()
    if tk:
        return True
    else:
        raise HTTPException(401, "Invalid Token or Not Logged")


def token_auth(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    tk = db.query(models.login.LoginModel).filter(models.login.LoginModel.token == token).first()
    if tk:
        if tk.user.usr_login != "admin":
            raise HTTPException(401, "Not Authorized or Invalid token")
        else:
            return True
    else:
        raise HTTPException(401, "Admin Not Logged or Invalid token")


@router.post("/", status_code=201, response_model=str)
async def login(usr_login: str, usr_passwd: str, db: Session = Depends(get_db)):
    token = uuid.uuid4()
    user = db.query(models.users.UsersModel).filter(models.users.UsersModel.usr_login == usr_login).first()
    if user and verify_password(usr_passwd, user.usr_passwd):
        create_login_model = LoginModel()
        create_login_model.token = token
        create_login_model.usr_id = user.usr_id

        db.add(create_login_model)
        db.commit()
    else:
        raise HTTPException()
    return f'El Token de inicio es: {token}'


@router.delete("/", status_code=200, response_model=str)
async def log_out(db: Session = Depends(get_db)):
    db.query(models.login.LoginModel).delete()
    db.commit()
    return 'Logged Out'
