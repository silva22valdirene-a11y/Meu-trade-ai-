import streamlit as st

st.title("🔒 SafeTrade Mobile")
st.subheader("Painel de Saques Seguros")

# Lista de contas autorizadas
contas_seguras = ["12345-6", "98765-4"]

# Campos de entrada
valor = st.number_input("Valor do Saque (R$)", min_value=0.0, format="%.2f")
destino = st.text_input("Conta de Destino:")

# Botão de ação
if st.button("Solicitar Saque"):
    if valor > 5000.00:
        st.error("ALERTA: Saque bloqueado. O limite máximo é R$ 5.000,00.")
    elif destino not in contas_seguras:
        st.error("ALERTA: Conta desconhecida. Saque bloqueado por segurança!")
    elif valor > 0 and destino:
        st.success("Saque autorizado com sucesso!")
        st.balloons()
    else:
        st.warning("Por favor, preencha o valor e a conta.")
        
