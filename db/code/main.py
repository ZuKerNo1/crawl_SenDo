import requests
import numpy as np
import pandas as pd
import mysql.connector 
from urllib.parse import urljoin
from fastapi import FastAPI

app = FastAPI()

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="A0934804796",
  database="crawl_sd"
)

cursor = db.cursor()

def insert_to_db(data):
    for product in data["data"]:
      product_id = product["item"]["product_id"]
      name = product["item"]["name"]
      price = product["item"]["price"]
      thumbnail_url = product["item"]["thumbnail_url"]
      shop_name = product["item"]["shop_name"]
      
      sql = ("INSERT INTO product"
                "(product_id, name_product, price, thumbnail_url,shop_name)"
                "VALUES (%d, %s, %f, %s, %s)")
      
      val = (product_id, name, price, thumbnail_url, shop_name)
      cursor.execute(sql, val)
      
    return 

@app.get("/insert_to_db")
def get_data_crawl():
    url = 'localhost:8000/get_data'
    response = requests.request("GET", url)
    data = json.loads(response.text)
    insert_to_db(data)
    return (data)


db.commit()
cursor.close()
db.close()