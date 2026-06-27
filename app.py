import streamlit as st
import requests
import hmac
import hashlib
import time
import urllib.parse

st.title("Central de Acúmulo (DCA) - Oficial V4")

API_KEY = st.secrets["MB_API_KEY"]
API_SECRET = st.secrets["MB_API_SECRET"]

def executar_ordem_v4(valor_brl, preco_atual):
    # O endpoint oficial para transações TAPI v4
    url = "https://www.mercadobitcoin.net/tapi/v4/"
    
    # Montagem do Payload
    payload = {
        "tapi_method": "place_order",
        "tapi_nonce": str(int(time.time() * 1000)),
        "pair": "BTC-BRL",
        "type": "buy",
        "quantity": f"{valor_brl / preco_atual:.8f}",
        "limit_price": f"{preco_atual:.2f}"
    }
    
    params_encoded = urllib.parse.urlencode(payload)
    
    # Assinatura HMAC-SHA512 exigida pela TAPI
    signature = hmac.new(API_SECRET.encode('utf-8'), 
                         ("/tapi/v4/?" + params_encoded).encode('utf-8'), 
                         hashlib.sha512).hexdigest()
    
    headers = {
        'TAPI-ID': API_KEY,
        'TAPI-MAC': signature,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    return requests.post(url, data=params_encoded, headers=headers)

if st.button("EXECUTAR COMPRA TAPI"):
    st.info("Conectando à TAPI...")
    try:
        # Preço de referência para teste
        res = executar_ordem_v4(25.0, 315000.0)
        
        st.write(f"Status Code: {res.status_code}")
        
        # Diagnóstico refinado
        if res.status_code == 200:
            st.json(res.json())
        else:
            st.error("Erro na comunicação.")
            st.text(res.text[:300]) # Mostra o erro bruto para depuração
    except Exception as e:
        st.error(f"Erro no sistema: {e}")
        
