import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Trader Pro", layout="wide")
st.title("💰 Terminal de Sinais | Trader Pro")

ticker = st.sidebar.text_input("Ativo", "BTC-USD")

if ticker:
    df = yf.download(ticker, period="1mo", interval="1d")
    if isinstance(df.columns, pd.MultiIndex): df.columns = df.columns.get_level_values(0)
    
    # Cálculo RSI
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
    rsi = 100 - (100 / (1 + (gain / loss)))
    
    # Sinal de Entrada Automático
    sinal = "AGUARDANDO"
    cor = "blue"
    
    if rsi.iloc[-1] < 30:
        sinal = "COMPRAR AGORA"
        cor = "green"
    elif rsi.iloc[-1] > 70:
        sinal = "VENDER AGORA"
        cor = "red"
        
    st.markdown(f"## Status: :{cor}[{sinal}]")
    st.metric("RSI", f"{rsi.iloc[-1]:.2f}")
    st.line_chart(rsi)
    
