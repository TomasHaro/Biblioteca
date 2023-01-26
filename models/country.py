from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from pydantic import BaseModel, Field

class CountryCreate(BaseModel):
    country_name: str = Field(..., min_length=3, max_length=50)


class Country(CountryCreate):
    country_id: int
    class Config:
        orm_mode = True


class CountryModel(Base):
    __tablename__ = "country"
    country_id = Column(Integer, primary_key=True, index=True)
    country_name = Column(String, unique=True, index=True)

