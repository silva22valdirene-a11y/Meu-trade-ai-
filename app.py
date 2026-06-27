import streamlit as st
import requests
import hmac
import hashlib
import time
import urllib.parse

st.title("Central de Acúmulo (DCA) V4")

# Configuração dos Secrets no Streamlit Cloud (Settings -> Secrets)
# MB_API_KEY = "sua_chave"
# MB_API_SECRET = "seu_segredo"

API_KEY = st.secrets["MB_API_KEY"]
API_SECRET = st.secrets["MB_API_SECRET"]

# 1. Função de consulta pública
def get_price():
    try:
        url = "https://api.mercadobitcoin.net/api/v4/tickers?symbols=BTC-BRL"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return float(response.json()[0].get('last'))
    except Exception as e:
        st.error(f"Erro ao buscar preço: {e}")
    return None

# 2. Função de execução de compra
def executar_compra(valor_brl, preco_atual):
    # Endpoint correto para ordens na API v4
    url = "https://api.mercadobitcoin.net/api/v4/broker/order"
    
    qtd_btc = valor_brl / preco_atual
    
    # Payload formatado para a v4
    payload = {
        "pair": "BTC-BRL",
        "type": "buy",
        "quantity": f"{qtd_btc:.8f}",
        "limit_price": f"{preco_atual:.2f}"
    }
    
    payload_encoded = urllib.parse.urlencode(payload)
    
    # Assinatura HMAC-SHA512
    signature = hmac.new(API_SECRET.encode('utf-8'), 
                         payload_encoded.encode('utf-8'), 
                         hashlib.sha512).hexdigest()
    
    headers = {
        'TAPI-ID': API_KEY,
        'TAPI-MAC': signature,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    return requests.post(url, data=payload_encoded, headers=headers)

# --- INTERFACE ---
preco = get_price()
if preco:
    st.metric("Preço Atual BTC", f"R$ {preco:,.2f}")
    
    valor_input = st.number_input("Valor para comprar (R$):", min_value=25.0, step=10.0)
    
    if st.button("EXECUTAR COMPRA REAL"):
        with st.spinner("Enviando ordem para a corretora..."):
            try:
                res = executar_compra(valor_input, preco)
                if res.status_code == 200:
                    st.success("Ordem executada com sucesso!")
                    st.json(res.json())
                else:
                    st.error(f"Erro {res.status_code}: {res.text}")
            except Exception as e:
                st.error(f"Falha de conexão: {e}")
else:
    st.error("Não foi possível conectar com o servidor do Mercado Bitcoin.")
    
