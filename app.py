import streamlit as st
import yfinance as yf

# Configuração da página para ocupar a tela toda
st.set_page_config(page_title="Trader Pro", layout="centered")

# Estilo usando colunas e containers
st.title("📊 Trader Pro 3.0")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    ticker = st.text_input("Ativo", "BTC-USD").upper()

with col2:
    capital = st.number_input("Capital (R$)", min_value=100.0, value=1000.0)

if st.button("🚀 Executar Análise de Alta Performance"):
    try:
        dados = yf.Ticker(ticker)
        preco = dados.history(period="1d")['Close'].iloc[-1]
        media = dados.history(period="5d")['Close'].mean()
        stop_loss = preco * 0.95
        
        # Dashboard visual
        st.metric(label=f"Cotação Atual de {ticker}", value=f"R$ {preco:,.2f}")
        
        # Área de alerta com design diferenciado
        if preco < media:
            st.success("SINAL DETECTADO: COMPRA")
        else:
            st.error("SINAL DETECTADO: AGUARDAR")
            
        # Tabela de Riscos
        st.write("### Gerenciamento de Risco")
        st.info(f"**Stop Loss Sugerido:** R$ {stop_loss:,.2f}")
        
    except Exception:
        st.warning("Verifique o código do ativo.")
        
