import sys

sys.path.append("..")

import models.users
from routers.login import token_auth_not_admin
from fastapi import APIRouter, Depends, HTTPException
from models import usr_book_state, books
from database import get_db
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(
    prefix="/Special",
    tags=["Special"],
    responses={404: {"description": "Not Found"}}
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


@router.get("/usersByCountry")
async def get_users_by_country(country_id: int, db: Session = Depends(get_db),
                               token: str = Depends(token_auth_not_admin)):
    list_users = db.query(models.users.UsersModel).filter(
        models.users.UsersModel.usr_country_id == country_id).all()
    if len(list_users) > 0:
        list_names = []
        for user in list_users:
            ctry = user.pais.country_name
            list_names.append(user.usr_name)
        return f'En {ctry} hay {len(list_users)} usuario/s: {list_names}'
    else:
        return f'No existen usuarios en el pais indicado'


@router.get("/booksByUser")
async def get_books_by_user(user_id: int, db: Session = Depends(get_db), token: str = Depends(token_auth_not_admin)):
    contador = 0
    user = db.query(models.users.UsersModel).filter(models.users.UsersModel.usr_id == user_id).first()
    prestamos = db.query(models.usr_book_state.usr_book_state_model).filter(
        models.usr_book_state.usr_book_state_model.usr_id == user_id).all()
    list_books = []
    for l in prestamos:
        list_books.append(
            db.query(models.books.BooksModel).filter(models.books.BooksModel.book_id == l.book_id).first())
        if l.state_id == 2:
            contador += 1
    list_names = []
    for l in list_books:
        list_names.append(l.book_name)

    return f'{user.usr_name} tiene {len(prestamos)} libro/s de la biblioteca.: {list_names}. {contador} prestado/s'


@router.get("/booksByUser2")
async def get_books_by_user2(user_id: int, db: Session = Depends(get_db), token: str = Depends(token_auth_not_admin)):
    Contador = 0
    user = db.query(models.users.UsersModel).filter(models.users.UsersModel.usr_id == user_id).first()
    list_books = []
    for l in user.usr_book:
        list_books.append(l.book.book_name)
        if l.state.state_name == "Prestado":
            Contador += 1
    return f'{user.usr_name} tiene {len(list_books)} libro/s de la biblioteca.: {list_books}. {Contador} prestado/s'
