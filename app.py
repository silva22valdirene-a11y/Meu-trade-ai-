import streamlit as st
import requests
import hmac
import hashlib
import time
import urllib.parse

st.title("Central de Acúmulo (DCA) - TAPI V4")

# Certifique-se de que MB_API_KEY e MB_API_SECRET estão nos Secrets do Streamlit Cloud
API_KEY = st.secrets["MB_API_KEY"]
API_SECRET = st.secrets["MB_API_SECRET"]

def executar_ordem_tapi(valor_brl, preco_atual):
    url = "https://www.mercadobitcoin.net/tapi/v4/"
    
    # Parâmetros da TAPI
    params = {
        "tapi_method": "place_order",
        "tapi_nonce": str(int(time.time() * 1000)),
        "pair": "BTC-BRL",
        "type": "buy",
        "quantity": f"{valor_brl / preco_atual:.8f}",
        "limit_price": f"{preco_atual:.2f}"
    }
    
    params_encoded = urllib.parse.urlencode(params)
    
    # Assinatura (Path + ? + Params)
    signature = hmac.new(API_SECRET.encode('utf-8'), 
                         ("/tapi/v4/?" + params_encoded).encode('utf-8'), 
                         hashlib.sha512).hexdigest()
    
    headers = {
        'TAPI-ID': API_KEY,
        'TAPI-MAC': signature,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    return requests.post(url, data=params_encoded, headers=headers)

# Interface
if st.button("EXECUTAR COMPRA TAPI"):
    st.info("Processando...")
    try:
        # Exemplo com preco fixo ou busque o real
        res = executar_ordem_tapi(25.0, 315000.0) 
        st.write(res.json())
    except Exception as e:
        st.error(str(e))
        
