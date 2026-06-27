import streamlit as st
import ccxt

# Em vez de chamar ccxt.mercado_bitcoin diretamente, usamos o método getattr
# Isso evita o erro de 'NameError' ou 'AttributeError'
def conectar_corretora(api_key, api_secret):
    # O nome da classe no CCXT é 'mercadobitcoin' (tudo junto, minúsculo)
    exchange_class = getattr(ccxt, 'mercadobitcoin')
    exchange = exchange_class({
        'apiKey': api_key,
        'secret': api_secret,
        'enableRateLimit': True,
    })
    return exchange
    
