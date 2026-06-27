import streamlit as st
import ccxt

st.title("💰 Central de Acúmulo (DCA)")

# Campos de input
api_key = st.text_input("API Key", type="password")
api_secret = st.text_input("API Secret", type="password")

if st.button("Verificar Saldo no Mercado Bitcoin"):
    try:
        # Conexão direta usando o nome correto da classe no CCXT
        exchange = ccxt.mercadobitcoin({
            'apiKey': api_key,
            'secret': api_secret,
        })
        
        # Tenta buscar o saldo
        balance = exchange.fetch_balance()
        brl_disponivel = balance['total'].get('BRL', 0)
        
        st.success(f"Conexão OK! Saldo disponível: R$ {brl_disponivel:,.2f}")
        
    except Exception as e:
        st.error(f"Erro ao conectar: {e}")
        
