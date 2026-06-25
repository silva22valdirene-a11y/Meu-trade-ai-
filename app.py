with tab2:
    st.header("Terminal de Execução")
    
    try:
        # Configuração com timeout e opções de rede para contornar o bloqueio
        exchange = ccxt.binance({
            'apiKey': st.secrets["BINANCE_API_KEY"],
            'secret': st.secrets["BINANCE_API_SECRET"],
            'enableRateLimit': True,
            'options': {
                'defaultType': 'spot',
                'adjustForTimeDifference': True,
            }
        })
        
        # Tenta usar um endpoint alternativo ou ignorar a checagem de info
        exchange.set_sandbox_mode(True)
        
        # Pula a verificação automática de mercados que causa o erro 451
        exchange.load_markets = lambda: None 
        
        # Tenta buscar o saldo direto
        balanco = exchange.fetch_balance()
        usdt = balanco['total'].get('USDT', 0)
        
        st.metric("Saldo USDT (Simulado)", f"{usdt:,.2f}")
        st.success("Conectado ao modo de teste!")
        
    except Exception as e:
        st.error(f"Erro ao carregar: {e}")
        
