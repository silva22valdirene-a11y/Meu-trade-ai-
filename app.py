import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Trader Pro", layout="wide")
st.title("📈 Trader Pro | Terminal de Análise")

with st.sidebar:
    ticker = st.text_input("Ativo (ex: BTC-USD)", "BTC-USD")
    periodo = st.selectbox("Período", ["1mo", "3mo", "6mo", "1y"])

if ticker:
    try:
        # Baixa os dados
        data = yf.download(ticker, period=periodo, interval="1d")
        
        if not data.empty and 'Close' in data.columns:
            # Seleciona o último preço de forma segura e converte para float
            # .iloc[-1] pega a última linha, .item() extrai o valor numérico
            ultimo_preco = data['Close'].iloc[-1].item()
            preco_anterior = data['Close'].iloc[-2].item()
            
            delta_pct = ((ultimo_preco - preco_anterior) / preco_anterior) * 100
            
            # Dashboard Superior
            col1, col2, col3 = st.columns(3)
            col1.metric("Preço Atual", f"US$ {ultimo_preco:,.2f}", f"{delta_pct:.2f}%")
            col2.metric("Máxima", f"US$ {data['High'].max().item():,.2f}")
            col3.metric("Mínima", f"US$ {data['Low'].min().item():,.2f}")
            
            st.line_chart(data['Close'])
            
            with st.expander("Dados Brutos"):
                st.dataframe(data.tail(10))
        else:
            st.warning("Dados indisponíveis para este ativo. Tente outro.")
    except Exception as e:
        st.error(f"Erro ao processar dados: {e}")
        
