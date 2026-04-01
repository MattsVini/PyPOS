from fastapi import FastAPI
import database
import os
from dotenv import load_dotenv

app = FastAPI()
URL_DATABASE = os.environ["URL_DATABASE"]
print(URL_DATABASE)

@app.get("/")
def request_database(URL_DATABASE):
    return database.create_table((URL_DATABASE))

request_database(URL_DATABASE)
