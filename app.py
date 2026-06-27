import streamlit as st
import requests

st.title("Teste de Verificação")

# Botão para verificar se o app está vivo
if st.button("Testar Conexão"):
    try:
        # Apenas uma consulta pública (não precisa de chaves)
        url = "https://api.mercadobitcoin.net/api/v4/tickers?symbols=BTC-BRL"
        response = requests.get(url)
        
        if response.status_code == 200:
            st.success("Conexão OK! O app está funcionando.")
            st.write(response.json())
        else:
            st.error(f"Erro na conexão: Código {response.status_code}")
            
    except Exception as e:
        st.error(f"Erro crítico: {e}")
        
