import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Trader Pro", layout="wide")
st.title("📊 Trader Pro | Dashboard 3.0")

# O yfinance não precisa de API da Binance, então não é bloqueado
ticker = st.text_input("Digite o ativo (ex: BTC-USD ou PETR4.SA)", "BTC-USD")

if ticker:
    # Busca dados
    data = yf.download(ticker, period="1mo", interval="1d")
    
    # Exibe métricas
    ultimo_preco = data['Close'].iloc[-1]
    st.metric(f"Preço Atual de {ticker}", f"{float(ultimo_preco):,.2f}")
    
    # Exibe gráfico simples
    st.line_chart(data['Close'])
    
    st.success("Dados carregados com sucesso sem restrições!")
else:
    st.info("Digite um ativo para começar a análise.")
    
