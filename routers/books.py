import sys
sys.path.append("..")

from routers.login import token_auth, token_auth_not_admin

from fastapi_crudrouter import SQLAlchemyCRUDRouter
from database import get_db
from fastapi import Depends
from models.books import Books, BooksCreate, BooksModel

routerBooks = SQLAlchemyCRUDRouter(
    schema=Books,
    create_schema=BooksCreate,
    db_model=BooksModel,
    db=get_db,
    tags=["Books"],
    delete_all_route = [Depends(token_auth)],
    create_route = [Depends(token_auth)],
    update_route = [Depends(token_auth)],
    delete_one_route = [Depends(token_auth)],
    get_one_route = [Depends(token_auth_not_admin)],
    get_all_route = [Depends(token_auth_not_admin)]

)