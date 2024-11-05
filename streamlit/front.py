import streamlit as st  # Streamlit é utilizado para criar interfaces web 
import requests  # Requests é utilizado para fazer requisições HTTP (GET, POST, etc.)
st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
# st.title("INSPER PAY")
# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )

# # Using "with" notation
# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )

col1, col2, col3, col4, col5 = st.columns(5)

with col1:


    if st.button("Sobremesas",use_container_width=True):
        st.write("Comidas")
        st.switch_page("pages/sobremesas.py")
    # st.image("https://static.streamlit.io/examples/cat.jpg")
    
    

with col2:
    if st.button("Pratos",use_container_width=True):
        st.write("Pratos")
    # st.image("https://static.streamlit.io/examples/dog.jpg")

    

with col3:
    if st.button("Bebidas",use_container_width=True):
        st.write("OI")

with col4:
    if st.button("Combos", use_container_width=True):
        st.write("Oi")

with col5:
    if st.button("Sla",use_container_width=True):
        st.write("oi")
    # st.image("https://static.streamlit.io/examples/owl.jpg")

# import streamlit as st



# with tab2:
#     st.header("A dog")
#     st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
# with tab3:
#     st.header("An owl")
#     st.image("https://static.streamlit.io/examples/owl.jpg", width=200)