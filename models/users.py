from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from pydantic import BaseModel, Field

class UsersCreate(BaseModel):
    usr_login: str = Field(..., min_length=3, max_length=50)
    usr_name: str = Field(..., min_length=3, max_length=50)
    usr_lastname: str = Field(..., min_length=3, max_length=50)
    usr_passwd: str = Field(..., min_length=3, max_length=50)
    usr_country_id: int = Field(gt=0)


class Users(UsersCreate):
    usr_id: int
    class Config:
        orm_mode = True



class UsersModel(Base):
    __tablename__ = "users"

    usr_id = Column(Integer, primary_key=True, index=True)
    usr_login = Column(String, unique=True, index=True)
    usr_name = Column(String)
    usr_lastname = Column(String)
    usr_passwd = Column(String)
    usr_country_id = Column(Integer, ForeignKey("country.country_id"), nullable=True)

    pais = relationship("CountryModel")
    usr_book = relationship("usr_book_state_model")