import streamlit as st
import yfinance as yf
import pandas as pd

# Configuração visual profissional
st.set_page_config(page_title="Trader Pro", layout="wide")

st.title("📈 Trader Pro | Terminal de Análise")

# Barra lateral para configurações
with st.sidebar:
    st.header("Configurações")
    ticker = st.text_input("Ativo (ex: BTC-USD)", "BTC-USD")
    periodo = st.selectbox("Período", ["1mo", "3mo", "6mo", "1y"])

if ticker:
    data = yf.download(ticker, period=periodo, interval="1d")
    
    if not data.empty:
        # Cálculo de indicadores básicos
        ultimo_preco = data['Close'].iloc[-1]
        preco_anterior = data['Close'].iloc[-2]
        delta = ((ultimo_preco - preco_anterior) / preco_anterior) * 100
        
        # Dashboard Superior (Métricas)
        col1, col2, col3 = st.columns(3)
        col1.metric("Preço Atual", f"US$ {float(ultimo_preco):,.2f}", f"{float(delta):.2f}%")
        col2.metric("Máxima (Período)", f"US$ {float(data['High'].max()):,.2f}")
        col3.metric("Mínima (Período)", f"US$ {float(data['Low'].min()):,.2f}")
        
        # Gráfico principal com Plotly (mais profissional)
        st.subheader(f"Evolução de Preço: {ticker}")
        st.line_chart(data['Close'])
        
        # Tabela de dados (Expandable)
        with st.expander("Ver dados brutos"):
            st.dataframe(data.tail(10))
            
        st.success("Dashboard atualizado em tempo real.")
    else:
        st.error("Ativo não encontrado.")
        
