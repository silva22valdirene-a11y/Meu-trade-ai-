import streamlit as st
import ccxt

st.title("🛡️ Trader Pro | Execução Binance")

# 1. Conexão com Binance (Dados vêm do Streamlit Secrets)
def get_exchange():
    return ccxt.binance({
        'apiKey': st.secrets["BINANCE_API_KEY"],
        'secret': st.secrets["BINANCE_API_SECRET"],
        'enableRateLimit': True,
        'options': {'defaultType': 'spot'}
    })

# 2. Sidebar de Controle de Ordem
with st.sidebar:
    st.header("Operação Real")
    ativo = st.text_input("Par de Negociação", "BTC/USDT").upper()
    quantidade = st.number_input("Quantidade", value=0.001)

# 3. Funções de Execução
if st.button("🚀 COMPRAR A MERCADO"):
    try:
        exchange = get_exchange()
        ordem = exchange.create_market_buy_order(ativo, quantidade)
        st.success(f"Compra executada! ID: {ordem['id']}")
    except Exception as e:
        st.error(f"Erro na execução: {e}")

if st.button("🛑 VENDER A MERCADO"):
    try:
        exchange = get_exchange()
        ordem = exchange.create_market_sell_order(ativo, quantidade)
        st.warning(f"Venda executada! ID: {ordem['id']}")
    except Exception as e:
        st.error(f"Erro na execução: {e}")

# 4. Verificação de Saldo
if st.button("Verificar Saldo"):
    try:
        exchange = get_exchange()
        balanco = exchange.fetch_balance()
        st.write(f"Saldo disponível (USDT): {balanco['total']['USDT']}")
    except Exception as e:
        st.error("Erro ao buscar saldo. Verifique suas chaves.")
        
