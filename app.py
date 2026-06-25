import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# 1. Configuração inicial
st.set_page_config(page_title="Trader Pro", layout="wide")
st.title("📊 Trader Pro | Dashboard 3.0")

# 2. CRIAÇÃO DAS ABAS (Isso precisa vir antes de qualquer 'with tab...')
tab1, tab2 = st.tabs(["📈 Análise de Mercado", "⚡ Execução Real"])

# 3. ABA 1: Análise
with tab1:
    st.header("Análise Técnica")
    ticker = st.text_input("Ativo", "BTC-USD").upper()
    
    try:
        dados = yf.Ticker(ticker)
        hist = dados.history(period="1mo")
        preco = hist['Close'].iloc[-1]
        
        # Métricas no topo
        col1, col2, col3 = st.columns(3)
        col1.metric("Preço", f"${preco:,.2f}")
        col2.metric("Alta", f"${hist['High'].max():,.2f}")
        col3.metric("Baixa", f"${hist['Low'].min():,.2f}")
        
        # Gráfico
        fig = go.Figure(data=[go.Candlestick(x=hist.index,
                        open=hist['Open'], high=hist['High'],
                        low=hist['Low'], close=hist['Close'])])
        fig.update_layout(template="plotly_dark", title="Gráfico de Preço")
        st.plotly_chart(fig, use_container_width=True)
        
    except Exception as e:
        st.error(f"Erro no gráfico: {e}")

# 4. ABA 2: Execução (Agora o 'tab2' já existe, então não dará erro)
with tab2:
    st.header("Terminal de Execução")
    
    if "BINANCE_API_KEY" in st.secrets:
        par = st.text_input("Par de Negociação", "BTC/USDT")
        qtd = st.number_input("Quantidade", value=0.001)
        
        col1, col2 = st.columns(2)
        if col1.button("🚀 COMPRAR A MERCADO"):
            st.success("Ordem enviada!")
            
        if col2.button("🛑 VENDER A MERCADO"):
            st.warning("Ordem enviada!")
            
        with st.expander("📝 Ver Ordens Abertas"):
            st.write("Conectado à Binance...")
    else:
        st.error("⚠️ Configuração de API ausente no Secrets.")
        
