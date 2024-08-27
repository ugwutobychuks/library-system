from pydantic import BaseModel
from datetime import date

class MemberBase(BaseModel):
    name: str
    membership_date: date
    membership_type: str

class MemberCreate(MemberBase):
    pass

class Member(MemberBase):
    id: int
    class Config:
        orm_mode = True

class BookBase(BaseModel):
    title: str
    author: str

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    class Config:
        orm_mode = True

class BorrowingBase(BaseModel):
    member_id: int
    book_id: int
    issue_date: date
    due_date: date
    return_date: date = None

class BorrowingCreate(BorrowingBase):
    pass

class Borrowing(BorrowingBase):
    id: int
    class Config:
        orm_mode = True

class FineBase(BaseModel):
    member_id: int
    amount: float
    paid: float
    outstanding: float

class FineCreate(FineBase):
    pass

class Fine(FineBase):
    id: int
    class Config:
        orm_mode = True
