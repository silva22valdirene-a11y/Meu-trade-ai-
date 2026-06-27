import requests
import streamlit as st

def get_price():
    url = "https://api.mercadobitcoin.net/api/v4/tickers?symbols=BTC-BRL"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # AQUI ESTÁ O SEGREDO: Vamos mostrar o que o site respondeu
            st.write("Dados recebidos da API:", data) 
            
            # Tente acessar de uma forma mais flexível
            if 'tickers' in data:
                return data['tickers'].get('BTC-BRL', {}).get('last', 'Não encontrado')
            return "Estrutura diferente da esperada"
        else:
            return f"Erro HTTP: {response.status_code}"
    except Exception as e:
        return f"Erro: {e}"

st.write("Preço atual do BTC:", get_price())
