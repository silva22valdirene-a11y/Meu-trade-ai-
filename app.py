import streamlit as st
import ccxt

# Agora o código pode reconhecer as ferramentas que você importou acima
st.write("Exchanges disponíveis no CCXT:", ccxt.exchanges)
