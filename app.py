import streamlit as st
import requests

st.title("Teste de Conexão")

try:
    url = "https://api.mercadobitcoin.net/api/v4/tickers?symbols=BTC-BRL"
    response = requests.get(url, timeout=5)
    
    if response.status_code == 200:
        data = response.json()
        st.write("Dados recebidos com sucesso!")
        st.write(data)
    else:
        st.error(f"Erro na API: {response.status_code}")
except Exception as e:
    st.error(f"Erro inesperado: {e}")
    
