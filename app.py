# Monitor de Operações
with st.expander("📝 Ver Ordens Abertas"):
    try:
        exchange = get_exchange()
        open_orders = exchange.fetch_open_orders(par)
        if open_orders:
            st.table(pd.DataFrame(open_orders))
        else:
            st.write("Nenhuma ordem aberta.")
    except:
        st.write("Conecte a API para ver ordens.")
      
