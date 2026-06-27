import streamlit as st
import requests
import hmac
import hashlib
import time
import urllib.parse

st.title("Central de Acúmulo (DCA) - TAPI v4")

# Certifique-se de que estas chaves estão configuradas nos Secrets do seu repositório no Streamlit Cloud
API_KEY = st.secrets["MB_API_KEY"]
API_SECRET = st.secrets["MB_API_SECRET"]

def executar_ordem_tapi(valor_brl, preco_atual):
    url = "https://www.mercadobitcoin.net/tapi/v4/"
    
    # Parâmetros necessários para a função 'place_order'
    params = {
        "tapi_method": "place_order",
        "tapi_nonce": str(int(time.time() * 1000)),
        "pair": "BTC-BRL",
        "type": "buy",
        "quantity": f"{valor_brl / preco_atual:.8f}",
        "limit_price": f"{preco_atual:.2f}"
    }
    
    # A TAPI exige que os parâmetros sejam codificados como formulário
    params_encoded = urllib.parse.urlencode(params)
    
    # A assinatura deve ser gerada sobre a string dos parâmetros
    signature = hmac.new(API_SECRET.encode('utf-8'), 
                         params_encoded.encode('utf-8'), 
                         hashlib.sha512).hexdigest()
    
    headers = {
        'TAPI-ID': API_KEY,
        'TAPI-MAC': signature,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    # Executa a requisição POST
    return requests.post(url, data=params_encoded, headers=headers)

if st.button("EXECUTAR COMPRA - TAPI v4"):
    st.info("Conectando ao Broker...")
    try:
        # Preço de referência fixo para teste imediato
        res = executar_ordem_tapi(25.0, 315000.0)
        
        st.write(f"Status Code: {res.status_code}")
        
        if res.status_code == 200:
            st.json(res.json())
        else:
            st.error(f"Erro na execução (Status {res.status_code})")
            # Exibe os primeiros caracteres para diagnóstico
            st.text(res.text[:200]) 
    except Exception as e:
        st.error(f"Erro no sistema: {e}")
        
