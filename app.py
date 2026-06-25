import streamlit as st
import ccxt

# 1. Configuração da página (deve ser a primeira coisa)
st.set_page_config(page_title="Trader Pro", layout="wide")
st.title("📊 Trader Pro | Dashboard 3.0")

# 2. DEFINIÇÃO DAS ABAS (Isto cria as variáveis tab1 e tab2)
tab1, tab2 = st.tabs(["📈 Análise de Mercado", "⚡ Execução Real"])

# 3. Agora, e só agora, você pode usar tab1 e tab2
with tab1:
    st.header("Análise de Mercado")
    st.write("Gráfico em construção...")

with tab2:
    st.header("Execução Real")
    # Tente buscar o saldo apenas aqui, dentro da tab2
    try:
        exchange = ccxt.binance({
            'apiKey': st.secrets["BINANCE_API_KEY"],
            'secret': st.secrets["BINANCE_API_SECRET"]
        })
        balanco = exchange.fetch_balance()
        usdt = balanco['total'].get('USDT', 0)
        st.metric("Saldo USDT Disponível", f"{usdt:,.2f}")
    except Exception as e:
        st.error(f"Erro ao carregar saldo: {e}")
        
