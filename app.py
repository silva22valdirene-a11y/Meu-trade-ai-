import ccxt
import os

# O GitHub vai inserir suas chaves aqui automaticamente
api_key = os.environ.get('MB_API_KEY')
api_secret = os.environ.get('MB_API_SECRET')

def executar_compra():
    exchange = ccxt.mercadobitcoin({'apiKey': api_key, 'secret': api_secret})
    
    # Define o que e quanto comprar
    symbol = 'BTC/BRL'
    valor_aporte = 50.00  # R$ 50,00 por compra
    
    ticker = exchange.fetch_ticker(symbol)
    price = ticker['last']
    amount_btc = valor_aporte / price
    
    # Cria a ordem de compra a preço de mercado
    order = exchange.create_market_buy_order(symbol, amount_btc)
    print(f"Compra realizada: {order}")

if __name__ == "__main__":
    executar_compra()
    
