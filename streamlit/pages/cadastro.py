import streamlit as st
import requests

BASE_URL = "https://insper-food-1-0oq8.onrender.com"

# Função para realizar o cadastro
def post_cadastro(BASE_URL, nome, usuario, email, senha, senha_confirm):
    if senha != senha_confirm:
        st.warning("As senhas não coincidem. Por favor, verifique.")
        return

    data = {
        "nome": nome,
        "usuario": usuario,
        "email": email,
        "senha": senha,
        "senha_confirm": senha_confirm
    }
    url = f"{BASE_URL}/cadastro"
    
    try:
        response = requests.post(url, json=data)

        if response.status_code == 201:
            st.success("Cadastro realizado com sucesso!")
            st.session_state.logged_in = False
            st.session_state.page = "login"  # Define a página alvo como 'login'
        elif response.status_code == 400:
            st.error("Erro ao fazer cadastro, verifique os dados informados")
            st.write("Detalhes do erro:", response.json())  # Exibe detalhes da resposta para debugging
        else:
            st.error(f"Erro desconhecido: {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"Erro de conexão com o servidor: {e}")

# Função principal para a página de cadastro
def run():
    # Título da página
    st.title("Página de Cadastro")

    # Campos de entrada para o cadastro
    nome = st.text_input("Nome Completo")
    usuario = st.text_input("Nome de Usuário")
    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")
    senha_confirm = st.text_input("Confirme a Senha", type="password")

    # Botão de cadastro, realiza a verificação apenas após o clique
    if st.button("Cadastrar", use_container_width=True):
        post_cadastro(BASE_URL, nome, usuario, email, senha, senha_confirm)

    # Botão para voltar para a página de login
    if st.button("Já tenho uma conta", use_container_width=True):
        st.session_state.page = "login"
