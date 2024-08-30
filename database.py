from sqlmodel import create_engine
import yaml

def connect():
  with open("dev.config.yml", "r") as file:
    config = yaml.safe_load(file)

  config = config["database"]
  
  connection = f"mariadb+mariadbconnector://{config["user"]}:{config["password"]}@{config["host"]}:{config["port"]}/{config["database"]}"
  engine = create_engine(connection)
  return engine
