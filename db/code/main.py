import requests
import numpy as np
import pandas as pd
from fastapi import FastAPI
import json
import mysql.connector
import datetime

app = FastAPI()



def insert_to_db(data):

  insert = 0
  update = 0
  deleted = 0
  db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="anhtuan2709_",
  database="baomoi"
  )
  cursor = db.cursor()
  sql_select_all = ("Select * from product_sd")
  cursor.execute(sql_select_all)
  result_all = cursor.fetchall()
  data_list = []
  for x in result_all:
    data_list.append(x) 
  #get single data from json file
  product_id_list =[]
  for product in data["data"]:
    product_id = str(product['item']['product_id'])
    name = str(product['item']['name'])
    price = str(product['item']['price'])
    thumbnail_url =str(product['item']['thumbnail_url'])
    shop_name = str(product['item']['shop_name'])
    
    product_id_list.append(product_id)
    # sql1 = ("Select * from product_sd where productID = '"+product_id+"'")
    # cursor.execute(sql1)
    # result = cursor.fetchall()
    data_list_row = [] #get exist row from db
    for x in data_list:
      if x[0]==product_id:
        data_list_row.append(x)
    if (len(data_list_row)==0): #add new data
      sql = ("INSERT INTO product_sd"+ " VALUES ('"+product_id+"','"+name+"','"+price+"','"+thumbnail_url+"','"+shop_name+"')")
      cursor3 = db.cursor()
      cursor3.execute(sql)
      insert=insert+1
    else: #update old data
      for x in data_list_row:
        if(x[1]!=name or x[2]!= price or x[3]!= thumbnail_url or x[4]!=shop_name):
            sql = ("update product_sd set name = '"+name+"', price = '"+price+"', thumbnail_url ='"+thumbnail_url+"', shop_name='"+shop_name+"' where productID = '"+product_id+"'")
            cursor2 = db.cursor()
            cursor2.execute(sql)
            update = update+1
    
  #delete data in old crawl time
  for x in data_list:
    if (x[0] not in product_id_list
    ):
      cursor_del = db.cursor()
      sql_del=("delete  from baomoi.product_sd where productID = '"+x[0]+"'")
      cursor_del.execute(sql_del)
      deleted=deleted+1
    
  db.commit()
  cursor.close()
  db.close()
    
  return {'crawl_time': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),'inserted': insert, 'updated': update,'deleted': deleted}

def count_row(cursor):
  count =0
  for x in cursor:
    count = count+1
  return count
@app.get("/insert_to_db")
def get_data_crawl():
    url = 'http://127.0.0.1:8000/get_data'
    response = requests.request("GET", url)
    data = json.loads(response.text)
    result=insert_to_db(data)
    return (result)





