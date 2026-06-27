import streamlit as st
import requests
import hmac
import hashlib
import time
import urllib.parse
import json

st.title("Central de Acúmulo (DCA) V4")

# Carrega os Secrets do Streamlit Cloud
API_KEY = st.secrets["MB_API_KEY"]
API_SECRET = st.secrets["MB_API_SECRET"]

# 1. Função de consulta pública
def get_price():
    url = "https://api.mercadobitcoin.net/api/v4/tickers?symbols=BTC-BRL"
    response = requests.get(url)
    if response.status_code == 200:
        return float(response.json()[0].get('last'))
    return None

# 2. Função de execução de compra autenticada
def executar_compra(valor_brl, preco_atual):
    # Endpoint oficial v4 para ordens
    url = "https://api.mercadobitcoin.net/api/v4/orders"
    
    # Cálculo da quantidade
    qtd_btc = valor_brl / preco_atual
    
    # O payload deve ser um JSON na v4
    payload = {
        "pair": "BTC-BRL",
        "type": "buy",
        "quantity": f"{qtd_btc:.8f}",
        "limit_price": f"{preco_atual:.2f}"
    }
    
    # Na API v4, a assinatura é feita sobre o JSON serializado
    payload_json = json.dumps(payload, separators=(',', ':'))
    
    signature = hmac.new(API_SECRET.encode('utf-8'), 
                         payload_json.encode('utf-8'), 
                         hashlib.sha512).hexdigest()
    
    headers = {
        'TAPI-ID': API_KEY,
        'TAPI-MAC': signature,
        'Content-Type': 'application/json'
    }
    
    return requests.post(url, data=payload_json, headers=headers)

# Interface
preco = get_price()
if preco:
    st.metric("Preço Atual BTC", f"R$ {preco:,.2f}")
    valor_input = st.number_input("Valor para comprar (R$):", min_value=25.0, step=10.0)
    
    if st.button("EXECUTAR COMPRA REAL"):
        with st.spinner("Processando..."):
            res = executar_compra(valor_input, preco)
            if res.status_code == 201: # 201 é o código padrão para criação de recursos
                st.success("Ordem enviada com sucesso!")
                st.json(res.json())
            else:
                st.error(f"Erro {res.status_code}: {res.text}")
else:
    st.error("Erro ao buscar preço.")
    
