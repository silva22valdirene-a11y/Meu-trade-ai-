import streamlit as st
import ccxt

# ... (seus outros imports no topo)

with tab2:
    st.header("Terminal de Execução")
    
    # Verifica se os secrets existem
    if "BINANCE_API_KEY" in st.secrets:
        try:
            # Conexão
            exchange = ccxt.binance({
                'apiKey': st.secrets["BINANCE_API_KEY"],
                'secret': st.secrets["BINANCE_API_SECRET"],
                'enableRateLimit': True
            })
            
            # --- O COMANDO QUE FAZ APARECER ---
            # Busca o saldo e armazena na variável 'balanco'
            balanco = exchange.fetch_balance()
            
            # Extrai apenas o USDT
            usdt = balanco['total'].get('USDT', 0)
            
            # Exibe o número na tela
            st.metric("Saldo USDT Disponível", f"{usdt:,.2f}")
            
            st.success("Conectado e saldo carregado!")
            
        except Exception as erro:
            st.error(f"Erro na execução: {erro}")
    else:
        st.error("⚠️ Configuração de API ausente nos Secrets.")

    # Seus botões de compra/venda
    par = st.text_input("Par de Negociação", "BTC/USDT")
    qtd = st.number_input("Quantidade", value=0.001)
    
    col1, col2 = st.columns(2)
    if col1.button("🚀 COMPRAR"):
        st.write("Ordem processada.")
    if col2.button("🛑 VENDER"):
        st.write("Ordem processada.")
        
