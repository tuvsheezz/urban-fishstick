from pydantic import BaseModel


class Book(BaseModel):
    book_id: int
    title: str
    author: str
