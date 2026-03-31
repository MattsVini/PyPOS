import psycopg as postgres
from dotenv import load_dotenv
import os
load_dotenv()


def create_table():
    connection = postgres.connect(os.getenv("URL_DATABASE"))
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS shop_owner(
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(100) NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
            )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS product(
        id SERIAL PRIMARY KEY NOT NULL,
        name VARCHAR(100)NOT NULL,
        PRICE DECIMAL(10, 2)NOT NULL,
        QUANTITY INT,
        shop_owner_id REFERENCES shop_owner(id)
        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS sale(
    id SERIAL PRIMARY KEY,
    quantity_sold INT NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    date_sale TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    product_id int REFERENCES product(id),
    shop_owner_id int REFERENCES shop_owner(id)
    )""")

    connection.commit()
    cursor.close()
    connection.close()


