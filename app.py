def assinar_e_executar():
    # A URL da API v4 para ordens é diferente
    url = "https://api.mercadobitcoin.net/api/v4/orders"
    
    # Parâmetros conforme a documentação da v4
    tonce = str(int(time.time() * 1000))
    params = {
        "pair": "BTC-BRL",
        "type": "buy",
        "quantity": "0.0001",
        "limit_price": "315000"
    }
    
    # Na v4, a assinatura é feita no corpo da requisição
    params_encoded = urllib.parse.urlencode(params)
    
    # Criando a assinatura (HMAC-SHA512)
    # Na v4, a assinatura geralmente usa o payload da requisição
    signature = hmac.new(API_SECRET.encode('utf-8'), 
                         params_encoded.encode('utf-8'), 
                         hashlib.sha512).hexdigest()
    
    headers = {
        'TAPI-ID': API_KEY,
        'TAPI-MAC': signature,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    response = requests.post(url, data=params_encoded, headers=headers)
    return response
    
