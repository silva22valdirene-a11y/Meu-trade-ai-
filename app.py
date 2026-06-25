import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Trader Pro 3.0", layout="wide")

st.markdown("""
    <style>
    .stMetric {background-color: #1e1e1e; padding: 15px; border-radius: 10px;}
    </style>
""", unsafe_allow_html=True)

st.title("📊 Trader Pro | Dashboard Executivo")

# Barra lateral para configurações
with st.sidebar:
    st.header("Configurações")
    ticker = st.text_input("Ativo", "BTC-USD").upper()
    capital = st.number_input("Capital (R$)", value=1000.0)
    risco = st.slider("Margem de Risco (%)", 1, 10, 5)

# Área principal
if st.button("🚀 ATUALIZAR DADOS DE MERCADO"):
    try:
        dados = yf.Ticker(ticker)
        preco = dados.history(period="1d")['Close'].iloc[-1]
        media = dados.history(period="5d")['Close'].mean()
        
        # Colunas de Destaque
        col1, col2, col3 = st.columns(3)
        col1.metric("Preço Atual", f"R$ {preco:,.2f}")
        col2.metric("Média 5d", f"R$ {media:,.2f}")
        col3.metric("Capital", f"R$ {capital:,.2f}")
        
        st.markdown("---")
        
        # Área de Análise Visual
        if preco < media:
            st.success("✅ OPORTUNIDADE DE COMPRA: O preço está abaixo da média móvel.")
        else:
            st.error("⚠️ AGUARDAR: O ativo está sobrecomprado acima da média.")
            
        # Gerenciamento de Risco Visual
        st.subheader("Gerenciamento de Risco")
        stop_loss = preco * (1 - (risco/100))
        
        st.write(f"Nível de proteção em {risco}%:")
        st.progress((risco)/10)
        st.info(f"**STOP LOSS SUGERIDO:** R$ {stop_loss:,.2f}")
        
    except Exception:
        st.error("Erro ao buscar dados. Verifique o símbolo do ativo.")
        
