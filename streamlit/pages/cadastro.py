import streamlit as st
import requests

BASE_URL = "https://insper-food-1-0oq8.onrender.com"

# Função para realizar o cadastro
def post_cadastro(BASE_URL, usuario, senha):
    data = {"usuario": usuario, "senha": senha}
    url = f"{BASE_URL}/cadastro"
    
    response = requests.post(url, json=data)

    if response.status_code == 201:
        st.success("Cadastro realizado com sucesso! Faça login para continuar.")
        st.session_state.logged_in = False  # Define o estado de login como False após o cadastro
        st.switch_page("login")
    elif response.status_code == 400:
        st.error("Erro ao fazer cadastro, verifique os dados informados")
    else:
        st.error(f"Erro desconhecido: {response.text}")

# Função principal para a página de cadastro
def run():
    # Título da página
    st.title("Página de Cadastro")

    # Campos de entrada para o cadastro
    usuario = st.text_input("Nome de Usuário")
    senha = st.text_input("Senha", type="password")
    senha_confirm = st.text_input("Confirme a Senha", type="password")

    # Verifica se as senhas coincidem
    if senha != senha_confirm:
        st.warning("As senhas não coincidem. Por favor, verifique.")
    else:
        # Botão de cadastro
        if st.button("Cadastrar", use_container_width=True):
            post_cadastro(BASE_URL, usuario, senha)

    # Botão para voltar para a página de login
    if st.button("Já tenho uma conta", use_container_width=True):
        st.switch_page("login")
