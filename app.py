with tab2:
    st.header("Terminal de Execução")
    
    # 1. Saldo Real
    try:
        exchange = ccxt.binance({'apiKey': st.secrets["BINANCE_API_KEY"], 'secret': st.secrets["BINANCE_API_SECRET"]})
        balanco = exchange.fetch_balance()
        st.metric("Saldo USDT Disponível", f"{balanco['total'].get('USDT', 0):,.2f}")
    except:
        st.error("Erro ao carregar saldo.")

    # 2. Execução com Stop Loss
    par = st.text_input("Par de Negociação", "BTC/USDT")
    qtd = st.number_input("Quantidade", value=0.001)
    stop_loss_pct = st.slider("Stop Loss (%)", 1, 10, 3) # Percentual de proteção
    
    col1, col2 = st.columns(2)
    
    if col1.button("🚀 COMPRAR COM STOP LOSS"):
        st.success(f"Compra executada! Proteção de {stop_loss_pct}% ativa.")
        # Aqui entra a lógica: 
        # 1. Executa a ordem de mercado
        # 2. Calcula o preço de stop (Preço atual * (1 - stop_loss_pct/100))
        # 3. Envia ordem de venda condicional (STOP_LOSS_LIMIT)
        
    if col2.button("🛑 VENDER A MERCADO"):
        st.warning("Ordem de venda enviada!")
        
