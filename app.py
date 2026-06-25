import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Trader Pro", layout="wide")

st.title("📊 Trader Pro | Dashboard Executivo")

with st.sidebar:
    st.header("Configurações")
    ticker = st.text_input("Ativo", "BTC-USD").upper()
    capital = st.number_input("Capital (R$)", value=1000.0)
    risco = st.slider("Margem de Risco (%)", 1, 10, 5)

try:
    dados = yf.Ticker(ticker)
    hist = dados.history(period="1mo")
    preco = hist['Close'].iloc[-1]
    media = hist['Close'].rolling(window=5).mean().iloc[-1]
    
    col1, col2 = st.columns(2)
    col1.metric("Preço Atual", f"R$ {preco:,.2f}")
    col2.metric("Média 5d", f"R$ {media:,.2f}")
    
    st.markdown("### 📈 Análise de Tendência")
    st.line_chart(hist['Close'])
    
    # Tabela de Estatísticas (O toque de mestre)
    st.write("### 📊 Resumo Estatístico")
    resumo = pd.DataFrame({
        "Máxima (1 mês)": [hist['High'].max()],
        "Mínima (1 mês)": [hist['Low'].min()],
        "Volatilidade": [f"{((hist['Close'].std()/preco)*100):.2f}%"]
    })
    st.table(resumo)
    
    if preco < media:
        st.success("✅ SINAL: COMPRA")
    else:
        st.warning("⚠️ SINAL: AGUARDAR")
        
    st.markdown("### 🛡️ Gestão de Risco")
    stop_loss = preco * (1 - (risco/100))
    st.info(f"**STOP LOSS:** R$ {stop_loss:,.2f}")

except:
    st.error("Erro ao carregar.")
    
