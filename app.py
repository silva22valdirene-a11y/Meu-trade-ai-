import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Trader Pro", layout="wide")
st.title("📊 Trader Pro | Dashboard 3.0")

tab1, tab2 = st.tabs(["📈 Análise de Mercado", "⚡ Execução Real"])

# --- ABA 1 ---
with tab1:
    st.header("Análise Técnica")
    ticker = st.text_input("Ativo", "BTC-USD").upper()
    
    try:
        dados = yf.Ticker(ticker)
        hist = dados.history(period="1mo")
        preco = hist['Close'].iloc[-1]
        
        # Colunas inseridas DENTRO da aba 1
        col1, col2, col3 = st.columns(3)
        col1.metric("Preço", f"${preco:,.2f}")
        col2.metric("Alta", f"${hist['High'].max():,.2f}")
        col3.metric("Baixa", f"${hist['Low'].min():,.2f}")
        
        fig = go.Figure(data=[go.Candlestick(x=hist.index,
                        open=hist['Open'], high=hist['High'],
                        low=hist['Low'], close=hist['Close'])])
        fig.update_layout(template="plotly_dark", title="Gráfico de Preço")
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"Erro no gráfico: {e}")

# --- ABA 2 ---
with tab2:
    st.header("Execução Real")
    # Conteúdo da execução aqui...
  
