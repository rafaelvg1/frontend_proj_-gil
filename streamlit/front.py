import streamlit as st  # Streamlit é utilizado para criar interfaces web 
import requests  # Requests é utilizado para fazer requisições HTTP (GET, POST, etc.)
BASE_URL="https://insper-food-1-0oq8.onrender.com"
st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
def get_pratos(BASE_URL):
    url = f"{BASE_URL}/cardapio"
    response = requests.get(url)
    
    if response.status_code == 200:
        pratos = response.json()["itens_cardapio"]
        return pratos
    else:
        st.error("Erro ao buscar usuários")
        return []

left, mid, right = st.columns(3,vertical_alignment="center")
with st.container():
    st.divider()
    with left:
        st.title(":red[INSPER PAY]")
      
    with mid:
        pesquisa=st.text_input("","pesquise aqui")
        
    with right:
        bt1,bt2,bt3=st.columns(3)
        
        with bt1:
            st.write("")
            st.write("")
            if st.button("login",use_container_width=True):
                st.switch_page("pages/login.py")
        with bt2:
            st.write("")
            st.write("")
            if st.button("cadastro",use_container_width=True):
                st.switch_page("pages/cadastro.py")
        with bt3:
            st.write("")
            st.write("")
            if st.button("🛒",use_container_width=True):
                st.switch_page("pages/carrinho.py")


st.text("Filtros")
col1, col2, col3, col4, col5 = st.columns(5,vertical_alignment="center")

with col1:
    st.write("")
    if st.button("Sobremesas",use_container_width=True):
        st.write("Comidas")
        st.switch_page("pages/sobremesas.py")
    # st.image("https://static.streamlit.io/examples/cat.jpg")
    
    

with col2:
    st.write("")
    if st.button("Pratos",use_container_width=True):
        st.write("Pratos")
    # st.image("https://static.streamlit.io/examples/dog.jpg")

    

with col3:
    st.write("")
    if st.button("Bebidas",use_container_width=True):
        comidas=get_pratos(BASE_URL)
        st.write(comidas)

with col4:
    st.write("")
    if st.button("Combos", use_container_width=True):
        st.write("Oi")

with col5:
    st.write("")
    if st.button("Sla",use_container_width=True):
        st.write("oi")
    # st.image("https://static.streamlit.io/examples/owl.jpg")
import streamlit as st
st.divider()
# Cria duas colunas: uma para a área à esquerda e outra para a área à direita
col_esquerda, col_direita = st.columns(2,vertical_alignment="center")

# Conteúdo da área da esquerda
with col_esquerda:
    st.subheader("Strogonoff de frango")
    st.image("imgs/strogonoff.jpg" , width=300)  # Ajuste o tamanho conforme necessário
    with st.expander("Mais detalhes"):
        st.write('''
       Descrição do produto.
    ''')

# Conteúdo da área da direita
with col_direita:
    st.subheader("Área Direita")
    # st.image("caminho_para_sua_imagem_direita.jpg", caption="Imagem à direita", width=150)  # Ajuste o tamanho conforme necessário
    st.write("Texto descritivo para a área à direita.")



#funções:


    
