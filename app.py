import streamlit as st

# --- Configuração da Página ---
st.set_page_config(page_title="SafeTrade Mobile", page_icon="🔒")

# --- Simulação de Banco de Dados ---
# Esta lista guarda as contas que você já aprovou
contas_seguras = ["12345-6", "98765-4"] 

def verificar_saque(valor, destino):
    # Regra de Segurança: Só autoriza se a conta estiver na lista
    if destino in contas_seguras:
        return True, "Conta autorizada. Saque processando..."
    else:
        return False, "ALERTA: Conta desconhecida. Saque bloqueado por segurança!"

# --- Interface Visual ---
st.title("🔒 SafeTrade Mobile")
st.subheader("Painel de Saques Seguros")

# Campos de entrada que aparecerão no seu celular/PC
valor = st.number_input("Valor do Saque (R$)", min_value=0.0)
destino = st.text_input("Conta de Destino:")

# Botão de ação
if st.button("Solicitar Saque"):
    if valor > 0 and destino:
        autorizado, mensagem = verificar_saque(valor, destino)
        if autorizado:
            st.success(mensagem)
        else:
            st.error(mensagem)
    else:
        st.warning("Preencha todos os campos.")

# --- Rodapé ---
st.sidebar.info("Status: Protegido por Token Único")
