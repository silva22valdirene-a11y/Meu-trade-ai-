import streamlit as st
import yfinance as yf

# Configuração de Layout
st.set_page_config(page_title="Trader Pro", layout="wide")

st.title("📊 Trader Pro 3.0")

# Inputs na lateral
with st.sidebar:
    st.header("Configurações")
    ticker = st.text_input("Ativo", "BTC-USD").upper()
    capital = st.number_input("Capital (R$)", value=1000.0)
    risco = st.slider("Margem de Risco (%)", 1, 10, 5)

# Tenta carregar os dados automaticamente
try:
    dados = yf.Ticker(ticker)
    hist = dados.history(period="5d")
    preco = hist['Close'].iloc[-1]
    media = hist['Close'].mean()
    
    # Exibe as métricas de imediato (sem precisar clicar)
    col1, col2 = st.columns(2)
    col1.metric("Preço Atual", f"R$ {preco:,.2f}")
    col2.metric("Média 5d", f"R$ {media:,.2f}")
    
    st.markdown("---")
    
    # Lógica de compra
    if preco < media:
        st.success("✅ OPORTUNIDADE DE COMPRA")
    else:
        st.warning("⚠️ AGUARDAR: Ativo sobrecomprado")
        
    # Risco
    stop_loss = preco * (1 - (risco/100))
    st.info(f"**STOP LOSS SUGERIDO:** R$ {stop_loss:,.2f}")

except:
    st.error("Digite um ativo válido (ex: BTC-USD)")
    
