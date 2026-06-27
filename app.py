import streamlit as st

st.title("💰 Central de Acúmulo (DCA)")

# Entrada do usuário
valor_mensal = st.number_input("Quanto você quer investir por mês (R$)?", min_value=10.0, value=100.0)
meta_anos = st.slider("Por quantos anos você vai investir?", 1, 30, 5)

if st.button("Simular Crescimento"):
    total_investido = valor_mensal * 12 * meta_anos
    st.write(f"Em {meta_anos} anos, você terá investido **R$ {total_investido:,.2f}**.")
    st.info("Essa é a sua base para criar patrimônio com segurança.")

st.subheader("Minha Carteira")
st.write("Aqui vamos conectar a sua corretora (Binance/Bybit) para mostrar o saldo atualizado.")
