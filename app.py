import streamlit as st
import ccxt

st.title("💰 Central de Acúmulo (DCA)")

# Campos de entrada
key = st.text_input("API Key", type="password")
secret = st.text_input("API Secret", type="password")

if st.button("Verificar Saldo"):
    if not key or not secret:
        st.warning("Por favor, insira as chaves.")
    else:
        try:
            # Conexão direta e simples
            mb = ccxt.mercadobitcoin()
            mb.apiKey = key
            mb.secret = secret
            
            # Busca saldo
            balance = mb.fetch_balance()
            total_brl = balance['total'].get('BRL', 0)
            
            st.success(f"Conexão OK! Seu saldo: R$ {total_brl:,.2f}")
        except Exception as e:
            st.error(f"Erro na conexão: {e}")
            
