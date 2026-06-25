import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Trader Pro", layout="wide")
st.title("📈 Trader Pro | Terminal Ágil")

# Seletor único para não sobrecarregar o servidor
ticker = st.sidebar.text_input("Ativo (ex: BTC-USD)", "BTC-USD")
periodo = st.sidebar.selectbox("Período", ["1mo", "3mo"])

if ticker:
    try:
        # Baixa apenas 1 ativo por vez
        df = yf.download(ticker, period=periodo, interval="1d")
        
        # Correção estrutural
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
            
        if not df.empty and 'Close' in df.columns:
            # Cálculo otimizado
            df['SMA_20'] = df['Close'].rolling(20).mean()
            
            # RSI simples
            delta = df['Close'].diff()
            gain = (delta.where(delta > 0, 0)).rolling(14).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
            df['RSI'] = 100 - (100 / (1 + (gain/loss)))
            
            # Exibição rápida
            st.metric("Preço Atual", f"US$ {float(df['Close'].iloc[-1]):,.2f}")
            st.line_chart(df[['Close', 'SMA_20']])
            st.line_chart(df['RSI'])
        else:
            st.warning("Ativo inválido ou sem dados.")
    except Exception as e:
        st.error("Erro ao carregar: tente um ticker diferente.")
        
