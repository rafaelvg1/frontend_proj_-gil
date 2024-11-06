import streamlit as st
import requests
st.set_page_config(page_title="Insper Pay", layout="centered")
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

col1,col2,col3=st.columns(3)
with col1:
    log,back=st.columns(2)
    with log:
# Botão de login
        if st.button("Login",use_container_width=True):
            login=post_login(BASE_URL,usuario,senha)
            if login == 201:
                st.switch_page("pages/front.py")
    with back:
        if st.button("Voltar",use_container_width=True):
            st.switch_page("front.py")
with col2:
        if st.button("Não tenho cadastro",use_container_width=False):
            st.switch_page("pages/cadastro.py")
with col3:
        st.link_button("Sou colaborador","https://hhenriquen-frontend-restaurante-front-restaurante-gklqi8.streamlit.app/")
             

