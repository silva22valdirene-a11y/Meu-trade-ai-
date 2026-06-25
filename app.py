import streamlit as st
import yfinance as yf

# Configuração da página
st.set_page_config(page_title="Trader Pro", layout="wide")

st.title("📊 Trader Pro | Dashboard Executivo")

# Barra lateral
with st.sidebar:
    st.header("Configurações")
    ticker = st.text_input("Ativo", "BTC-USD").upper()
    capital = st.number_input("Capital (R$)", value=1000.0)
    risco = st.slider("Margem de Risco (%)", 1, 10, 5)

# Ação principal
if st.button("🚀 ATUALIZAR DADOS"):
    try:
        dados = yf.Ticker(ticker)
        preco = dados.history(period="1d")['Close'].iloc[-1]
        media = dados.history(period="5d")['Close'].mean()
        
        # Colunas de métricas
        col1, col2, col3 = st.columns(3)
        col1.metric("Preço Atual", f"R$ {preco:,.2f}")
        col2.metric("Média 5d", f"R$ {media:,.2f}")
        col3.metric("Capital", f"R$ {capital:,.2f}")
        
        st.markdown("---")
        
        # Lógica de decisão
        if preco < media:
            st.success("✅ OPORTUNIDADE: Preço abaixo da média móvel.")
        else:
            st.error("⚠️ AGUARDAR: Ativo acima da média.")
            
        # Gerenciamento
        st.subheader("Gerenciamento de Risco")
        stop_loss = preco * (1 - (risco/100))
        st.info(f"**STOP LOSS SUGERIDO:** R$ {stop_loss:,.2f}")
        
    except Exception:
        st.error("Erro ao buscar dados. Verifique o símbolo do ativo.")
        
