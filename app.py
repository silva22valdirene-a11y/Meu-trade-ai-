def executar_compra(valor_brl, preco_atual):
    # Rota TAPI v4 padrão
    url = "https://www.mercadobitcoin.net/tapi/v4/"
    
    # Payload estruturado para a TAPI
    payload = {
        "tapi_method": "place_order", # O método vai no corpo
        "pair": "BTC-BRL",
        "type": "buy",
        "quantity": f"{valor_brl / preco_atual:.8f}",
        "limit_price": f"{preco_atual:.2f}"
    }
    
    # A TAPI exige os parâmetros como formulário
    payload_encoded = urllib.parse.urlencode(payload)
    
    # Assinatura baseada no path + query string
    # Nota: a TAPI v4 requer assinatura sobre o caminho e os parâmetros
    signature = hmac.new(API_SECRET.encode('utf-8'), 
                         (url.replace("https://www.mercadobitcoin.net", "") + '?' + payload_encoded).encode('utf-8'), 
                         hashlib.sha512).hexdigest()
    
    headers = {
        'TAPI-ID': API_KEY,
        'TAPI-MAC': signature,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    return requests.post(url, data=payload_encoded, headers=headers)
    
