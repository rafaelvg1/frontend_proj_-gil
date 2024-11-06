import streamlit as st
import requests
from pages.login import post_login

# Configuração da página (deve ser a primeira chamada do Streamlit)
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

# Inicializa o estado de login no session state se ainda não estiver definido
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False  # Define como False inicialmente

# Inicializa a lista de itens selecionados no session state
if "itens_selecionados" not in st.session_state:
    st.session_state.itens_selecionados = set()

# Customizando o estilo do filtro com HTML e CSS
st.markdown("""
    <style>
    .stRadio > label {
        font-size: 16px;
        font-weight: bold;
    }
    div.stRadio > div > label > div {
        background-color: #f0f0f5;
        border-radius: 5px;
        padding: 8px 16px;
        margin-right: 8px;
        transition: 0.3s ease;
    }
    div.stRadio > div > label input:checked + div {
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Configuração da interface
left, mid, right = st.columns(3, vertical_alignment="center")
with st.container():
    st.divider()
    with left:
        st.title(":red[INSPER PAY]")
      
    with mid:
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

# Busca os pratos do cardápio
comidas = get_pratos(BASE_URL)

# Aplica o filtro de pesquisa
if pesquisa:
    comidas_filtradas = [comida for comida in comidas if pesquisa.lower() in comida["nome"].lower()]
else:
    comidas_filtradas = comidas

# Exibindo o filtro estilizado
st.text("Filtros")
filtro_selecionado = st.radio(
    "Escolha um filtro",
    options=["Todos", "Sobremesas", "Pratos", "Bebidas"],
    horizontal=True
)

# Mapeamento do filtro selecionado para o tipo correspondente
tipo_map = {
    "Todos": None,
    "Sobremesas": "sobremesa",
    "Pratos": "prato",
    "Bebidas": "bebida",
}
tipo_filtrado = tipo_map[filtro_selecionado]

# Exibe itens de acordo com o filtro selecionado
st.divider()
col_esquerda, col_direita = st.columns(2, vertical_alignment="center")

with col_direita:
    contador = 0
    for comida in comidas_filtradas:
        if (tipo_filtrado is None or comida["tipo"] == tipo_filtrado) and contador % 2 == 1:
            col_checkbox, col_nome = st.columns([1, 4])
            with col_checkbox:
                selecionado = st.checkbox(
                    "", 
                    key=f"check_direita_{comida['nome']}",
                    value=comida['codigo'] in st.session_state.itens_selecionados
                )
                if selecionado:
                    st.session_state.itens_selecionados.add(comida['codigo'])
                else:
                    st.session_state.itens_selecionados.discard(comida['codigo'])
            with col_nome:
                st.write()
                st.subheader(comida["nome"])
                # st.image(f'streamlit/imgs/{comida["nome"]}.jpg', width=250)
                st.text(f"{comida['preco']} Reais")
        contador += 1

with col_esquerda:
    contador = 0
    for comida in comidas_filtradas:
        if (tipo_filtrado is None or comida["tipo"] == tipo_filtrado) and contador % 2 == 0:
            col_checkbox, col_nome = st.columns([1, 4])
            with col_checkbox:
                selecionado = st.checkbox(
                    "", 
                    key=f"check_esquerda_{comida['nome']}",
                    value=comida['codigo'] in st.session_state.itens_selecionados
                )
                if selecionado:
                    st.session_state.itens_selecionados.add(comida['codigo'])
                else:
                    st.session_state.itens_selecionados.discard(comida['codigo'])
            with col_nome:
                st.write("")
                st.subheader(comida["nome"])
                # st.image(f'streamlit/imgs/{comida["nome"]}.jpg', width=250)
                st.text(f"{comida['preco']} Reais")
        contador += 1

# Botão fixo na parte inferior para concluir o pedido
st.divider()
with st.container():
    if st.button("Concluir Pedido", use_container_width=True):
        # Verifica se o usuário está logado
        if not st.session_state.logged_in:
            st.warning("Você precisa estar logado para concluir o pedido.")
            st.markdown(
                """
                <script>
                    window.location.href = "pages/login.py";
                </script>
                """,
                unsafe_allow_html=True
            )
        elif st.session_state.itens_selecionados:
            # Se o usuário está logado, tenta enviar o pedido
            url_pedido = f"{BASE_URL}/pedidos"
            response = requests.post(url_pedido, json={"codigos_itens": list(st.session_state.itens_selecionados)})
            if response.status_code == 201:
                st.success("Pedido realizado com sucesso!")
            else:
                st.error("Erro ao enviar o pedido.")
        else:
            st.warning("Selecione ao menos um item para concluir o pedido.")
