import mariadb

def connect(config):
  try:
    connection = mariadb.connect(
      user = config["user"],
      password = config["password"],
      database = config["database"],
      host = config["host"],
      port = int(config["port"])
    )
  except mariadb.Error as e:
    print(e)

  return connection