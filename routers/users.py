import sys

sys.path.append("..")

from routers.login import token_auth, token_auth_not_admin, get_password_hash
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from database import get_db
from fastapi import Depends, HTTPException
import models
from models.users import Users, UsersModel, UsersCreate
from sqlalchemy.orm import Session

routerUsers = SQLAlchemyCRUDRouter(
    schema=Users,
    create_schema=UsersCreate,
    db_model=UsersModel,
    db=get_db,
    tags=["Users"],
    delete_all_route=[Depends(token_auth)],
    create_route=False,
    update_route=False,
    delete_one_route=[Depends(token_auth)],
    get_one_route=[Depends(token_auth_not_admin)],
    get_all_route=[Depends(token_auth_not_admin)],
)


@routerUsers.post('')
async def create_user(user: UsersCreate, token: str = Depends(token_auth), db: Session = Depends(get_db)):
    create_user_model = models.users.UsersModel()
    create_user_model.usr_login = user.usr_login
    create_user_model.usr_name = user.usr_name
    create_user_model.usr_lastname = user.usr_lastname
    create_user_model.usr_country_id = user.usr_country_id

    hash_password = get_password_hash(user.usr_passwd)

    create_user_model.usr_passwd = hash_password

    db.add(create_user_model)
    db.commit()


@routerUsers.put('/{usr_id}')
async def update_user(usr_id: int, user: UsersCreate, token: str = Depends(token_auth), db: Session = Depends(get_db)):
    user_model = db.query(models.users.UsersModel).filter(models.users.UsersModel.usr_id == usr_id).first()
    if user_model is not None:
        user_model.usr_login = user.usr_login
        user_model.usr_name = user.usr_name
        user_model.usr_lastname = user.usr_lastname
        user_model.usr_country_id = user.usr_country_id

        hash_password = get_password_hash(user.usr_passwd)

        user_model.usr_passwd = hash_password

        db.add(user_model)
        db.commit()


"""
@routerUsers.delete("/")
async def delete_all_users(token: str = Depends(token_auth), db: Session = Depends(get_db)):
    if token:
        db.query(models.users.UsersModel).filter(models.users.UsersModel.usr_id != 1).delete()
        db.commit()
        return 'Users deleted'
    else:
        raise HTTPException(401, "Not Authorized or Invalid token")

@routerUsers.delete("/")
async def delete_one_user(usr_id: int, token: str = Depends(token_auth), db: Session = Depends(get_db)):
    if usr_id == 1:
        return 'Admin user cannot be deleted'
    if token:
        db.query(models.users.UsersModel).filter(models.users.UsersModel.usr_id == usr_id).delete()
        db.commit()
        return 'User deleted'
    else:
        raise HTTPException(401, "Not Authorized or Invalid token")
"""
