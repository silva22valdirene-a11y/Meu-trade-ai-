import streamlit as st
import requests
import hmac
import hashlib
import time
import json

st.title("Central de Acúmulo (DCA) - Oficial V4")

# Configuração de chaves (Certifique-se de que estão no Secrets do Streamlit Cloud)
API_KEY = st.secrets["MB_API_KEY"]
API_SECRET = st.secrets["MB_API_SECRET"]

# 1. Função de consulta pública (preço)
def get_price():
    url = "https://api.mercadobitcoin.net/api/v4/tickers?symbols=BTC-BRL"
    response = requests.get(url)
    if response.status_code == 200:
        return float(response.json()[0].get('last'))
    return None

# 2. Função de compra (API v4)
def executar_compra_v4(valor_brl, preco_atual):
    url = "https://api.mercadobitcoin.net/api/v4/orders"
    qtd_btc = valor_brl / preco_atual
    
    payload = {
        "pair": "BTC-BRL",
        "type": "buy",
        "quantity": f"{qtd_btc:.8f}",
        "limit_price": f"{preco_atual:.2f}"
    }
    
    payload_json = json.dumps(payload, separators=(',', ':'))
    
    # Assinatura HMAC-SHA512
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
    valor_input = st.number_input("Valor (R$):", min_value=25.0, step=10.0)
    
    if st.button("EXECUTAR COMPRA REAL"):
        # Mensagem corrigida para evitar SyntaxError
        st.warning("Enviando ordem via API...") 
        try:
            res = executar_compra_v4(valor_input, preco)
            if res.status_code == 201:
                st.success("Ordem enviada com sucesso!")
                st.json(res.json())
            else:
                st.error(f"Erro {res.status_code}: {res.text}")
        except Exception as e:
            st.error(f"Erro no sistema: {e}")
            
