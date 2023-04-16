import pandas as pd
from fastapi import FastAPI
import requests
import json

data = []

app = FastAPI()

@app.get("/get_data")

def get_data():
    # crawl data
    url = "https://recommend-api.sendo.vn/web/home/recommend/external?p=10&s=60&track_id=cd161bcd-91ac-47ff-b0a9-56c80e7cdf39&platform=desktop2&app_version=2.29.51&inventory_id=&advertising_id=&session_key=1681640169279"
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
        













