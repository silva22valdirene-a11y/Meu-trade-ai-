import ccxt
import streamlit as st

# Tente listar as corretoras que ele conhece
st.write("Lista completa de exchanges:", ccxt.exchanges)

# Tente usar o acesso genérico
try:
    exchange = ccxt.load_exchange('mercadobitcoin')
    st.write("Conexão bem-sucedida!")
except Exception as e:
    st.write("Erro ao conectar:", e)
    
