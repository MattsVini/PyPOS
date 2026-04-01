from fastapi import FastAPI
import database
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()
def create_table():
    database.create_table()

create_table()