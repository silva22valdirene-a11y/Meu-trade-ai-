import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Trader Pro", layout="centered")
st.title("📈 Trader Pro | Terminal Ágil")

# Entrada simples
ticker = st.sidebar.text_input("Ativo (ex: BTC-USD)", "BTC-USD")

if ticker:
    try:
        # Baixa dados com timeout definido
        df = yf.download(ticker, period="1mo", interval="1d", timeout=10)
        
        # Garante que o DataFrame seja lido corretamente
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
            
        if not df.empty and 'Close' in df.columns:
            # Cálculos de indicadores
            close = df['Close']
            sma_20 = close.rolling(20).mean()
            delta = close.diff()
            gain = (delta.where(delta > 0, 0)).rolling(14).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
            rsi = 100 - (100 / (1 + (gain / loss)))
            
            # Exibição dos dados
            st.metric("Preço Atual", f"US$ {float(close.iloc[-1]):,.2f}")
            
            # Gráfico unificado para economizar processamento
            st.line_chart(pd.DataFrame({
                "Preço": close,
                "SMA 20": sma_20
            }))
            
            st.line_chart(rsi.rename("RSI"))
            st.success("Dados carregados com sucesso!")
        else:
            st.warning("Aguardando resposta do servidor... tente atualizar.")
    except Exception as e:
        st.error("Erro de conexão. Verifique o ticker ou tente novamente.")
        
