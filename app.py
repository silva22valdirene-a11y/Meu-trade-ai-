import streamlit as st
import requests
import hmac
import hashlib
import time
import urllib.parse

st.title("Central de Acúmulo (DCA) - TAPI V4")

API_KEY = st.secrets["MB_API_KEY"]
API_SECRET = st.secrets["MB_API_SECRET"]

def executar_ordem_tapi(valor_brl, preco_atual):
    url = "https://www.mercadobitcoin.net/tapi/v4/"
    
    params = {
        "tapi_method": "place_order",
        "tapi_nonce": str(int(time.time() * 1000)),
        "pair": "BTC-BRL",
        "type": "buy",
        "quantity": f"{valor_brl / preco_atual:.8f}",
        "limit_price": f"{preco_atual:.2f}"
    }
    
    params_encoded = urllib.parse.urlencode(params)
    path = "/tapi/v4/"
    
    signature = hmac.new(API_SECRET.encode('utf-8'), 
                         (path + '?' + params_encoded).encode('utf-8'), 
                         hashlib.sha512).hexdigest()
    
    headers = {
        'TAPI-ID': API_KEY,
        'TAPI-MAC': signature,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    return requests.post(url, data=params_encoded, headers=headers)

if st.button("EXECUTAR COMPRA TAPI"):
    st.info("Processando...")
    try:
        res = executar_ordem_tapi(25.0, 315000.0)
        
        # Verificação: Tenta exibir o texto bruto se o JSON falhar
        st.write(f"Status Code: {res.status_code}")
        try:
            st.json(res.json())
        except:
            st.error("Resposta do servidor não é JSON. Resposta bruta:")
            st.text(res.text)
            
    except Exception as e:
        st.error(f"Erro na requisição: {e}")
        
