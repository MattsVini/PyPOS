from contextlib import asynccontextmanager
from account import Account
from fastapi import FastAPI
import database
import os


@asynccontextmanager
async def lifespan(app):
    database.create_table()
    print("done DB!")
    print("Register!")
    name = "Test"
    email = "test@test"
    password = "test1234-H@)DF"
    password_hash = Account.hash_password(password)
    auth_register = database.register_account(name, email, password_hash)
    print(auth_register)
    yield

    print("Shutting down")


app = FastAPI(lifespan=lifespan)


@app.get("/")
def request_database():
    return {"status": "online"}
