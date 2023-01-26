import sys

from routers.login import token_auth, token_auth_not_admin

sys.path.append("..")

from fastapi_crudrouter import SQLAlchemyCRUDRouter
from database import get_db
from fastapi import Depends
from models.states import State, StateCreate, StateModel


routerState = SQLAlchemyCRUDRouter(
    schema=State,
    create_schema=StateCreate,
    db_model=StateModel,
    db=get_db,
    tags=["State"],
    delete_all_route=[Depends(token_auth)],
    create_route=[Depends(token_auth)],
    update_route=[Depends(token_auth)],
    delete_one_route=[Depends(token_auth)],
    get_one_route=[Depends(token_auth_not_admin)],
    get_all_route=[Depends(token_auth_not_admin)]
)
