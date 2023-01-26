import sys

from routers.login import token_auth, token_auth_not_admin

sys.path.append("..")

from fastapi_crudrouter import SQLAlchemyCRUDRouter
from database import get_db
from fastapi import Depends
from models.usr_book_state import *

routerUsrBookState = SQLAlchemyCRUDRouter(
    schema=usr_book_states,
    create_schema=usr_book_states_create,
    db_model=usr_book_state_model,
    db=get_db,
    tags=["usr_book_state"],
    delete_all_route=[Depends(token_auth)],
    create_route=[Depends(token_auth)],
    update_route=[Depends(token_auth)],
    delete_one_route=[Depends(token_auth)],
    get_one_route=[Depends(token_auth_not_admin)],
    get_all_route=[Depends(token_auth_not_admin)]
)