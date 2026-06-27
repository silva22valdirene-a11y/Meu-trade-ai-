import streamlit as st
import requests
import hmac
import hashlib
import time
import json

st.title("Central de Acúmulo (DCA) - TAPI V4 - Ajuste Final")

# Chaves configuradas no Secrets do Streamlit Cloud
API_KEY = st.secrets["MB_API_KEY"]
API_SECRET = st.secrets["MB_API_SECRET"]

def executar_compra_v4(valor_brl, preco_atual):
    # Endpoint correto de negociação para a v4
    url = "https://api.mercadobitcoin.net/api/v4/broker/order"
    
    # Cálculo da quantidade
    qtd_btc = valor_brl / preco_atual
    
    # Payload JSON
    payload = {
        "pair": "BTC-BRL",
        "type": "buy",
        "quantity": f"{qtd_btc:.8f}",
        "limit_price": f"{preco_atual:.2f}"
    }
    
    # Serialização do JSON para a assinatura
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
    
    # Requisição POST
    return requests.post(url, data=payload_json, headers=headers)

if st.button("EXECUTAR COMPRA - V4"):
    st.info("Conectando ao broker...")
    try:
        # Preço de referência para teste
        res = executar_compra_v4(25.0, 315000.0)
        
        st.write(f"Status Code: {res.status_code}")
        
        if res.status_code == 201:
            st.success("Ordem executada!")
            st.json(res.json())
        else:
            st.error(f"Erro na execução (Status {res.status_code})")
            st.text(res.text[:300])
    except Exception as e:
        st.error(f"Erro crítico: {e}")
        
