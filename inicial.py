import streamlit as st

# Configuração inicial
st.set_page_config(page_title="Insper Pay", page_icon="🍽️", layout="wide")

# Cabeçalho com HTML e CSS customizados
def header():
    st.markdown(
        """
        <style>
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 20px;
            background-color: #FFFFFF;
            border-bottom: 2px solid #EEEEEE;
        }
        .logo {
            font-size: 32px;
            color: #B22222;
            font-weight: bold;
            margin: 0;
        }
        .search-bar {
            width: 100%;
            max-width: 500px;
            padding: 8px;
            border-radius: 20px;
            border: 1px solid #DDDDDD;
        }
        .buttons-container {
            display: flex;
            gap: 10px;
        }
        .btn {
            background-color: #B22222;
            color: white;
            border: none;
            border-radius: 20px;
            padding: 8px 16px;
            font-size: 16px;
            cursor: pointer;
        }
        </style>
        <div class="header-container">
            <div class="logo">INSPER PAY</div>
            <input type="text" class="search-bar" placeholder="Pesquisar produtos...">
            <div class="buttons-container">
                <button class="btn" onclick="window.location.href='?page=Login'">Login</button>
                <button class="btn" onclick="window.location.href='?page=Cadastro'">Cadastro</button>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Seção de categorias e destaques com HTML e CSS
def product_section():
    st.markdown(
        """
        <style>
        .category-section, .highlight-section {
            margin: 20px 0;
        }
        .category-section h3, .highlight-section h3 {
            color: #333333;
            font-weight: bold;
        }
        .category-buttons {
            display: flex;
            gap: 15px;
            margin-top: 10px;
        }
        .category-button {
            background-color: #EEEEEE;
            padding: 12px 20px;
            border-radius: 10px;
            font-weight: bold;
            color: #B22222;
            cursor: pointer;
            text-align: center;
            width: 100%;
        }
        .highlight-cards {
            display: flex;
            gap: 20px;
            margin-top: 15px;
        }
        .highlight-card {
            background-color: #FAFAFA;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            width: 100%;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        }
        .highlight-card img {
            width: 100%;
            border-radius: 10px;
        }
        .highlight-card button {
            background-color: #B22222;
            color: white;
            padding: 8px 16px;
            border: none;
            border-radius: 20px;
            margin-top: 10px;
            cursor: pointer;
        }
        </style>
        
        <div class="category-section">
            <h3>Categorias</h3>
            <div class="category-buttons">
                <div class="category-button">Pratos</div>
                <div class="category-button">Bebidas</div>
                <div class="category-button">Sobremesas</div>
                <div class="category-button">Combos</div>
            </div>
        </div>
        
        <div class="highlight-section">
            <h3>Destaques</h3>
            <div class="highlight-cards">
                <div class="highlight-card">
                    <img src="https://via.placeholder.com/150" alt="Produto">
                    <h4>Produto Exemplo 1</h4>
                    <button>Ver detalhes</button>
                </div>
                <div class="highlight-card">
                    <img src="https://via.placeholder.com/150" alt="Produto">
                    <h4>Produto Exemplo 2</h4>
                    <button>Ver detalhes</button>
                </div>
                <div class="highlight-card">
                    <img src="https://via.placeholder.com/150" alt="Produto">
                    <h4>Produto Exemplo 3</h4>
                    <button>Ver detalhes</button>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Função para a tela de login
def login_page():
    st.subheader("Acesse sua conta")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        st.success("Login efetuado com sucesso!")
    if st.button("Voltar"):
        st.session_state["page"] = "Main"

# Função para a tela de cadastro
def register_page():
    st.subheader("Crie sua conta")
    username = st.text_input("Escolha um Usuário")
    password = st.text_input("Escolha uma Senha", type="password")
    if st.button("Cadastrar"):
        st.success("Cadastro realizado com sucesso!")
    if st.button("Voltar"):
        st.session_state["page"] = "Main"

# Definindo a navegação entre as páginas usando `st.session_state`
if "page" not in st.session_state:
    st.session_state["page"] = "Main"

# Verifica o parâmetro de URL para navegar entre páginas
query_params = st.query_params
if "page" in query_params:
    st.session_state["page"] = query_params["page"][0]

# Renderização das páginas com base no estado atual
if st.session_state["page"] == "Main":
    header()
    product_section()
elif st.session_state["page"] == "Login":
    header()  # Adicionando o cabeçalho à página de login
    login_page()
elif st.session_state["page"] == "Cadastro":
    header()  # Adicionando o cabeçalho à página de cadastro
    register_page()
