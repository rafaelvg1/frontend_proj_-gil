import streamlit as st
import requests
from pages.login import post_login  # Caso o login seja usado para redirecionamento

# Função para buscar os pratos do cardápio
def get_pratos(BASE_URL):
    url = f"{BASE_URL}/cardapio"
    response = requests.get(url)
    
    if response.status_code == 200:
        pratos = response.json().get("itens_cardapio", [])
        return pratos
    else:
        st.error("Erro ao buscar o cardápio")
        return []

# Função principal para a página inicial
def run():
    BASE_URL = "https://insper-food-1-0oq8.onrender.com"

    # Garante que 'logged_in' e 'itens_selecionados' estejam inicializados no session state
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False  # Define como False inicialmente
    if "itens_selecionados" not in st.session_state:
        st.session_state.itens_selecionados = set()

    # Título e interface de pesquisa
    st.title("INSPER PAY")

    # Campo de pesquisa
    pesquisa = st.text_input("Pesquise aqui", placeholder="Digite o nome do prato")

    # Filtro de tipo de prato
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

    # Busca os pratos do cardápio
    comidas = get_pratos(BASE_URL)

    # Aplica o filtro de pesquisa e tipo
    if pesquisa:
        comidas_filtradas = [comida for comida in comidas if pesquisa.lower() in comida["nome"].lower()]
    else:
        comidas_filtradas = comidas

    if tipo_filtrado:
        comidas_filtradas = [comida for comida in comidas_filtradas if comida["tipo"] == tipo_filtrado]

    # Exibindo os pratos filtrados com imagens e caixas de seleção estilizadas
    col1, col2 = st.columns(2)

    with col1:
        for index, comida in enumerate(comidas_filtradas):
            if index % 2 == 0:
                with st.container():
                    selecionado = st.checkbox(
                        f"Selecionar {comida['nome']}", 
                        key=f"check_{comida['codigo']}",
                        value=comida['codigo'] in st.session_state.itens_selecionados
                    )
                    # st.image(f'streamlit/imgs/{comida["nome"]}.jpg', width=250)
                    if selecionado:
                        st.session_state.itens_selecionados.add(comida['codigo'])
                    else:
                        st.session_state.itens_selecionados.discard(comida['codigo'])
                    st.subheader(comida["nome"])
                    st.text(f"Preço: {comida['preco']} Reais")
                    st.text(f"Tipo: {comida['tipo']}")
                    st.divider()

    with col2:
        for index, comida in enumerate(comidas_filtradas):
            if index % 2 == 1:
                with st.container():
                    selecionado = st.checkbox(
                        f"Selecionar {comida['nome']}", 
                        key=f"check_{comida['codigo']}",
                        value=comida['codigo'] in st.session_state.itens_selecionados
                    
                    )
                    # st.image(f'streamlit/imgs/{comida["nome"]}.jpg', width=250)
                    if selecionado:
                        st.session_state.itens_selecionados.add(comida['codigo'])
                    else:
                        st.session_state.itens_selecionados.discard(comida['codigo'])
                    st.subheader(comida["nome"])
                    st.text(f"Preço: {comida['preco']} Reais")
                    st.text(f"Tipo: {comida['tipo']}")
                    st.divider()

    st.divider()
    if st.button("Concluir Pedido"):
        if not st.session_state.logged_in:
            st.warning("Você precisa estar logado para concluir o pedido.")
        elif st.session_state.itens_selecionados:
            url_pedido = f"{BASE_URL}/pedidos"
            try:
                response = requests.post(url_pedido, json={"codigos_itens": list(st.session_state.itens_selecionados)})
                if response.status_code == 201:
                    st.success("Pedido realizado com sucesso!")
                    st.session_state.itens_selecionados.clear()  # Limpa a seleção após concluir o pedido
                else:
                    st.error("Erro ao enviar o pedido.")
                    st.write("Resposta do servidor:", response.status_code, response.text)  # Exibe a resposta para debug
            except requests.exceptions.RequestException as e:
                st.error(f"Erro de conexão com o servidor: {e}")
        else:
            st.warning("Selecione ao menos um item para concluir o pedido.")

