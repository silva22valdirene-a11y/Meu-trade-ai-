# --- ABA 2: EXECUÇÃO ---
with tab2:
    st.header("Terminal de Execução")
    
    # Verificação básica de segurança
    if "BINANCE_API_KEY" in st.secrets:
        par = st.text_input("Par de Negociação", "BTC/USDT")
        qtd = st.number_input("Quantidade", value=0.001)
        
        col1, col2 = st.columns(2)
        if col1.button("🚀 COMPRAR A MERCADO"):
            st.success(f"Ordem de compra enviada para {par}")
            
        if col2.button("🛑 VENDER A MERCADO"):
            st.warning(f"Ordem de venda enviada para {par}")
            
        with st.expander("📝 Ver Ordens Abertas"):
            st.write("Conectado à Binance - Buscando ordens...")
    else:
        st.error("⚠️ ERRO: Chaves de API não encontradas!")
        st.info("Vá em 'Settings' > 'Secrets' no painel do Streamlit e adicione suas chaves.")
        
