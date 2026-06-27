import streamlit as st
import requests
import hmac
import hashlib
import time
import urllib.parse

st.title("Central de Acúmulo - TAPI v4")

API_KEY = st.secrets["MB_API_KEY"]
API_SECRET = st.secrets["MB_API_SECRET"]

def executar_ordem():
    # URL sem margem para erros
    url = "https://www.mercadobitcoin.net/tapi/v4/"
    
    params = {
        "tapi_method": "place_order",
        "tapi_nonce": str(int(time.time() * 1000)),
        "pair": "BTC-BRL",
        "type": "buy",
        "quantity": "0.0001", # Quantidade mínima para teste
        "limit_price": "200000.00"
    }
    
    params_encoded = urllib.parse.urlencode(params)
    
    # Assinatura HMAC
    signature = hmac.new(API_SECRET.encode('utf-8'), 
                         params_encoded.encode('utf-8'), 
                         hashlib.sha512).hexdigest()
    
    # Adicionando um User-Agent para evitar bloqueio de "robô"
    headers = {
        'TAPI-ID': API_KEY,
        'TAPI-MAC': signature,
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    
    return requests.post(url, data=params_encoded, headers=headers)

if st.button("EXECUTAR COMPRA"):
    try:
        res = executar_ordem()
        st.write(f"Status Code: {res.status_code}")
        if res.status_code == 200:
            st.json(res.json())
        else:
            st.text(res.text[:500]) # Mostra o erro real do servidor
    except Exception as e:
        st.error(e)
        
