import streamlit as st
import ccxt

# Configuração da página
st.set_page_config(page_title="Bot de Trade", layout="wide")

# Menu de Navegação
st.sidebar.title("Navegação")
aba = st.sidebar.radio("Ir para:", ["Dashboard", "Configurações", "Logs de Trade"])

# --- ABA 1: DASHBOARD ---
if aba == "Dashboard":
    st.title("📊 Visão Geral do Mercado")
    st.write("Monitorando o mercado em tempo real...")
    # Aqui você poderá exibir preços (ex: st.metric("BTC/USDT", "65.000"))
    st.info("O robô está aguardando sinais de entrada.")

# --- ABA 2: CONFIGURAÇÕES ---
elif aba == "Configurações":
    st.title("⚙️ Configurações do Bot")
    api_key = st.text_input("API Key", type="password")
    api_secret = st.text_input("API Secret", type="password")
    
    if st.button("Salvar Conexão"):
        if api_key and api_secret:
            st.success("Credenciais salvas temporariamente na sessão.")
        else:
            st.error("Por favor, preencha as chaves.")

# --- ABA 3: LOGS DE TRADE ---
elif aba == "Logs de Trade":
    st.title("📜 Histórico de Operações")
    st.write("Registros de ordens executadas:")
    # Aqui vamos mostrar o histórico quando você tiver trades
    st.warning("Nenhum trade realizado nas últimas 24h.")
    
