from sqlmodel import SQLModel ,create_engine
import yaml

def connect():
  with open("dev.config.yml", "r") as file:
    config = yaml.safe_load(file)

  config = config["database"]
  
  connection = f"mariadb+mariadbconnector://{config["user"]}:{config["password"]}@{config["host"]}:{config["port"]}/{config["database"]}"
  engine = create_engine(connection)
  return engine


def create_db():
  SQLModel.metadata.create_all(connect())


if __name__ == "__main__":
  create_db()