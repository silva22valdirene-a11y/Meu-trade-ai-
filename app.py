import ccxt
import time

# Configuração da API
exchange = ccxt.binance({
    'apiKey': 'SUA_API_KEY',
    'secret': 'SUA_SECRET_KEY',
    'enableRateLimit': True,
})

def robô_de_lucro():
    while True:
        try:
            # 1. Busca dados do mercado
            ticker = 'BTC/USDT'
            ohlcv = exchange.fetch_ohlcv(ticker, timeframe='1h', limit=20)
            # ... (cálculo do RSI aqui)
            
            # 2. Lógica de Compra
            if rsi < 30:
                print("Sinal detectado: COMPRANDO...")
                exchange.create_market_buy_order(ticker, 0.001)
            
            # 3. Pausa para não ser bloqueado pela Binance
            time.sleep(60) 
            
        except Exception as e:
            print(f"Erro: {e}")
            time.sleep(10)

# robô_de_lucro()
