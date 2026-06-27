import streamlit as st
import requests

st.title("Central de Acúmulo (DCA)")

# Adicionamos um botão para evitar que o código tente rodar 
# automaticamente e trave na inicialização
if st.button("Buscar Preço Atual"):
    try:
        url = "https://api.mercadobitcoin.net/api/v4/tickers?symbols=BTC-BRL"
        st.write("Conectando à API...")
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            # Acesso seguro aos dados
            if isinstance(data, list) and len(data) > 0:
                preco = data[0].get('last')
                st.success(f"Preço atual do BTC: R$ {preco}")
            else:
                st.warning("Dados recebidos, mas em formato inesperado.")
                st.write(data)
        else:
            st.error(f"Erro na API: {response.status_code}")
            
    except Exception as e:
        st.error(f"Ocorreu um erro técnico: {e}")
      
