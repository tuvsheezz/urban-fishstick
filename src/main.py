from fastapi import FastAPI

from authors.router import router as authors_router
from books.router import router as books_router

app = FastAPI()

app.include_router(books_router, prefix="/books", tags=["books"])
app.include_router(authors_router, prefix="/authors", tags=["authors"])
