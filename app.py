import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Trader Pro", layout="wide")
st.title("📊 Trader Pro | Dashboard 3.0")

ticker = st.text_input("Digite o ativo (ex: BTC-USD ou PETR4.SA)", "BTC-USD")

if ticker:
    try:
        # Busca dados com tratamento de erro
        data = yf.download(ticker, period="1mo", interval="1d")
        
        if not data.empty:
            # Pega o valor de fechamento de forma segura
            ultimo_preco = data['Close'].iloc[-1]
            
            # Se for uma série, pegamos o valor escalar
            if isinstance(ultimo_preco, pd.Series):
                ultimo_preco = ultimo_preco.iloc[0]
            
            st.metric(f"Preço Atual de {ticker}", f"{float(ultimo_preco):,.2f}")
            st.line_chart(data['Close'])
            st.success("Dados carregados com sucesso!")
        else:
            st.warning("Não foram encontrados dados para este ticker. Tente outro.")
            
    except Exception as e:
        st.error(f"Erro ao buscar dados: {e}")
        
