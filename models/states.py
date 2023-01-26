from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from pydantic import BaseModel, Field

class StateCreate(BaseModel):
    state_name: str = Field(..., min_length=3, max_length=50)


class State(StateCreate):
    state_id: int
    class Config:
        orm_mode = True

class StateModel(Base):
    __tablename__ = "states"
    state_id = Column(Integer, primary_key=True, index=True)
    state_name = Column(String, unique=True, index=True)
