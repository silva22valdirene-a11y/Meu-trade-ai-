# Exemplo de configuração para o modo de testes
exchange = ccxt.binance({
    'apiKey': st.secrets["BINANCE_API_KEY"],
    'secret': st.secrets["BINANCE_API_SECRET"],
    'enableRateLimit': True,
})
exchange.set_sandbox_mode(True) # Ativa o ambiente de testes

