import streamlit as st
import ccxt

st.set_page_config(page_title="Central de Acúmulo", layout="wide")

# Menu de Navegação
aba = st.sidebar.radio("Navegação", ["Dashboard", "Configurações"])

# --- ABA DE CONFIGURAÇÕES ---
if aba == "Configurações":
    st.title("⚙️ Conectar Corretora")
    st.write("Insira suas chaves de API da Binance (ou outra exchange).")
    
    api_key = st.text_input("API Key", type="password")
    api_secret = st.text_input("API Secret", type="password")
    
    if st.button("Salvar e Conectar"):
        st.session_state['api_key'] = api_key
        st.session_state['api_secret'] = api_secret
        st.success("Credenciais guardadas nesta sessão!")

# --- ABA DASHBOARD (COM SALDO) ---
elif aba == "Dashboard":
    st.title("💰 Central de Acúmulo (DCA)")
    
    if 'api_key' in st.session_state and 'api_secret' in st.session_state:
        try:
            exchange = ccxt.binance({
                'apiKey': st.session_state['api_key'],
                'secret': st.session_state['api_secret'],
                'enableRateLimit': True,
            })
            
            # Buscar saldo
            balance = exchange.fetch_balance()
            total_usdt = balance['total'].get('USDT', 0)
            
            st.metric("Saldo em USDT na Binance", f"USDT {total_usdt:,.2f}")
            st.success("Conectado com sucesso!")
            
        except Exception as e:
            st.error(f"Erro ao conectar: {e}")
    else:
        st.warning("Por favor, vá na aba 'Configurações' e conecte a sua API Key.")

    # Simulador DCA
    st.divider()
    valor_mensal = st.number_input("Investimento Mensal (R$)", value=100.0)
    if st.button("Simular Crescimento"):
        st.write(f"Você está acumulando R$ {valor_mensal} mensalmente.")
        
