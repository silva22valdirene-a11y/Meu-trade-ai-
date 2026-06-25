import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Trader Pro", layout="wide")
st.title("📈 Trader Pro | Terminal Avançado")

# Barra Lateral: Configurações Profissionais
with st.sidebar:
    st.header("Ferramentas")
    ativos = st.text_input("Ativos (separados por vírgula)", "BTC-USD, ETH-USD")
    periodo = st.selectbox("Período", ["1mo", "3mo", "6mo", "1y"])
    intervalo = st.selectbox("Intervalo", ["1d", "1h", "1wk"])
    st.divider()
    mostrar_rsi = st.checkbox("Mostrar RSI", True)

# Processamento dos ativos
lista_ativos = [a.strip() for a in ativos.split(",")]

for ticker in lista_ativos:
    try:
        data = yf.download(ticker, period=periodo, interval=intervalo)
        if not data.empty:
            # Cálculos Profissionais
            data['SMA_20'] = data['Close'].rolling(window=20).mean()
            
            # Cálculo RSI
            delta = data['Close'].diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
            rs = gain / loss
            data['RSI'] = 100 - (100 / (1 + rs))
            
            # Exibição
            st.subheader(f"Análise: {ticker}")
            col1, col2, col3 = st.columns(3)
            col1.metric("Preço Atual", f"US$ {data['Close'].iloc[-1].item():,.2f}")
            col2.metric("Média Móvel (20)", f"US$ {data['SMA_20'].iloc[-1]:,.2f}")
            col3.metric("RSI Atual", f"{data['RSI'].iloc[-1]:.2f}")
            
            st.line_chart(data[['Close', 'SMA_20']])
            if mostrar_rsi:
                st.line_chart(data['RSI'])
            
            with st.expander(f"Dados técnicos de {ticker}"):
                st.dataframe(data.tail())
        else:
            st.error(f"Ativo {ticker} não encontrado.")
    except Exception as e:
        st.error(f"Erro no ativo {ticker}: {e}")
        
