import streamlit as st
import requests
import hmac
import hashlib
import time
import urllib.parse

st.title("Central de Acúmulo (DCA) - TAPI V4 - Ajuste Final")

API_KEY = st.secrets["MB_API_KEY"]
API_SECRET = st.secrets["MB_API_SECRET"]

def executar_ordem_tapi_v4(valor_brl, preco_atual):
    # O endpoint da TAPI v4 é sempre este caminho raiz
    url = "https://www.mercadobitcoin.net/tapi/v4/"
    
    # Parâmetros obrigatórios para a função 'place_order'
    params = {
        "tapi_method": "place_order",
        "tapi_nonce": str(int(time.time() * 1000)),
        "pair": "BTC-BRL",
        "type": "buy",
        "quantity": f"{valor_brl / preco_atual:.8f}",
        "limit_price": f"{preco_atual:.2f}"
    }
    
    params_encoded = urllib.parse.urlencode(params)
    
    # A assinatura é feita sobre a string codificada
    signature = hmac.new(API_SECRET.encode('utf-8'), 
                         params_encoded.encode('utf-8'), 
                         hashlib.sha512).hexdigest()
    
    headers = {
        'TAPI-ID': API_KEY,
        'TAPI-MAC': signature,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    return requests.post(url, data=params_encoded, headers=headers)

if st.button("EXECUTAR COMPRA - TAPI V4"):
    st.info("Conectando ao Broker...")
    try:
        # Preço de teste: 315000.0
        res = executar_ordem_tapi_v4(25.0, 315000.0)
        
        st.write(f"Status Code: {res.status_code}")
        
        if res.status_code == 200:
            st.json(res.json())
        else:
            st.error(f"Erro na execução (Status {res.status_code})")
            st.text(res.text[:500])
    except Exception as e:
        st.error(f"Erro crítico: {e}")
        
