import streamlit as st
import requests
import hmac
import hashlib
import time
import urllib.parse

st.title("Central de Acúmulo (DCA) V4")

# Carrega os Secrets do Streamlit Cloud
API_KEY = st.secrets["MB_API_KEY"]
API_SECRET = st.secrets["MB_API_SECRET"]

# 1. Função de consulta pública (para ver o preço)
def get_price():
    url = "https://api.mercadobitcoin.net/api/v4/tickers?symbols=BTC-BRL"
    response = requests.get(url)
    if response.status_code == 200:
        return float(response.json()[0].get('last'))
    return None

# 2. Função de execução de compra autenticada
def executar_compra(valor_brl, preco_atual):
    url = "https://api.mercadobitcoin.net/api/v4/orders"
    qtd_btc = valor_brl / preco_atual
    
    payload = {
        "pair": "BTC-BRL",
        "type": "buy",
        "quantity": f"{qtd_btc:.8f}",
        "limit_price": f"{preco_atual:.2f}"
    }
    
    payload_encoded = urllib.parse.urlencode(payload)
    
    # Assinatura HMAC-SHA512 exigida pela API v4
    signature = hmac.new(API_SECRET.encode('utf-8'), 
                         payload_encoded.encode('utf-8'), 
                         hashlib.sha512).hexdigest()
    
    headers = {
        'TAPI-ID': API_KEY,
        'TAPI-MAC': signature,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    return requests.post(url, data=payload_encoded, headers=headers)

# Interface
preco = get_price()
if preco:
    st.metric("Preço Atual BTC", f"R$ {preco:,.2f}")
    
    valor_input = st.number_input("Valor para comprar (R$):", min_value=25.0, step=10.0)
    
    if st.button("EXECUTAR COMPRA REAL"):
        with st.spinner("Processando..."):
            res = executar_compra(valor_input, preco)
            if res.status_code == 200:
                st.success("Compra realizada com sucesso!")
                st.json(res.json())
            else:
                st.error(f"Erro {res.status_code}: {res.text}")
else:
    st.error("Não foi possível buscar o preço atual.")
    
