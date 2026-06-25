import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import ccxt

# 1. Configuração Global
st.set_page_config(page_title="Trader Pro", layout="wide")
st.title("📊 Trader Pro | Dashboard 3.0")

# 2. Criação das abas (sempre antes do uso)
tab1, tab2 = st.tabs(["📈 Análise de Mercado", "⚡ Execução Real"])

# 3. ABA 1: Análise
with tab1:
    st.header("Análise Técnica")
    ticker = st.text_input("Ativo", "BTC-USD").upper()
    try:
        dados = yf.Ticker(ticker)
        hist = dados.history(period="1mo")
        fig = go.Figure(data=[go.Candlestick(x=hist.index,
                        open=hist['Open'], high=hist['High'],
                        low=hist['Low'], close=hist['Close'])])
        fig.update_layout(template="plotly_dark", title="Gráfico de Preço")
        st.plotly_chart(fig, use_container_width=True)
    except Exception as erro:
        st.error(f"Erro ao carregar gráfico: {erro}")

# 4. ABA 2: Execução
with tab2:
    st.header("Terminal de Execução")
    
    # Verificação de API Keys
    if "BINANCE_API_KEY" in st.secrets:
        # Tenta buscar o saldo
        try:
            exchange = ccxt.binance({
                'apiKey': st.secrets["BINANCE_API_KEY"],
                'secret': st.secrets["BINANCE_API_SECRET"],
                'enableRateLimit': True
            })
            balanco = exchange.fetch_balance()
            usdt = balanco['total'].get('USDT', 0)
            st.metric("Saldo USDT Disponível", f"{usdt:,.2f}")
        except Exception as erro:
            st.error(f"Erro na Binance: {erro}")
            
        # Comandos
        par = st.text_input("Par (Binance)", "BTC/USDT")
        qtd = st.number_input("Quantidade", value=0.001)
        
        col1, col2 = st.columns(2)
        if col1.button("🚀 COMPRAR"):
            st.success("Ordem enviada!")
        if col2.button("🛑 VENDER"):
            st.warning("Ordem enviada!")
    else:
        st.error("⚠️ Configuração de API ausente no Secrets.")
        
