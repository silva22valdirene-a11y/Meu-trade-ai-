import streamlit as st
import requests
import hmac
import hashlib
import time
import urllib.parse

st.title("Central de Acúmulo (DCA)")

# Chaves vindas do Streamlit Secrets
API_KEY = st.secrets["MB_API_KEY"]
API_SECRET = st.secrets["MB_API_SECRET"]

def assinar_requisicao(path, params):
    # Lógica de assinatura exigida pelo Mercado Bitcoin (TAPI)
    tonce = str(int(time.time() * 1000))
    params['tonce'] = tonce
    params_encoded = urllib.parse.urlencode(params)
    
    # Criando a assinatura HMAC-SHA512
    signature = hmac.new(API_SECRET.encode('utf-8'), 
                         (path + '?' + params_encoded).encode('utf-8'), 
                         hashlib.sha512).hexdigest()
    
    headers = {
        'TAPI-ID': API_KEY,
        'TAPI-MAC': signature,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    return headers, params_encoded

if st.button("EXECUTAR COMPRA REAL"):
    st.warning("Tentando executar a ordem...")
    
    try:
        # Exemplo: Comprar R$ 10,00 (valor mínimo)
        path = "/tapi/v4/"
        params = {
            "tapi_method": "place_order",
            "pair": "BTC-BRL",
            "type": "buy",
            "quantity": "0.0001", # Exemplo: ajuste conforme o preço atual
            "limit_price": "315000" # Exemplo: preço limite
        }
        
        headers, data = assinar_requisicao(path, params)
        response = requests.post("https://www.mercadobitcoin.net" + path, data=data, headers=headers)
        
        if response.status_code == 200:
            st.success("Compra enviada com sucesso!")
            st.json(response.json())
        else:
            st.error(f"Erro ao enviar ordem: {response.text}")
            
    except Exception as e:
        st.error(f"Falha na conexão: {e}")
        
