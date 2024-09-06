import os
import json

if __name__ == '__main__':
  app = json.load(open("db-config.json"))
  print(app['database_host'])
  print(app['database_port'])