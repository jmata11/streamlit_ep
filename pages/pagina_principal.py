import streamlit as st
import streamlit.components.v1 as components


if not st.session_state.get('authenticated'):
    st.error("❌ Acesso negado! Por favor, faça o login primeiro.")
    st.stop()


header_html = """
<div style="
    background-color: #ffffff; 
    padding: 10px; 
    border-bottom: 1px solid rgba(0, 0, 0, 0.08); 
    display: flex; 
    flex-direction: column; 
    align-items: flex-start; 
    gap: 10px;
    width: 100vw;
    box-sizing: border-box;
">

    <!-- Logo -->
    <img src="https://framerusercontent.com/images/pyxOhu5rvS6UBSMhyCX1PRrqJcs.png" alt="Logo" style="height: 40px; margin-bottom: 10px;">

    <!-- Menu principal -->
    <div style="display: flex; gap: 20px;">
        <a href="./" style="text-decoration: none; color: #666; font-family: Inter, sans-serif; font-size: 15px; font-weight: 500;">Insights</a>
        <a href="./atualizacoes" style="text-decoration: none; color: #666; font-family: Inter, sans-serif; font-size: 15px; font-weight: 500;">Atualizações</a>
        <a href="./chat" style="text-decoration: none; color: #666; font-family: Inter, sans-serif; font-size: 15px; font-weight: 500;">Chat</a>
    </div>

    <!-- Segundo Menu (Submenu) -->
    <div style="display: flex; gap: 20px; margin-top: 10px;">
        <a href="./perfil" style="text-decoration: none; color: #666; font-family: Inter, sans-serif; font-size: 15px; font-weight: 500;">Perfil</a>
        <a href="./configuracoes" style="text-decoration: none; color: #666; font-family: Inter, sans-serif; font-size: 15px; font-weight: 500;">Configurações</a>
        <a href="./suporte" style="text-decoration: none; color: #666; font-family: Inter, sans-serif; font-size: 15px; font-weight: 500;">Suporte</a>
    </div>

</div>
"""


components.html(header_html, height=180)

st.title("Bem-vindo à página principal!")
st.write("Você está logado como **admin**. Parabéns! 🎉")

if st.button("Sair"):
    st.session_state['authenticated'] = False
    st.success("✅ Logout realizado com sucesso!")
    st.query_params.clear("pagina_principal")
    st.rerun()

