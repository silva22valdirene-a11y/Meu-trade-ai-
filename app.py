import streamlit as st
import requests

# 1. Função para pegar o preço atual
def get_price():
    url = "https://api.mercadobitcoin.net/api/v4/tickers?symbols=BTC-BRL"
    response = requests.get(url)
    if response.status_code == 200:
        return float(response.json()[0].get('last'))
    return None

st.title("Central de Acúmulo (DCA) - Mercado Bitcoin")

# 2. Interface para definir o investimento
preco_atual = get_price()
if preco_atual:
    st.write(f"Preço atual do BTC: R$ {preco_atual:,.2f}")
    
    valor_investimento = st.number_input("Quanto deseja investir em R$?", min_value=10.0, step=10.0)
    
    if valor_investimento > 0:
        quantidade_btc = valor_investimento / preco_atual
        st.write(f"Com R$ {valor_investimento}, você acumularia: {quantidade_btc:.8f} BTC")
else:
    st.error("Não foi possível conectar à API.")
    
