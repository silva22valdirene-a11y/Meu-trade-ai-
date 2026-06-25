import ccxt
import time

# Use as suas chaves API (crie uma API Key na Binance com permissão de 'Spot Trading')
exchange = ccxt.binance({
    'apiKey': 'SUA_API_KEY',
    'secret': 'SUA_SECRET_KEY',
    'enableRateLimit': True,
})

def executar_bot():
    print("Robô iniciado...")
    ticker = 'BTC/USDT'
    
    while True:
        try:
            # Busca histórico de velas
            ohlcv = exchange.fetch_ohlcv(ticker, timeframe='1h', limit=20)
            close_prices = [candle[4] for candle in ohlcv]
            
            # Cálculo simples de média móvel para exemplo
            sma = sum(close_prices[-5:]) / 5
            preco_atual = close_prices[-1]
            
            # Estratégia: Se preço < média, compra
            if preco_atual < sma:
                print(f"Sinal de Compra: {preco_atual}")
                # exchange.create_market_buy_order(ticker, 0.001)
            
            time.sleep(60) # Espera 1 minuto entre checagens
            
        except Exception as e:
            print(f"Erro: {e}")
            time.sleep(60)

# Para rodar: basta executar este script
