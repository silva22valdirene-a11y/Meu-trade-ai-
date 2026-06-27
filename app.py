# ... (após o sucesso da requisição)
    if response.status_code == 200:
        data = response.json()
        # Acessa o índice 0 da lista e a chave "last"
        preco_btc = data[0].get("last")
        st.success(f"Preço atual do BTC: R$ {preco_btc}")
        
