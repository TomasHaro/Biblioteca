from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from pydantic import BaseModel, Field

class usr_book_states_create(BaseModel):
    usr_id: int = Field(gt=0)
    book_id: int = Field(gt=0)
    state_id: int = Field(gt=0)


class usr_book_states(usr_book_states_create):
    usr_book_state_id: int
    class Config:
        orm_mode = True


class usr_book_state_model(Base):
    __tablename__ = "usr_book_state"
    usr_book_state_id = Column(Integer, primary_key=True, index=True)
    usr_id = Column(Integer, ForeignKey("users.usr_id"), nullable=True)
    book_id = Column(Integer, ForeignKey("books.book_id"), nullable=True)
    state_id = Column(Integer, ForeignKey("states.state_id"), nullable=True)

    book = relationship("BooksModel")
    state = relationship("StateModel")

