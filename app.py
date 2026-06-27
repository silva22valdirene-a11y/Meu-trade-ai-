import streamlit as st
import ccxt  # <--- ESSA LINHA É OBRIGATÓRIA

# ... resto do seu código ...

# Quando for fazer a conexão, use:
exchange = ccxt.mercadobitcoin({
    'apiKey': api_key,
    'secret': api_secret,
})
