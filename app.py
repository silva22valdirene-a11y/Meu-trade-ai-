import streamlit as st
import ccxt

# Define a interface
st.title("💰 Central de Acúmulo (DCA)")

# Função para conectar
def conectar():
    return ccxt.mercadobitcoin({
        'enableRateLimit': True,
    })

# Inputs para as chaves
api_key = st.text_input("API Key", type="password")
api_secret = st.text_input("API Secret", type="password")

# Botão de ação
if st.button("Verificar Saldo"):
    try:
        exchange = conectar()
        exchange.apiKey = api_key
        exchange.secret = api_secret
        
        balance = exchange.fetch_balance()
        saldo = balance['total'].get('BRL', 0)
        st.success(f"Saldo atual: R$ {saldo:,.2f}")
    except Exception as e:
        st.error(f"Erro: {e}")
      
