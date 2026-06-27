import requests
import streamlit as st

def get_price():
    url = "https://api.mercadobitcoin.net/api/v4/tickers?symbols=BTC-BRL"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # A resposta é uma lista, acessamos o primeiro item [0]
            # e pegamos o valor da chave 'last'
            if isinstance(data, list) and len(data) > 0:
                return data[0].get('last', 'Valor não encontrado')
            else:
                return "Erro: Formato de lista inesperado."
        else:
            return f"Erro HTTP: {response.status_code}"
    except Exception as e:
        return f"Erro: {e}"

# Exibe o preço na tela
st.write("Preço atual do BTC:", get_price())

