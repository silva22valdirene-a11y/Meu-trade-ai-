import streamlit as st
import requests
import hmac
import hashlib
import time
import urllib.parse

st.title("Central de Acúmulo (DCA) - Oficial")

# Certifique-se de que os nomes no 'Secrets' são exatamente estes:
# MB_API_KEY e MB_API_SECRET
API_KEY = st.secrets["MB_API_KEY"]
API_SECRET = st.secrets["MB_API_SECRET"]

def executar_compra_segura(valor_brl):
    # Endpoint unificado da TAPI v4
    url = "https://www.mercadobitcoin.net/tapi/v4/"
    
    # Parâmetros obrigatórios
    tonce = str(int(time.time() * 1000))
    params = {
        "tapi_method": "place_order",
        "tapi_nonce": tonce,
        "pair": "BTC-BRL",
        "type": "buy",
        "quantity": "0.0001",  # Ajuste conforme o preço ou use a lógica anterior
        "limit_price": "315000" # Ajuste conforme necessário
    }
    
    params_encoded = urllib.parse.urlencode(params)
    
    # Assinatura HMAC-SHA512 (obrigatória para TAPI)
    # A assinatura é baseada na string de parâmetros
    signature = hmac.new(API_SECRET.encode('utf-8'), 
                         params_encoded.encode('utf-8'), 
                         hashlib.sha512).hexdigest()
    
    headers = {
        'TAPI-ID': API_KEY,
        'TAPI-MAC': signature,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    return requests.post(url, data=params_encoded, headers=headers)

if st.button("EXECUTAR COMPRA REAL"):
    st.warning("Enviando ordem...")
    try:
        response = executar_compra_segura(25.0)
        if response.status_code == 200:
            st.success("Ordem enviada!")
            st.json(response.json())
        else:
            st.error(f"Erro {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"Erro crítico: {e}")
        
