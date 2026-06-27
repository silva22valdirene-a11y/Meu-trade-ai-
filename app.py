# Em vez de chamar ccxt.mercadobitcoin({ ... }), use isto:
exchange = ccxt.load_exchange('mercadobitcoin')
exchange.apiKey = api_key
exchange.secret = api_secret
exchange.enableRateLimit = True
