from fastapi import FastAPI
from database import connect, create_db
from src.languages.router import get_language_router

app = FastAPI()


engine = connect()
create_db()


app.include_router(get_language_router())
