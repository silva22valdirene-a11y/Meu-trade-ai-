import streamlit as st
import requests

st.title("Central de Acúmulo (DCA)")

# Função para buscar o preço
def get_price():
    url = "https://api.mercadobitcoin.net/api/v4/tickers?symbols=BTC-BRL"
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        return float(response.json()[0].get('last'))
    return None

# Interface
if st.button("Buscar Preço Atual"):
    preco = get_price()
    if preco:
        st.success(f"Preço atual do BTC: R$ {preco:,.2f}")
        
        # Campo para inserir o valor de investimento
        valor = st.number_input("Valor para investir (R$):", min_value=10.0, step=10.0)
        
        if valor > 0:
            qtd_btc = valor / preco
            st.info(f"Com R$ {valor:,.2f}, você acumularia aproximadamente: {qtd_btc:.8f} BTC")
    else:
        st.error("Erro ao conectar com a API.")
        
