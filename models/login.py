from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from pydantic import BaseModel, Field


class LoginCreate(BaseModel):
    token: str = Field(..., min_length=3, max_length=50)
    usr_id: int = Field(gt=0)


class LoginModel(Base):
    __tablename__ = "login"
    login_id = Column(Integer, primary_key=True, index=True)
    token = Column(String, unique=True, index=True)
    usr_id = Column(Integer, ForeignKey("users.usr_id"))

    user = relationship("UsersModel")
