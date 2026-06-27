import streamlit as st
import requests

# Todo código que não está dentro de uma função ou 'if' deve começar rente à margem esquerda
st.title("Teste de Conexão")

url = "https://api.mercadobitcoin.net/api/v4/tickers?symbols=BTC-BRL"

try:
    response = requests.get(url, timeout=5)
    
    # O 'if' começa logo após o 'try'
    if response.status_code == 200:
        data = response.json()
        st.write("Dados recebidos com sucesso!")
        st.write(data)
    else:
        st.error(f"Erro na API: {response.status_code}")
        
except Exception as e:
    st.error(f"Erro inesperado: {e}")
    
