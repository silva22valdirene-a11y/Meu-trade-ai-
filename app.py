import streamlit as st
import requests
import hmac
import hashlib
import time
import urllib.parse

st.title("Central de Acúmulo (DCA) - Ajuste Final")

API_KEY = st.secrets["MB_API_KEY"]
API_SECRET = st.secrets["MB_API_SECRET"]

def executar_ordem_final(valor_brl, preco_atual):
    # O endpoint correto de ordens na TAPI v4 é o caminho raiz
    url = "https://www.mercadobitcoin.net/tapi/v4/"
    
    # Parâmetros necessários para a TAPI v4
    params = {
        "tapi_method": "place_order",
        "tapi_nonce": str(int(time.time() * 1000)),
        "pair": "BTC-BRL",
        "type": "buy",
        "quantity": f"{valor_brl / preco_atual:.8f}",
        "limit_price": f"{preco_atual:.2f}"
    }
    
    params_encoded = urllib.parse.urlencode(params)
    
    # A assinatura deve ser feita sobre o caminho do endpoint + a query string
    # Tente esta combinação de path para a TAPI v4
    path = "/tapi/v4/"
    signature = hmac.new(API_SECRET.encode('utf-8'), 
                         (path + "?" + params_encoded).encode('utf-8'), 
                         hashlib.sha512).hexdigest()
    
    headers = {
        'TAPI-ID': API_KEY,
        'TAPI-MAC': signature,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    return requests.post(url, data=params_encoded, headers=headers)

if st.button("EXECUTAR COMPRA FINAL"):
    st.info("Tentando nova rota...")
    try:
        # Usando um valor de teste ou preço fixo para depuração
        res = executar_ordem_final(25.0, 315000.0)
        
        st.write(f"Status Code: {res.status_code}")
        if res.status_code == 200:
            st.json(res.json())
        else:
            st.error("Erro na requisição. Verifique o Status Code acima.")
            st.text(res.text[:500]) # Mostra apenas o início do erro
            
    except Exception as e:
        st.error(f"Erro crítico: {e}")
        
