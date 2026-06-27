import streamlit as st
import requests
import hmac
import hashlib
import time
import urllib.parse

st.title("Central de Acúmulo (DCA)")

# Chaves
API_KEY = st.secrets["MB_API_KEY"]
API_SECRET = st.secrets["MB_API_SECRET"]

def assinar_e_executar():
    # 1. Preparar os dados
    path = "/tapi/v3/"
    tonce = str(int(time.time() * 1000))
    params = {
        "tapi_method": "place_order",
        "tapi_nonce": tonce,
        "pair": "BTC-BRL",
        "type": "buy",
        "quantity": "0.0001",
        "limit_price": "315000"
    }
    
    # 2. Assinatura
    params_encoded = urllib.parse.urlencode(params)
    signature = hmac.new(API_SECRET.encode('utf-8'), 
                         (path + '?' + params_encoded).encode('utf-8'), 
                         hashlib.sha512).hexdigest()
    
    headers = {
        'TAPI-ID': API_KEY,
        'TAPI-MAC': signature,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    # 3. Execução
    response = requests.post("https://www.mercadobitcoin.net" + path, data=params_encoded, headers=headers)
    return response

# Interface
if st.button("EXECUTAR COMPRA REAL"):
    st.warning("Enviando ordem...")
    try:
        res = assinar_e_executar()
        if res.status_code == 200:
            st.success("Resposta do servidor:")
            st.json(res.json())
        else:
            st.error(f"Erro {res.status_code}: {res.text}")
    except Exception as e:
        st.error(f"Erro de execução: {e}")
      
