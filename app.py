# --- SUBSTITUA O BLOCO DE SALDO POR ESTE ---
try:
    exchange = ccxt.binance({
        'apiKey': st.secrets["BINANCE_API_KEY"], 
        'secret': st.secrets["BINANCE_API_SECRET"],
        'enableRateLimit': True
    })
    # Tenta buscar o balanço
    balanco = exchange.fetch_balance()
    st.metric("Saldo USDT Disponível", f"{balanco['total'].get('USDT', 0):,.2f}")
except Exception as e:
    st.error(f"Erro detalhado da Binance: {e}")
    
