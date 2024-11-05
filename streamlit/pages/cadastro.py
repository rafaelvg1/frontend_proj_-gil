import streamlit as st
import requests
BASE_URL="https://insper-food-1-0oq8.onrender.com"
def post_cadastro(BASE_URL, nome, email, nome_usuario,senha,):
    data = {
        "nome": nome,
        "email": email,
        "usuario": nome_usuario,
        "senha": senha
    }
    
    url = f"{BASE_URL}/cadastro"
    
    response = requests.post(url, json=data)
    
    if response.status_code == 201:
        st.success("Usuário adicionado com sucesso!")
        st.switch_page("pages/login.py")
    elif response.status_code == 400:
        st.error(f"Erro: {response.json()['erro']}")
    else:
        st.error(f"Erro desconhecido: {response.text}")

    
# Título da página de cadastro
st.title("Página de Cadastro")

# Campos de entrada para o cadastro
nome = st.text_input("Nome Completo")
email = st.text_input("Email")
nome_usuario = st.text_input("Nome de Usuário")
senha = st.text_input("Senha", type="password")
confirm_password = st.text_input("Confirme a Senha", type="password")

# Botão de criação de conta
if st.button("Criar Conta"):
    # Verifica se todos os campos estão preenchidos
    if not nome or not email or not nome_usuario or not senha or not confirm_password:
        st.warning("Por favor, preencha todos os campos.")
    elif senha != confirm_password:
        st.error("As senhas não coincidem. Tente novamente.")
    else:
        post_cadastro(BASE_URL,nome,email,nome_usuario,senha)
        




