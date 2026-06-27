# Use 'mercado_bitcoin' com underline
exchange = ccxt.mercado_bitcoin({
    'apiKey': api_key, 
    'secret': api_secret,
    'enableRateLimit': True,
})
