import streamlit as st
from generator import generate_post, generate_description, generate_email
from predictor import predict_best_version

# ==============================
# CONFIGURAÇÃO DO APP
# ==============================
st.set_page_config(
    page_title="YouShop Genie",
    page_icon="💡",
    layout="wide"
)

# ==============================
# CSS PERSONALIZADO
# ==============================
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0B3D91 0%, #00B894 100%);
        color: white;
    }
    h1, h2, h3 {
        color: #ffffff !important;
        text-shadow: 1px 1px 2px #00000055;
    }
    section[data-testid="stSidebar"] {
        background-color: #0B3D91;
    }
    section[data-testid="stSidebar"] h2 {
        color: #00B894 !important;
    }
    div.stButton > button {
        background-color: #00B894;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        border: none;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #0984e3;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# ==============================
# HEADER
# ==============================
st.title("💡 YouShop Genie")
st.subheader("Seu assistente de conteúdo inteligente")
st.markdown("---")

# ==============================
# INTERFACE
# ==============================
option = st.sidebar.selectbox(
    "O que você deseja gerar?",
    ["Post para redes sociais", "Descrição de produto", "E-mail de marketing"]
)

user_input = st.text_area("Digite o nome do produto/curso:", "")

if st.button("✨ Gerar conteúdo"):
    if not user_input.strip():
        st.warning("Por favor, digite algo antes de gerar.")
    else:
        if option == "Post para redes sociais":
            output = generate_post(user_input)
        elif option == "Descrição de produto":
            output = generate_description(user_input)
        else:
            output = generate_email(user_input)

        st.success("✅ Conteúdo gerado com sucesso!")
        st.write(output)

        best = predict_best_version([output])
        st.info(f"Sugestão de destaque: {best}")

# ==============================
# RODAPÉ
# ==============================
st.markdown(
    """
    <div style="text-align:center; margin-top:2em; font-size:0.9em; color:#ffffffaa;">
    Feito com 💚💙 para o desafio de inovação da <b>YouShop</b>.
    </div>
    """,
    unsafe_allow_html=True
)