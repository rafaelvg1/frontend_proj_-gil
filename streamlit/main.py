import streamlit as st
from streamlit_option_menu import option_menu
from pages import front
from pages import login
from pages import cadastro

st.set_page_config(page_title="Insper Pay", layout="wide")

# Menu de navegação
with st.sidebar:
    selected = option_menu(
        "Menu",
        ["Página Inicial", "Login", "Cadastro"],
        icons=["house", "person-circle", "person-plus"],
        menu_icon="cast",
        default_index=0,
    )

# Exibe a página selecionada
if selected == "Página Inicial":
    front.run()
elif selected == "Login":
    login.run()
elif selected == "Cadastro":
    cadastro.run()
