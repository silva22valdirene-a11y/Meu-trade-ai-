
import streamlit as st
import ccxt

# Configuração da página
st.set_page_config(page_title="Meu Bot de Trade", layout="wide")

st.title("🤖 Painel do Bot de Trade")

# Exemplo de como usar a biblioteca ccxt
st.subheader("Verificação de Conexão")
try:
    exchange = ccxt.binance()
    st.success("Biblioteca CCXT carregada com sucesso!")
    st.write("Pronto para buscar dados de mercado.")
except Exception as e:
    st.error(f"Erro ao carregar ccxt: {e}")

st.info("Seu bot está configurado corretamente. Adicione aqui sua estratégia de trading.")
