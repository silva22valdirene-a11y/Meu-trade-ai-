import streamlit as st
import yfinance as yf

st.title("🛡️ Trader Pro - Com Gestão de Risco")

ticker = st.text_input("Ativo (ex: BTC-USD ou PETR4.SA):", "BTC-USD")
capital_alocado = st.number_input("Capital para Operação (R$):", min_value=100.0, value=1000.0)

if st.button("Executar Análise"):
    try:
        dados = yf.Ticker(ticker)
        preco_atual = dados.history(period="1d")['Close'].iloc[-1]
        
        # Cálculo de Stop Loss (Margem de 5% de proteção)
        stop_loss = preco_atual * 0.95
        
        st.metric(f"Preço {ticker}", f"R$ {preco_atual:,.2f}")
        st.error(f"⚠️ Preço de Proteção (Stop Loss): R$ {stop_loss:,.2f}")
        
        # Lógica de decisão
        hist = dados.history(period="5d")
        media = hist['Close'].mean()
        
        if preco_atual < media:
            st.success("✅ SINAL: COMPRA")
            st.write(f"Gerenciamento: Se comprar hoje, coloque seu Stop Loss em R$ {stop_loss:,.2f}")
        else:
            st.warning("❌ SINAL: ESPERA (Risco alto)")
            
    except Exception as e:
        st.error("Erro ao conectar com o mercado. Verifique o código.")
        
