import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Trader Pro", layout="wide")

st.title("📊 Trader Pro | Dashboard Executivo")

# Barra lateral de controle
with st.sidebar:
    st.header("Configurações")
    ticker = st.text_input("Ativo", "BTC-USD").upper()
    capital = st.number_input("Capital (R$)", value=1000.0)
    risco = st.slider("Margem de Risco (%)", 1, 10, 5)

try:
    dados = yf.Ticker(ticker)
    hist = dados.history(period="1mo") # 1 mês de histórico
    preco = hist['Close'].iloc[-1]
    media = hist['Close'].rolling(window=5).mean().iloc[-1]
    
    # Métricas de topo
    col1, col2 = st.columns(2)
    col1.metric("Preço Atual", f"R$ {preco:,.2f}")
    col2.metric("Média 5d", f"R$ {media:,.2f}")
    
    # Análise de Performance
    st.markdown("### 📈 Análise de Tendência")
    st.line_chart(hist['Close']) # Gráfico de linha profissional
    
    # Caixa de Decisão com cálculo de lucro
    if preco < media:
        st.success("✅ SINAL: COMPRA DETECTADA")
        lucro_potencial = (media - preco)
        st.write(f"Potencial de retorno técnico: R$ {lucro_potencial:,.2f} por unidade.")
    else:
        st.warning("⚠️ SINAL: AGUARDAR (Tendência de baixa)")
        
    # Gerenciamento de Risco
    st.markdown("### 🛡️ Gestão de Risco")
    stop_loss = preco * (1 - (risco/100))
    perda_maxima = capital * (risco/100)
    
    st.info(f"**STOP LOSS:** R$ {stop_loss:,.2f}")
    st.error(f"**Exposição de Risco:** Se atingir o stop, você perderá R$ {perda_maxima:,.2f} do seu capital.")

except:
    st.error("Erro ao carregar dados. Verifique o ativo.")
    
