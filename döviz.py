import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

API_URL = "https://api.exchangerate.host/live?access_key=136522fdd1e2e34f2293e78999fcdc2d&format=1"

def get_exchange_data(base_currency: str, target_currency: str):
    params = {
        'access_key': '136522fdd1e2e34f2293e78999fcdc2d',  
        'source': base_currency,
        'currencies': target_currency,
        'format': 1
    }
    response = requests.get(API_URL, params=params)
    data = response.json()
    
    if data.get('success'):
        
        rate = data['quotes'][f'{base_currency}{target_currency}']
        return rate
    else:
        raise Exception(f"Veri alınamadı: {data['error']['info']}")


base_currency = input("Baz döviz (örneğin: USD): ").upper()
target_currency = input("Hedef döviz (örneğin: TRY): ").upper()

try:
    exchange_rate = get_exchange_data(base_currency, target_currency)
    
    print(f"{base_currency}/{target_currency} kuru: {exchange_rate}")
except Exception as e:
    print(e)
