import ccxt
import streamlit as st

# Carrega as chaves do segredo que você configurou no painel
api_key = st.secrets["MB_API_KEY"]
api_secret = st.secrets["MB_API_SECRET"]

# Conecta ao Mercado Bitcoin
exchange = ccxt.mercadobitcoin({
    'apiKey': api_key,
    'secret': api_secret,
})

