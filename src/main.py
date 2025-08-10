from fastapi import FastAPI

from src.books.router import router as books_router

app = FastAPI()

app.include_router(books_router, prefix="/books", tags=["books"])
