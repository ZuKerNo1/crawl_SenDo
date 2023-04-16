import requests
import numpy as np
import pandas as pd
from fastapi import FastAPI
import json

app = FastAPI()

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="anhtuank56",
  database="baoMoi"
)

def insert_to_db(data):
    for product in data["data"]:
      product_id = data['product_id']
      name = data['name']
      price = data['price']
      thumbnail_url = data['thumbnail_url']
      shop_name = data['shop_name']
      
      sql = ("INSERT INTO product_SD"
                "(productID, name, price, thumbnail_url,shop_name)"
                "VALUES (%d, %s, %f, %s, %s)")
      
    return 

@app.get("/insert_to_db")
def get_data_crawl():
    url = 'localhost:8000/get_data'
    response = requests.request("GET", url)
    data = json.loads(response.text)
    insert_to_db(data)
    return (data)


cursor = db.cursor()

db.commit()
cursor.close()
db.close()