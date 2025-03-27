import streamlit as st

st.markdown(
    """
    <style>
        body {
            background-color: #e3f2fd; /* Azul pastel claro */
            color: #0d47a1;
            font-family: Arial, sans-serif;
        }
        .login-box {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            width: 320px;
            margin: auto;
            margin-top: 100px;
            border-left: 5px solid #0d47a1;
            border-right: 5px solid #0d47a1;
        }
        
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            height: 30%;  
            background: linear-gradient(to right, #0d47a1, #1976d2);
            clip-path: polygon(0% 50%, 100% 30%, 100% 100%, 0% 100%);  
            color: white;
            text-align: center;
            padding-top: 40px;
            font-size: 16px;
            z-index: 9999;  
        }

        .footer-text {
            position: fixed;
            left: 0;
            bottom: 30px; /* Ajusta a posição vertical do texto */
            width: 100%;
            color: white;
            text-align: center;
            font-size: 18px;
            z-index: 10000;
        }

        .btn {
            background-color: #1976d2;
            color: white;
            padding: 0.5rem;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
            font-size: 16px;
        }
        .btn:hover {
            background-color: #0d47a1;
        }
        .input-box {
            width: 100%;
            padding: 0.5rem;
            margin-bottom: 1rem;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
    </style>
    <div class="footer"></div>
    <div class="footer-text">EPTV - Todos os direitos reservados © 2025</div>
    """,
    unsafe_allow_html=True
)

if 'menu_open' not in st.session_state:
    st.session_state.menu_open = False

def toggle_menu():
    st.session_state.menu_open = not st.session_state.menu_open

st.markdown(
    """
    <style>
        body {
            padding-top: 120px; /* Aumenta o espaço para o header */
        }
        .nav-bar {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #1976d2;
            padding: 30px 20px; /* Aumenta o padding para descer mais os elementos */
            z-index: 9999;
            box-shadow: 0px 4px 8px rgba(0,0,0,0.2);
            color: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
            height: 90px;
        }
        .nav-links {
            display: none;
            flex-direction: column;
            background-color: #1976d2;
            position: absolute;
            top: 90px;
            right: 0;
            width: 220px;
            box-shadow: 0px 4px 8px rgba(0,0,0,0.2);
            padding: 10px;
        }
        .nav-links a {
            color: white;
            padding: 18px;
            text-decoration: none;
            display: block;
            transition: background-color 0.2s;
            font-size: 18px;
        }
        .nav-links a:hover {
            background-color: #0d47a1;
        }
        .hamburger {
            display: block;
            cursor: pointer;
            font-size: 32px;
            color: white;
            background: none;
            border: none;
            outline: none;
            margin-top: 10px; /* Desce o botão hamburguer */
        }
        @media (min-width: 768px) {
            .hamburger {
                display: none;
            }
            .nav-links {
                display: flex;
                flex-direction: row;
                position: static;
                width: auto;
                box-shadow: none;
            }
            .nav-links a {
                padding: 14px 24px;
            }
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="nav-bar">
        <div class="logo">EPTV</div>
        <button class="hamburger" onclick="toggleMenu()">☰</button>
        <div class="nav-links" id="navLinks">
            <a href="#home">Home</a>
            <a href="#services">Serviços</a>
            <a href="#contact">Contato</a>
        </div>
    </div>

    <script>
        function toggleMenu() {
            var nav = document.getElementById("navLinks");
            if (nav.style.display === "flex") {
                nav.style.display = "none";
            } else {
                nav.style.display = "flex";
            }
        }
    </script>
    """,
    unsafe_allow_html=True
)


### Logo do site

st.markdown(
    """
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        <img src="https://upload.wikimedia.org/wikipedia/pt/6/67/EPTV.png" width="150"> 
    </div>
    """,

    unsafe_allow_html=True
)

if 'page' not in st.session_state:
    st.session_state.page = 'login'  # Defina a página inicial como 'login'

def show_login_page():
    st.markdown("#### Iniciar sessão abaixo:")
    username = st.text_input("Usuário", key="user", placeholder="Digite seu usuário")
    password = st.text_input("Senha", key="password", placeholder="Digite sua senha", type="password")
    
    if st.button("Entrar", key="login", help="Clique para entrar", use_container_width=True):
        if username == "admin" and password == "pass":
            st.session_state.authenticated = True
            st.session_state.page = 'principal'  # Altera para a página principal
            st.success("✅ Login realizado com sucesso!")
            st.experimental_rerun()  # Força a recarga da página
        else:
            st.error("❌ Usuário ou senha incorretos")

if st.session_state.get('authenticated'):
    st.switch_page("pages/pagina_principal.py")

show_login_page()
st.markdown('</div>', unsafe_allow_html=True)



