from contextlib import asynccontextmanager

from fastapi import FastAPI
import database
import os
from dotenv import load_dotenv
app = FastAPI()
@asynccontextmanager
async def lifespan(app):
    URL_DATABASE = os.environ["URL_DATABASE"]
    database.create_table(URL_DATABASE)
    print("done DB!")
    yield

app = FastAPI(lifespan=lifespan)
@app.get("/")
def request_database():
    return {"status: online"}
