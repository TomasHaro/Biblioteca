from fastapi import FastAPI, Depends
from models import country, books, states, users, usr_book_state
from database import engine, Base
from routers import country, states, books, users, usr_book_state, consultas, login


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(login.router)
app.include_router(consultas.router)
app.include_router(country.routerCountry)
app.include_router(states.routerState)
app.include_router(books.routerBooks)
app.include_router(users.routerUsers)
app.include_router(usr_book_state.routerUsrBookState)
