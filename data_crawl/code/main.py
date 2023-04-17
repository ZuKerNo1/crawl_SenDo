import pandas as pd
from fastapi import FastAPI
import requests
import json

data = []

app = FastAPI()

@app.get("/get_data")

def get_data():
    # crawl data
    url = "https://recommend-api.sendo.vn/web/listing/recommend/internal?track_id=948778d8-079f-4a5c-9865-ee19e1c73aec&p=1&s=100&cate_path=do-boi&category_id=63&sort_type=vasup_desc&platform=desktop2&app_verion=2.29.51&session_key=1681739587797&version=v2&is_new_listing=2"
    payload={}
    headers = {
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)

    return (data)



print(data)
        













