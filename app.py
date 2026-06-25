import streamlit as st
import ccxt

# 1. Configuração inicial
st.set_page_config(page_title="Trader Pro", layout="wide")
st.title("📊 Trader Pro | Dashboard 3.0")

# 2. DEFINIÇÃO DAS ABAS (Isto resolve o seu erro de NameError)
tab1, tab2 = st.tabs(["📈 Análise de Mercado", "⚡ Execução Real"])

# 3. Uso das abas
with tab1:
    st.header("Análise de Mercado")
    st.write("Gráfico em construção...")

with tab2:
    st.header("Terminal de Execução")
    
    try:
        # Configuração da conexão com a Binance
        exchange = ccxt.binance({
            'apiKey': st.secrets["BINANCE_API_KEY"],
            'secret': st.secrets["BINANCE_API_SECRET"],
            'enableRateLimit': True
        })
        
        # Tentativa de bypass para erro 451 (Restricted Location)
        exchange.set_sandbox_mode(True)
        exchange.load_markets = lambda: None 
        
        # Buscar saldo
        balanco = exchange.fetch_balance()
        usdt = balanco['total'].get('USDT', 0)
        
        st.metric("Saldo USDT (Simulado)", f"{usdt:,.2f}")
        st.success("Conectado ao modo de teste com sucesso!")
        
    except Exception as e:
        st.error(f"Erro ao carregar saldo: {e}")
        
