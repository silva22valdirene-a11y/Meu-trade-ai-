# Métrica rápida no topo (Layout Profissional)
col1, col2, col3 = st.columns(3)
col1.metric("Preço BTC", f"${preco:,.2f}", "+2.5%")
col2.metric("Volume 24h", "1.2B", "Alta")
col3.metric("RSI (14)", "58.2", "Neutro")

# Adicionando Médias Móveis ao gráfico do Plotly
fig.add_trace(go.Scatter(x=hist.index, y=hist['Close'].rolling(window=20).mean(), name="Média 20", line=dict(color='yellow', width=1)))
