import streamlit as st
import ccxt

st.title("💰 Central de Acúmulo (DCA)")

# Campos de entrada
api_key = st.text_input("API Key", type="password")
api_secret = st.text_input("API Secret", type="password")

# Lógica do botão
if st.button("Verificar Saldo no Mercado Bitcoin"):
    if api_key and api_secret:
        try:
            # Conecta na exchange
            exchange = ccxt.mercadobitcoin({
                'apiKey': api_key,
                'secret': api_secret,
                'enableRateLimit': True,
            })
            
            # Tenta buscar o saldo
            balance = exchange.fetch_balance()
            saldo_brl = balance['total'].get('BRL', 0)
            
            st.success(f"Conexão realizada! Seu saldo é: R$ {saldo_brl:,.2f}")
            
        except Exception as e:
            st.error(f"Erro ao conectar: {e}")
    else:
        st.warning("Por favor, preencha a API Key e o Secret.")
        
