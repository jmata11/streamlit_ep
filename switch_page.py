import streamlit as st
from streamlit.runtime.scriptrunner import RerunData, RerunException
from streamlit.source_util import get_pages

def switch_page(page_name: str):
    # Função para padronizar o nome da página
    def standardize_name(name: str) -> str:
        return name.lower().replace("_", " ")

    # Padroniza o nome da página
    page_name = standardize_name(page_name)

    # Obtém as páginas configuradas no arquivo .streamlit/pages.toml
    pages = get_pages("tela_login.py")  
    for page_hash, config in pages.items():
        if standardize_name(config["page_name"]) == page_name:
            st.experimental_set_query_params(page=page_name)
            raise RerunException(RerunData(page_script_hash=page_hash, page_name=page_name))

    page_names = [standardize_name(config["page_name"]) for config in pages.values()]
    raise ValueError(f"Página {page_name} não encontrada. Deve ser uma das: {page_names}")
