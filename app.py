import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Trader Pro", layout="wide")
st.title("📈 Trader Pro | Terminal de Análise")

with st.sidebar:
    ticker = st.text_input("Ativo (ex: BTC-USD)", "BTC-USD")
    periodo = st.selectbox("Período", ["1mo", "3mo", "6mo", "1y"])

if ticker:
    data = yf.download(ticker, period=periodo, interval="1d")
    
    if not data.empty:
        # Extrair valores como números puros (float)
        ultimo_preco = float(data['Close'].iloc[-1])
        preco_anterior = float(data['Close'].iloc[-2])
        delta_pct = ((ultimo_preco - preco_anterior) / preco_anterior) * 100
        
        # Dashboard Superior
        col1, col2, col3 = st.columns(3)
        # Passando apenas valores float para evitar o TypeError
        col1.metric("Preço Atual", f"US$ {ultimo_preco:,.2f}", f"{delta_pct:.2f}%")
        col2.metric("Máxima", f"US$ {float(data['High'].max()):,.2f}")
        col3.metric("Mínima", f"US$ {float(data['Low'].min()):,.2f}")
        
        st.line_chart(data['Close'])
        
        with st.expander("Dados Brutos"):
            st.dataframe(data.tail(10))
    else:
        st.error("Ativo não encontrado.")
