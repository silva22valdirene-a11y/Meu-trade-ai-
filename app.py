import streamlit as st
import requests
import hmac
import hashlib
import time
import urllib.parse

st.title("Central de Acúmulo (DCA) - TAPI V4 - Ajuste")

API_KEY = st.secrets["MB_API_KEY"]
API_SECRET = st.secrets["MB_API_SECRET"]

def executar_compra_tapi(valor_brl, preco_atual):
    # Endpoint de negociação TAPI v4
    url = "https://www.mercadobitcoin.net/tapi/v4/"
    
    params = {
        "tapi_method": "place_order",
        "tapi_nonce": str(int(time.time() * 1000)),
        "pair": "BTC-BRL",
        "type": "buy",
        "quantity": f"{valor_brl / preco_atual:.8f}",
        "limit_price": f"{preco_atual:.2f}"
    }
    
    # Ordenar e codificar parâmetros
    params_encoded = urllib.parse.urlencode(params)
    
    # Assinatura HMAC-SHA512
    # Nota: A assinatura deve ser feita sobre o corpo da requisição POST
    signature = hmac.new(API_SECRET.encode('utf-8'), 
                         params_encoded.encode('utf-8'), 
                         hashlib.sha512).hexdigest()
    
    headers = {
        'TAPI-ID': API_KEY,
        'TAPI-MAC': signature,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    # Faz o POST para o endpoint
    return requests.post(url, data=params_encoded, headers=headers)

if st.button("EXECUTAR COMPRA - TAPI V4"):
    st.info("Processando pedido na TAPI...")
    try:
        # Preço fictício para teste: 315000.00
        res = executar_compra_tapi(25.0, 315000.0)
        
        st.write(f"Status Code: {res.status_code}")
        
        if res.status_code == 200:
            st.json(res.json())
        else:
            # Depuração de erro
            st.error("Falha na chamada da API.")
            st.write(f"Resposta bruta: {res.text[:200]}")
    except Exception as e:
        st.error(f"Erro no sistema: {e}")
        
