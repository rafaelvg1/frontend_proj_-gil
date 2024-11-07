import streamlit as st
from pages import cadastro, login, front  # Importe suas páginas aqui

# Inicializa o estado da página se ainda não estiver definido
if "page" not in st.session_state:
    st.session_state.page = "Página Inicial"  # Define a página inicial como padrão

# Função para definir a página de forma simples
def set_page(page_name):
    st.session_state.page = page_name

# Controle de navegação com base na página atual
if st.session_state.page == "login":
    login.run()  # Carrega a página de login
elif st.session_state.page == "cadastro":
    cadastro.run()  # Carrega a página de cadastro
else:
    front.run()  # Carrega a página principal (front.py)

# Menu de navegação
st.sidebar.title("Menu de Navegação")
if st.sidebar.button("Página Inicial"):
    set_page("Página Inicial")
if st.sidebar.button("Login"):
    set_page("login")
if st.sidebar.button("Cadastro"):
    set_page("cadastro")
