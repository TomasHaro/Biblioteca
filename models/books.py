from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from pydantic import BaseModel, Field

class BooksCreate(BaseModel):
    book_name: str = Field(..., min_length=3, max_length=50)
    book_description: str = Field(..., min_length=10, max_length=500)


class Books(BooksCreate):
    book_id: int
    class Config:
        orm_mode = True


class BooksModel(Base):
    __tablename__ = "books"
    book_id = Column(Integer, primary_key=True, index=True)
    book_name = Column(String, unique=True, index=True)
    book_description = Column(String)

