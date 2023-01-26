import sys

sys.path.append("..")

from fastapi_crudrouter import SQLAlchemyCRUDRouter
from database import get_db
from fastapi import Depends
from models.country import Country, CountryCreate, CountryModel
from routers.login import token_auth, token_auth_not_admin

routerCountry = SQLAlchemyCRUDRouter(
    schema=Country,
    create_schema=CountryCreate,
    db_model=CountryModel,
    db=get_db,
    tags=["Country"],
    delete_all_route=[Depends(token_auth)],
    create_route=[Depends(token_auth)],
    update_route=[Depends(token_auth)],
    delete_one_route=[Depends(token_auth)],
    get_one_route=[Depends(token_auth_not_admin)],
    get_all_route=[Depends(token_auth_not_admin)]
)
