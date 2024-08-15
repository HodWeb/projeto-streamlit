import streamlit as st
import pandas as pd
from datetime import date

def gravar_dados(nome, data_nasc, tipo):
    idade = (date.today() - data_nasc).days // 365  # Calcula a idade em anos
    if nome and data_nasc <= date.today() and idade >= 18:
        # Formata a data no formato dia/mês/ano
        data_nasc_formatada = data_nasc.strftime("%d/%m/%Y")
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome},{data_nasc_formatada},{tipo}\n")
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False

st.set_page_config(
    page_title="Cadastro de Clientes",
    page_icon="📒"
)

st.title("Cadastro de Clientes")
st.divider()

nome = st.text_input("Digite o nome do Cliente", 
                     key="Nome_cliente")
dt_nasc = st.date_input("Data de nascimento - Precisar ser maior de idade",
                        key="input_data",
                        format="DD/MM/YYYY")
tipo = st.selectbox("Tipo do cliente", 
                    ["Pessoa Física", "Pessoa Jurídica"])

btn_cadastrar = st.button("Cadastrar", on_click=gravar_dados, args=[nome, dt_nasc, tipo])

if btn_cadastrar:
    if st.session_state.get("sucesso"):
        st.success("Cliente Cadastrado com Sucesso!", icon="✅")
    else:
        st.error("Houve algum problema no cadastro!", icon="❌")
