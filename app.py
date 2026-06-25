import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Trader Pro", layout="wide")
st.title("💰 Trader Pro | Algoritmo de Sinais")

with st.sidebar:
    ativos = st.text_input("Ativos", "BTC-USD, ETH-USD")
    periodo = st.selectbox("Período", ["1mo", "3mo"])
    intervalo = st.selectbox("Intervalo", ["1d", "1h"])

lista_ativos = [a.strip() for a in ativos.split(",")]

for ticker in lista_ativos:
    try:
        df = yf.download(ticker, period=periodo, interval=intervalo)
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
            
        if not df.empty and 'Close' in df.columns:
            # Cálculos de RSI
            delta = df['Close'].diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
            rs = gain / loss
            df['RSI'] = 100 - (100 / (1 + rs))
            
            rsi_atual = float(df['RSI'].iloc[-1])
            preco = float(df['Close'].iloc[-1])
            
            st.subheader(f"Monitor: {ticker}")
            
            # Lógica de "Fazer Dinheiro" (Sinais)
            if rsi_atual < 30:
                st.success(f"🚨 SINAL DE COMPRA: {ticker} em US$ {preco:,.2f} (RSI: {rsi_atual:.2f})")
            elif rsi_atual > 70:
                st.error(f"⚠️ SINAL DE VENDA: {ticker} em US$ {preco:,.2f} (RSI: {rsi_atual:.2f})")
            else:
                st.info(f"Aguardando sinal... {ticker} (RSI: {rsi_atual:.2f})")
                
            st.line_chart(df['RSI'])
    except Exception as e:
        st.error(f"Erro em {ticker}: {e}")
        
