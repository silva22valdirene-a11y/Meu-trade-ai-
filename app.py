import streamlit as st
import requests
import hmac
import hashlib
import time
import json

st.title("Central de Acúmulo (DCA) - Oficial V4")

# Certifique-se de que estes dois campos estão configurados nos "Secrets" do seu app no Streamlit Cloud
API_KEY = st.secrets["MB_API_KEY"]
API_SECRET = st.secrets["MB_API_SECRET"]

def executar_compra_v4(valor_brl):
    # Endpoint correto e atualizado para a API v4 de ordens
    url = "https://api.mercadobitcoin.net/api/v4/orders"
    
    # 1. Definir o payload (dados da compra)
    # Nota: substitua '315000' por uma função que busca o preço real se desejar
    payload = {
        "pair": "BTC-BRL",
        "type": "buy",
        "quantity": "0.0001", 
        "limit_price": "315000"
    }
    
    # 2. Preparar os dados para a assinatura
    # A v4 exige que a assinatura seja feita sobre o JSON dos dados
    payload_json = json.dumps(payload, separators=(',', ':'))
    
    # 3. Gerar assinatura HMAC-SHA512
    signature = hmac.new(API_SECRET.encode('utf-8'), 
                         payload_json.encode('utf-8'), 
                         hashlib.sha512).hexdigest()
    
    # 4. Configurar cabeçalhos com a chave e a assinatura
    headers = {
        'TAPI-ID': API_KEY,
        'TAPI-MAC': signature,
        'Content-Type': 'application/json'
    }
    
    return requests.post(url, data=payload_json, headers=headers)

if st.button("EXECUTAR COMPRA REAL"):
    st.warning("Enviando ordem via API
               
