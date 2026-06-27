import requests
import streamlit as st

def get_price():
    url = "https://api.mercadobitcoin.net/api/v4/tickers?symbols=BTC-BRL"
    try:
        response = requests.get(url)
        # Verifica se a requisição deu certo (status 200)
        if response.status_code == 200:
            data = response.json()
            # Verifica se os dados existem antes de acessar
            if 'tickers' in data and len(data['tickers']) > 0:
                return data['tickers'][0]['last']
            else:
                return "Erro: Estrutura da resposta inesperada."
        else:
            return f"Erro na API: {response.status_code}"
    except Exception as e:
        return f"Erro de conexão: {e}"

st.write("Preço atual do BTC:", get_price())

