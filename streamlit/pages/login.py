import streamlit as st
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "https://insper-food-1-0oq8.onrender.com"

# Função para login normal
def post_login(BASE_URL, usuario, senha):
    data = {"usuario": usuario, "senha": senha}
    url = f"{BASE_URL}/login"
    
    response = requests.post(url, json=data)

    if response.status_code == 200:
        st.success("Login realizado com sucesso!")
        st.session_state.logged_in = True  # Define o estado de login como True
    elif response.status_code == 400:
        st.error("Erro ao fazer login, verifique se você informou corretamente os dados")
    else:
        st.error(f"Erro desconhecido: {response.text}")

# Função para autenticação de colaborador
def post_colaborador(BASE_URL, usuario, senha):
    url = f"{BASE_URL}/secret"
    
    # Envia as credenciais usando HTTP Basic Authentication
    response = requests.get(url, auth=HTTPBasicAuth(usuario, senha))

    if response.status_code == 200:
        st.success("Autenticação de colaborador realizada com sucesso!")
        # Redirecionamento externo
        st.markdown(
            """
            <meta http-equiv="refresh" content="0; url=https://hhenriquen-frontend-restaurante-front-restaurante-gklqi8.streamlit.app/" />
            """,
            unsafe_allow_html=True
        )
    else:
        st.error("Falha na autenticação de colaborador.")

# Função principal para a página de login
def run():
    # Título da página
    st.title("Página de Login")

    # Campos de entrada para o login
    usuario = st.text_input("Nome de Usuário")
    senha = st.text_input("Senha", type="password")

    # Botão de login
    if st.button("Login", use_container_width=True):
        post_login(BASE_URL, usuario, senha)

    # Botão para redirecionar para a página de cadastro
    if st.button("Não tenho cadastro", use_container_width=True):
        st.session_state.page = "cadastro"  # Define o estado da página para 'cadastro'
    
    # Botão para autenticação de colaborador
    if st.button("Sou colaborador", use_container_width=True):
        post_colaborador(BASE_URL, usuario, senha)

    # Botão para voltar para a página inicial
    if st.button("Voltar", use_container_width=True):
        st.session_state.page = "Página Inicial"
