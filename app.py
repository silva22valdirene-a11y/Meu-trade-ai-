import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Trader Pro", layout="wide")
st.title("📈 Trader Pro | Terminal Avançado")

with st.sidebar:
    st.header("Ferramentas")
    ativos = st.text_input("Ativos (separados por vírgula)", "BTC-USD, ETH-USD")
    periodo = st.selectbox("Período", ["1mo", "3mo", "6mo", "1y"])
    intervalo = st.selectbox("Intervalo", ["1d", "1h", "1wk"])
    mostrar_rsi = st.checkbox("Mostrar RSI", True)

lista_ativos = [a.strip() for a in ativos.split(",")]

for ticker in lista_ativos:
    try:
        # Baixa os dados
        df = yf.download(ticker, period=periodo, interval=intervalo)
        
        # Correção para o erro de index: se os dados tiverem colunas MultiIndex, achatamos
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
            
        if not df.empty and 'Close' in df.columns:
            # Cálculos de forma segura
            df['SMA_20'] = df['Close'].rolling(window=20).mean()
            
            delta = df['Close'].diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
            rs = gain / loss
            df['RSI'] = 100 - (100 / (1 + rs))
            
            st.subheader(f"Análise: {ticker}")
            col1, col2, col3 = st.columns(3)
            
            # Extração segura dos valores
            preco_atual = float(df['Close'].iloc[-1])
            sma = float(df['SMA_20'].iloc[-1])
            rsi = float(df['RSI'].iloc[-1])
            
            col1.metric("Preço Atual", f"US$ {preco_atual:,.2f}")
            col2.metric("Média Móvel (20)", f"US$ {sma:,.2f}")
            col3.metric("RSI Atual", f"{rsi:.2f}")
            
            st.line_chart(df[['Close', 'SMA_20']])
            if mostrar_rsi:
                st.line_chart(df['RSI'])
                
        else:
            st.warning(f"Dados não processáveis para {ticker}.")
    except Exception as e:
        st.error(f"Erro no ativo {ticker}: {e}")
        
