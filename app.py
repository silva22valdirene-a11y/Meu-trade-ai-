import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import ccxt # Certifique-se de que o ccxt está no requirements.txt

st.set_page_config(page_title="Trader Pro", layout="wide")
st.title("📊 Trader Pro | Dashboard 3.0")

# Criação das abas antes de qualquer uso
tab1, tab2 = st.tabs(["📈 Análise de Mercado", "⚡ Execução Real"])

with tab1:
    st.header("Análise Técnica")
    # ... (seu código de gráfico aqui)

with tab2:
    st.header("Execução Real")
    try:
        # Configuração da API
        exchange = ccxt.binance({
            'apiKey': st.secrets["BINANCE_API_KEY"],
            'secret': st.secrets["BINANCE_API_SECRET"]
        })
        # Opcional: Adicionar sandbox para evitar restrições de localização
        # exchange.set_sandbox_mode(True) 
        
        st.success("Conectado com sucesso!")
    except Exception as e:
        st.error(f"Erro de conexão: {e}")
        
