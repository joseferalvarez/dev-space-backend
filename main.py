from fastapi import FastAPI;
from database import connect
import yaml

app = FastAPI();

with open("dev.config.yml", "r") as file:
  config = yaml.safe_load(file)

connection = connect(config["database"])
cursor = connection.cursor()

cursor.execute("INSERT INTO languages (language_name, slug, iso) VALUES ('Spanish', 'spanish', 'es');")
cursor.execute("SELECT * FROM languages")
connection.commit()
connection.close()

for language in cursor:
  print(language)

@app.get("/")
def get_test():
  return {"Hello": "World"}