import streamlit as st
import ccxt

# 1. Configuração da página (deve vir primeiro)
st.set_page_config(page_title="Trader Pro", layout="wide")
st.title("📊 Trader Pro | Dashboard 3.0")

# 2. DEFINIÇÃO DAS ABAS (Isto cria a variável tab2, agora o erro vai sumir)
tab1, tab2 = st.tabs(["📈 Análise de Mercado", "⚡ Execução Real"])

# 3. Uso das abas
with tab1:
    st.header("Análise de Mercado")
    st.write("Gráfico em construção...")

with tab2:
    st.header("Terminal de Execução")
    st.info("O acesso via nuvem (Streamlit Cloud) está restrito pela Binance.")
    st.write("Para execução real, rode este script no seu computador local.")
    
