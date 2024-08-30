from fastapi import FastAPI;
from database import connect
from sqlmodel import Session, text

app = FastAPI();

engine = connect()

with Session(engine) as session:
  language = session.exec(text("SELECT * FROM languages")).first()
  print(language)

@app.get("/")
def get_test():
  return {"Hello": "World"}