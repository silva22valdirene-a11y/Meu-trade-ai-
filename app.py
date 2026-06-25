import streamlit as st
import yfinance as yf # Precisa adicionar no requirements.txt

st.title("📈 Trader Pro - Algoritmo de Análise")

# Configuração do Ativo (ex: PETR4.SA ou BTC-USD)
ticker_symbol = st.text_input("Digite o código do ativo (ex: BTC-USD):", "BTC-USD")

if st.button("Analisar Mercado"):
    try:
        # Busca dados reais
        dados = yf.Ticker(ticker_symbol)
        preco = dados.history(period="1d")['Close'].iloc[-1]
        
        st.metric(f"Preço Atual de {ticker_symbol}", f"R$ {preco:,.2f}")
        
        # Lógica de Competência (Média Móvel Simples)
        hist = dados.history(period="5d")
        media = hist['Close'].mean()
        
        if preco < media:
            st.success("Sinal: COMPRA (Preço abaixo da média de 5 dias)")
        else:
            st.warning("Sinal: AGUARDAR (Preço acima da média. Risco de correção.)")
            
    except Exception as e:
        st.error("Erro ao buscar dados. Verifique o código do ativo.")

st.info("Algoritmo operando com base em Média Móvel de 5 períodos.")
