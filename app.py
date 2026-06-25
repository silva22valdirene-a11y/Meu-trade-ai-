import streamlit as st
import ccxt

# Configuração da página
st.set_page_config(page_title="Trader Pro", layout="wide")
st.title("📊 Trader Pro | Dashboard 3.0")

# Criação das abas (Isto resolve o erro NameError)
tab1, tab2 = st.tabs(["📈 Análise de Mercado", "⚡ Execução Real"])

with tab1:
    st.header("Análise de Mercado")
    st.write("Gráfico em construção...")

with tab2:
    st.header("Terminal de Execução")
    
    try:
        # Configuração da conexão com a Binance
        exchange = ccxt.binance({
            'apiKey': st.secrets["BINANCE_API_KEY"],
            'secret': st.secrets["BINANCE_API_SECRET"]
        })
        
        # ATIVAÇÃO DO MODO SANDBOX (O "simulador" que resolve o erro de localização)
        exchange.set_sandbox_mode(True)
        
        # Comando para buscar o saldo
        balanco = exchange.fetch_balance()
        usdt = balanco['total'].get('USDT', 0)
        
        # Exibição do resultado
        st.metric("Saldo USDT Disponível", f"{usdt:,.2f}")
        st.success("Conectado ao modo de teste com sucesso!")
        
    except Exception as e:
        st.error(f"Erro ao carregar saldo: {e}")
        
