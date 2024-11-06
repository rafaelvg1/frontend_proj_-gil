import streamlit as st
import requests
from requests.auth import HTTPBasicAuth

st.set_page_config(page_title="Insper Pay", layout="centered")
BASE_URL = "https://insper-food-1-0oq8.onrender.com"

# Função para login normal
def post_login(BASE_URL, usuario, senha):
    data = {"usuario": usuario, "senha": senha}
    url = f"{BASE_URL}/login"
    
    response = requests.post(url, json=data)

    if response.status_code == 200:
        st.success("Login realizado com sucesso!")
        st.session_state.logged_in = True  # Define o estado de login como True
        st.switch_page("front.py")
    elif response.status_code == 400:
        st.error(f"Erro: {response.json()['erro']}")
    else:
        st.error(f"Erro desconhecido: {response.text}")

# Função para autenticação de colaborador
def post_colaborador(BASE_URL, usuario, senha):
    url = f"{BASE_URL}/secret"
    
    # Envia as credenciais usando HTTP Basic Authentication
    response = requests.get(url, auth=HTTPBasicAuth(usuario, senha))

    if response.status_code == 200:
        st.success("Autenticação de colaborador realizada com sucesso!")

        # Redirecionamento para o URL externo usando JavaScript dentro do Streamlit
        st.experimental_set_query_params()
        st.markdown(
            """
            <meta http-equiv="refresh" content="0; url=https://hhenriquen-frontend-restaurante-front-restaurante-gklqi8.streamlit.app/" />
            """,
            unsafe_allow_html=True
        )
    else:
        st.error("Falha na autenticação de colaborador.")

# Título da página
st.title("Página de Login")

# Campos de entrada para o login
usuario = st.text_input("Nome de Usuário")
senha = st.text_input("Senha", type="password")

col1, col2, col3 = st.columns(3)
with col1:
    log, back = st.columns(2)
    with log:
        # Botão de login
        if st.button("Login", use_container_width=True):
            post_login(BASE_URL, usuario, senha)
    with back:
        if st.button("Voltar", use_container_width=True):
            st.switch_page("front.py")
with col2:
    if st.button("Não tenho cadastro", use_container_width=False):
        st.switch_page("pages/cadastro.py")
with col3:
    # Botão "Sou colaborador" com redirecionamento
    if st.button("Sou colaborador", use_container_width=True):
        post_colaborador(BASE_URL, usuario, senha)
