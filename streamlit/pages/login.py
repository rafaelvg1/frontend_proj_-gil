import streamlit as st
import requests
BASE_URL="https://insper-food-1-0oq8.onrender.com"
def post_login(BASE_URL,usuario,senha):
    data={"usuario":usuario,
          "senha":senha}
    url = f"{BASE_URL}/login"
    
    response = requests.post(url, json=data)

    if response.status_code == 200:
        st.success("Login realizado com sucessoooo!")
        st.switch_page("front.py")
    elif response.status_code == 400:
        st.error(f"Erro: {response.json()['erro']}")
    else:
        st.error(f"Erro desconhecido: {response.text}")

# Título da página
st.title("Página de Login")

# Campos de entrada para o login
usuario = st.text_input("Nome de Usuário")
senha = st.text_input("Senha", type="password")

# Botão de login
if st.button("Login"):
    login=post_login(BASE_URL,usuario,senha)
    if login == 201:
        st.switch_page("pages/front.py")

