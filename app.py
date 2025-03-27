import streamlit as st
from snowflake.snowpark.session import Session
import requests
import time
import streamlit.components.v1 as components
import polars as pl
import pandas as pd
import plotly.express as px
from snowflake.snowpark.functions import col



def authenticate(username, password):
    headers = {
    "usuario": f"{username}",
    "senha": f"{password}"
    }
    url = "https://servicos.cisp.com.br/v1/usuario/autentica"

    rr = requests.get(url, headers=headers, verify=False)
    
    if rr.status_code == 200:
        return True


def login():
    st.markdown("<h1 style='text-align: center; color: black;'>Área do Associado</h1>", unsafe_allow_html=True)
    with st.form(key='login_form'):
        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")
        submit_button = st.form_submit_button(label='Entrar')

    if submit_button:
        name = authenticate(username, password)
        if name == True:
            st.success("Login realizado com sucesso!")
            st.session_state['usuario'] = username
            st.session_state['associada'] = int(username[3:6]) 
            st.session_state.connection_established = True
            session.sql(f"INSERT INTO PRODUCAO.ANALYTICS.LOG_LOGIN_STREAMLIT (USUARIO , ASSOCIADA, DATA_HORA) values ('{st.session_state['usuario'].upper()}', {st.session_state['associada']}, DATEADD(HOUR, 4, current_timestamp()));").collect()
            time.sleep(2)
            st.experimental_rerun()
        else:
            st.error("Usuário ou senha incorretos!")

    if 'button_pressed' not in st.session_state:
        st.session_state['button_pressed'] = False
