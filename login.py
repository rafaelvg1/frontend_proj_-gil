import streamlit as st

# Configuração inicial
st.set_page_config(page_title="Login - Insper Pay", page_icon="🍽️", layout="centered")

# Estilos CSS personalizados
st.markdown(
    """
    <style>
    .login-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 40px;
        border: 2px solid #EEEEEE;
        border-radius: 10px;
        max-width: 400px;
        margin: auto;
        background-color: #FAFAFA;
    }
    .login-logo {
        font-size: 32px;
        color: #B22222;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .input-field {
        width: 100%;
        padding: 10px;
        margin: 10px 0;
        border-radius: 5px;
        border: 1px solid #DDDDDD;
    }
    .login-button {
        width: 100%;
        background-color: #B22222;
        color: white;
        padding: 10px;
        border: none;
        border-radius: 5px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        margin-top: 20px;
    }
    .login-button:hover {
        background-color: #8B0000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Interface de Login
def login_page():
    
    st.markdown("<div class='login-logo'>INSPER PAY</div>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #333333;'>Login</h3>", unsafe_allow_html=True)

    matricula = st.text_input("Matrícula", key="matricula", help="Digite sua matrícula")
    senha = st.text_input("Senha", type="password", key="senha", help="Digite sua senha")

    # Botão de login estilizado
    login_button = st.markdown(
        "<button class='login-button'>Entrar</button>",
        unsafe_allow_html=True
    )

    if login_button and matricula and senha:
        st.success("Login efetuado com sucesso!")
    elif login_button:
        st.error("Por favor, preencha os campos de matrícula e senha.")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Executa a função da página de login
login_page()

