import plotly.graph_objects as go

# No lugar do st.line_chart:
fig = go.Figure(data=[go.Candlestick(x=hist.index,
                open=hist['Open'], high=hist['High'],
                low=hist['Low'], close=hist['Close'])])
fig.update_layout(title="Preço em Tempo Real", template="plotly_dark")
st.plotly_chart(fig, use_container_width=True)
