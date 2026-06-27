import requests
import streamlit as st

# Exemplo para pegar o preço atual (Ticker) sem precisar de CCXT
def get_price():
    url = "https://api.mercadobitcoin.net/api/v4/tickers?symbols=BTC-BRL"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['tickers'][0]['last']
    return None

st.write("Preço atual do BTC:", get_price())
