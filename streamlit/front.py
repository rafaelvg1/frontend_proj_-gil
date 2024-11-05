import streamlit as st
import requests
from pages.login import post_login
st.set_page_config(page_title="Insper Pay", layout="wide")
BASE_URL = "https://insper-food-1-0oq8.onrender.com"


# Função para buscar os pratos do cardápio
def get_pratos(BASE_URL):
    url = f"{BASE_URL}/cardapio"
    response = requests.get(url)
    
    if response.status_code == 200:
        pratos = response.json()["itens_cardapio"]
        return pratos
    else:
        st.error("Erro ao buscar o cardápio")
        return []

# Configuração da interface
left, mid, right = st.columns(3, vertical_alignment="center")
with st.container():
    st.divider()
    with left:
        st.title(":red[INSPER PAY]")
      
    with mid:
        # Campo de pesquisa
        pesquisa = st.text_input("Pesquise aqui", placeholder="Digite o nome do prato")

    with right:
        bt1, bt2, bt3 = st.columns(3)
        
        with bt1:
            st.write("")
            st.write("")
            if st.button("login", use_container_width=True):
                st.switch_page("pages/login.py")
        with bt2:
            st.write("")
            st.write("")
            if st.button("cadastro", use_container_width=True):
                st.switch_page("pages/cadastro.py")
        with bt3:
            st.write("")
            st.write("")
            if st.button("🛒", use_container_width=True):
                st.switch_page("pages/carrinho.py")

# Filtros (exemplo simples)
st.text("Filtros")
col1, col2, col3, col4, col5 = st.columns(5, vertical_alignment="center")

with col1:
    if st.button("Sobremesas", use_container_width=True):
        st.write("Sobremesas")
with col2:
    if st.button("Pratos", use_container_width=True):
        st.write("Pratos")
with col3:
    if st.button("Bebidas", use_container_width=True):
        st.write("Bebidas")
with col4:
    if st.button("Combos", use_container_width=True):
        st.write("Combos")
with col5:
    if st.button("Outros", use_container_width=True):
        st.write("Outros")

# Busca os pratos do cardápio
comidas = get_pratos(BASE_URL)

# Aplica o filtro de pesquisa
if pesquisa:
    comidas_filtradas = [comida for comida in comidas if pesquisa.lower() in comida["nome"].lower()]
else:
    comidas_filtradas = comidas

# Exibição dos itens do cardápio
st.divider()
col_esquerda, col_direita = st.columns(2, vertical_alignment="center")

# Conteúdo da área da direita
with col_direita:
    contador = 0
    lista_comida_direita = []
    for comida in comidas_filtradas:
        if contador % 2 == 1:
            col_checkbox, col_nome = st.columns([1, 4])
            with col_checkbox:
                selecionado = st.checkbox("", key=f"check_direita_{comida['nome']}")
                if selecionado:
                    lista_comida_direita.append(comida['codigo'])
            with col_nome:
                st.subheader(comida["nome"])
                # st.image(f'imgs/{comida["nome"]}.jpg', width=250)
                st.text(f"{comida['preco']} Reais")
        contador += 1

# Conteúdo da área da esquerda
with col_esquerda:
    contador = 0
    lista_comida_esquerda = []
    for comida in comidas_filtradas:
        if contador % 2 == 0:
            col_checkbox, col_nome = st.columns([1, 4])
            with col_checkbox:
                selecionado = st.checkbox("", key=f"check_esquerda_{comida['nome']}")
                if selecionado:
                    lista_comida_esquerda.append(comida['codigo'])
            with col_nome:
                st.subheader(comida["nome"])
                # st.image(f'imgs/{comida["nome"]}.jpg', width=250)
                st.text(f"{comida['preco']} Reais")
        contador += 1

# Coletando todos os itens selecionados
itens_selecionados = lista_comida_esquerda + lista_comida_direita

# Botão fixo na parte inferior para concluir o pedido
st.divider()
with st.container():
    if st.button("Concluir Pedido", use_container_width=True):
        if itens_selecionados:
            url_pedido = f"{BASE_URL}/pedidos"
            response = requests.post(url_pedido, json={"codigos_itens": itens_selecionados})
            if response.status_code == 201:
                st.success("Pedido realizado com sucesso!")
            else:
                st.error("Erro ao enviar o pedido.")
        else:
            st.warning("Selecione ao menos um item para concluir o pedido.")