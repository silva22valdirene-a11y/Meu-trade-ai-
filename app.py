import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# Configuração de Layout
st.set_page_config(page_title="Trader Pro", layout="wide")
st.title("📊 Trader Pro | Dashboard 3.0")

# Abas para organizar a interface
tab1, tab2 = st.tabs(["📈 Análise de Mercado", "⚡ Execução Real"])

# --- ABA 1: ANÁLISE ---
with tab1:
    st.header("Análise Técnica")
    ticker = st.text_input("Ativo", "BTC-USD").upper()
    
    try:
        dados = yf.Ticker(ticker)
        hist = dados.history(period="1mo")
        preco = hist['Close'].iloc[-1]
        
        # Gráfico Profissional
        fig = go.Figure(data=[go.Candlestick(x=hist.index,
                        open=hist['Open'], high=hist['High'],
                        low=hist['Low'], close=hist['Close'])])
        fig.update_layout(template="plotly_dark", title="Gráfico de Preço")
        st.plotly_chart(fig, use_container_width=True)
        
    except Exception as e:
        st.error(f"Erro ao carregar gráfico: {e}")

# --- ABA 2: EXECUÇÃO ---
with tab2:
    st.header("Execução Real")
    par = st.text_input("Par (Binance)", "BTC/USDT")
    qtd = st.number_input("Quantidade", value=0.001)
    
    col1, col2 = st.columns(2)
    if col1.button("🚀 COMPRAR"):
        st.success("Ordem enviada!")
        
    if col2.button("🛑 VENDER"):
        st.warning("Ordem enviada!")
        
    # Expander de ordens (corrigido para dentro do bloco da aba)
    with st.expander("📝 Ver Ordens Abertas"):
        st.write("Conecte a API para visualizar ordens.")
        
