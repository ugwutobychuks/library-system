from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, schemas, models, database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.post("/members/", response_model=schemas.Member)
def create_member(member: schemas.MemberCreate, db: Session = Depends(database.get_db)):
    return crud.create_member(db=db, member=member)

@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(database.get_db)):
    return crud.create_book(db=db, book=book)

@app.get("/books/", response_model=list[schemas.Book])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    books = crud.get_books(db=db)
    return books
