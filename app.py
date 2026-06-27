import ccxt
import os

# Pega as chaves diretamente das configurações do GitHub (Secrets)
api_key = os.environ.get('MB_API_KEY')
api_secret = os.environ.get('MB_API_SECRET')

def executar_compra():
    # Conecta no Mercado Bitcoin
    exchange = ccxt.mercadobitcoin({'apiKey': api_key, 'secret': api_secret})
    
    # Executa uma compra de mercado (Market Order)
    # Exemplo: Comprar R$ 50,00 de BTC/BRL
    symbol = 'BTC/BRL'
    amount_brl = 50.00
    
    ticker = exchange.fetch_ticker(symbol)
    price = ticker['last']
    amount_btc = amount_brl / price
    
    order = exchange.create_market_buy_order(symbol, amount_btc)
    print(f"Compra realizada com sucesso: {order}")

if __name__ == "__main__":
    executar_compra()
    
